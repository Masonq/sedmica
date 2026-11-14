#!/usr/bin/env bash
# Sedmica: first install + update. Run as root on the VPS.
set -e
APP=/var/www/sedmica
git config --global --add safe.directory /var/www/sedmica 2>/dev/null || true
REPO=https://github.com/Masonq/sedmica.git
if [ ! -d "$APP/.git" ]; then git clone "$REPO" "$APP"; fi
cd "$APP"
git fetch origin
git reset --hard origin/main
echo "DEPLOYED COMMIT: $(git log --oneline -1)"
if [ ! -d .venv ]; then python3 -m venv .venv; fi
.venv/bin/pip install -q -r backend/requirements.txt
cd frontend && npm install --silent && npm run build && cd ..
cp deploy/sedmica.service /etc/systemd/system/sedmica.service
chown -R www-data:www-data "$APP"
systemctl daemon-reload
systemctl enable --now sedmica >/dev/null 2>&1
systemctl restart sedmica
ufw allow 8102/tcp >/dev/null 2>&1 || true
sleep 2
curl -sf http://127.0.0.1:8102/api/meta >/dev/null && echo "SEDMICA OK: http://89.208.113.147:8102" || (journalctl -u sedmica -n 20 --no-pager; exit 1)
