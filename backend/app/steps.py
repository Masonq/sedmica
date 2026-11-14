# -*- coding: utf-8 -*-
"""Cooking steps per recipe, RU + SR. Concise, 3-5 steps."""

STEPS = {
    "oatmeal_banana": {
        "ru": ["Вскипяти молоко, всыпь хлопья и вари 5 минут, помешивая.", "Добавь сахар, сними с огня и дай постоять 2 минуты.", "Нарежь банан кружочками и выложи сверху."],
        "sr": ["Zagrej mleko, dodaj pahuljice i kuvaj 5 minuta uz mešanje.", "Dodaj šećer, skloni sa vatre i ostavi 2 minuta.", "Iseci bananu na kolutove i poređaj preko kaše."],
    },
    "oatmeal_apple": {
        "ru": ["Вскипяти молоко, всыпь хлопья и вари 5 минут.", "Натри яблоко на крупной тёрке, добавь с изюмом в кашу.", "Перемешай и дай постоять под крышкой 2 минуты."],
        "sr": ["Zagrej mleko, dodaj pahuljice i kuvaj 5 minuta.", "Narendaj jabuku, dodaj je sa suvim grožđem u kašu.", "Promešaj i ostavi poklopljeno 2 minuta."],
    },
    "syrniki": {
        "ru": ["Разомни творог с яйцом, сахаром и мукой до однородной массы.", "Сформируй шайбы, обваляй в муке.", "Жарь на среднем огне по 3–4 минуты с каждой стороны.", "Подавай со сметаной."],
        "sr": ["Izgnječi sir sa jajetom, šećerom i brašnom u glatku masu.", "Oblikuj pljoskice i uvaljaj ih u brašno.", "Prži na srednjoj vatri 3–4 minuta sa svake strane.", "Posluži sa pavlakom."],
    },
    "scrambled_veg": {
        "ru": ["Нарежь помидор и перец, обжарь 3 минуты на масле.", "Вбей яйца, посоли и жарь до готовности, помешивая.", "Подавай с хлебом."],
        "sr": ["Iseci paradajz i papriku, prži 3 minuta na ulju.", "Umuti jaja, posoli i prži uz mešanje do gotovosti.", "Posluži uz hleb."],
    },
    "omelet_cheese": {
        "ru": ["Взбей яйца с молоком и солью.", "Вылей на разогретую сковороду, посыпь тёртым сыром.", "Накрой крышкой и готовь 5–6 минут на слабом огне."],
        "sr": ["Umuti jaja sa mlekom i solju.", "Sipaj na zagrejan tiganj, pospi rendanim sirom.", "Poklopi i spremaj 5–6 minuta na tihoj vatri."],
    },
    "pancakes": {
        "ru": ["Смешай муку, молоко, яйцо и сахар в жидкое тесто без комков.", "Жарь тонкие блины на горячей сковороде по минуте с каждой стороны.", "Смазывай маслом и складывай стопкой."],
        "sr": ["Umuti brašno, mleko, jaje i šećer u glatko testo.", "Prži tanke palačinke po minut sa svake strane.", "Premaži maslacem i slaži na gomilu."],
    },
    "semolina": {
        "ru": ["Вскипяти молоко с сахаром.", "Тонкой струйкой всыпь манку, постоянно помешивая.", "Вари 3–4 минуты, добавь масло."],
        "sr": ["Zagrej mleko sa šećerom do ključanja.", "U tankom mlazu sipaj griz uz stalno mešanje.", "Kuvaj 3–4 minuta, dodaj maslac."],
    },
    "toast_tuna": {
        "ru": ["Разомни тунца со сметаной.", "Намажь на хлеб, сверху выложи кружочки огурца.", "По желанию подсуши хлеб в тостере."],
        "sr": ["Izgnječi tunjevinu sa pavlakom.", "Namaži na hleb, preko poređaj kolutove krastavca.", "Po želji tostiraj hleb."],
    },
    "toast_cheese": {
        "ru": ["Смажь хлеб маслом, положи сыр и ломтик помидора.", "Запеки в духовке или на сковороде под крышкой до расплавления сыра."],
        "sr": ["Premaži hleb maslacem, stavi sir i krišku paradajza.", "Zapeci u rerni ili na tiganju dok se sir ne istopi."],
    },
    "yogurt_bowl": {
        "ru": ["Налей йогурт в миску.", "Добавь нарезанный банан, хлопья и орехи.", "Перемешай перед подачей."],
        "sr": ["Sipaj jogurt u činiju.", "Dodaj iseckanu bananu, pahuljice i orahe.", "Promešaj pre služenja."],
    },
    "cottage_bowl": {
        "ru": ["Выложи творог в миску, добавь сметану и сахар.", "Перемешай, сверху — нарезанное яблоко."],
        "sr": ["Stavi sir u činiju, dodaj pavlaku i šećer.", "Promešaj, preko dodaj iseckanu jabuku."],
    },
    "smoothie": {
        "ru": ["Сложи банан, молоко и хлопья в блендер.", "Взбей 30–40 секунд до однородности."],
        "sr": ["Stavi bananu, mleko i pahuljice u blender.", "Blendaj 30–40 sekundi dok ne bude glatko."],
    },
    "proja": {
        "ru": ["Смешай муку, яйцо, йогурт и масло.", "Добавь раскрошенный сыр, перемешай.", "Выпекай в форме при 200 °C 25–30 минут до золотистой корочки."],
        "sr": ["Pomešaj brašno, jaje, jogurt i ulje.", "Dodaj izmrvljen sir i promešaj.", "Peci u kalupu na 200 °C 25–30 minuta do zlatne korice."],
    },
    "egg_toast_avocado": {
        "ru": ["Подсуши хлеб, смажь маслом.", "Свари яйцо-пашот: 3 минуты в едва кипящей воде с уксусом.", "Выложи яйцо на тост, посыпь зеленью."],
        "sr": ["Tostiraj hleb i premaži maslacem.", "Poširaj jaje 3 minuta u vodi koja jedva ključa.", "Stavi jaje na tost i pospi peršunom."],
    },
    "fr_toast": {
        "ru": ["Взбей яйцо с молоком и сахаром.", "Обмакни ломтики хлеба в смесь.", "Обжарь с двух сторон до золотистости."],
        "sr": ["Umuti jaje sa mlekom i šećerom.", "Umoči kriške hleba u smesu.", "Prži sa obe strane do zlatne boje."],
    },
    "mushroom_omelet": {
        "ru": ["Обжарь нарезанные шампиньоны 5 минут.", "Залей взбитыми яйцами, посоли.", "Готовь под крышкой 4–5 минут. Подавай с хлебом."],
        "sr": ["Prži iseckane šampinjone 5 minuta.", "Prelij umućenim jajima i posoli.", "Spremaj poklopljeno 4–5 minuta. Posluži uz hleb."],
    },
    "chicken_soup": {
        "ru": ["Залей бёдра водой, доведи до кипения, сними пену, вари 25 минут.", "Добавь картофель, морковь и лук, вари 10 минут.", "Всыпь вермишель, вари ещё 5 минут.", "Посоли, добавь зелень."],
        "sr": ["Prelij batake vodom, prokuvaj, skini penu i kuvaj 25 minuta.", "Dodaj krompir, šargarepu i luk, kuvaj 10 minuta.", "Ubaci rezance i kuvaj još 5 minuta.", "Posoli i dodaj peršun."],
    },
    "borsch": {
        "ru": ["Свари бульон на бёдрах 25 минут, мясо разбери.", "Добавь картофель и капусту, вари 10 минут.", "Обжарь лук с морковью и томатной пастой, отправь в кастрюлю.", "Вари 10 минут. Подавай со сметаной."],
        "sr": ["Skuvaj supu od bataka 25 minuta, meso iseckaj.", "Dodaj krompir i kupus, kuvaj 10 minuta.", "Pri dinstaj luk, šargarepu i paradajz pire, dodaj u lonac.", "Kuvaj još 10 minuta. Posluži sa pavlakom."],
    },
    "pasulj": {
        "ru": ["Замочи фасоль на ночь, слей воду.", "Вари фасоль 40 минут.", "Обжарь лук и морковь с томатной пастой, добавь в кастрюлю.", "Вари до мягкости, посоли и дай настояться."],
        "sr": ["Potopi pasulj preko noći i ocedi.", "Kuvaj pasulj 40 minuta.", "Prodinstaj luk i šargarepu sa paradajz pireom, dodaj u lonac.", "Kuvaj do mekoće, posoli i ostavi da odstoji."],
    },
    "lentil_soup": {
        "ru": ["Промой чечевицу.", "Обжарь лук и морковь, добавь чечевицу, пасту и воду.", "Вари 25 минут до мягкости, посоли."],
        "sr": ["Operi sočivo.", "Prodinstaj luk i šargarepu, dodaj sočivo, pire i vodu.", "Kuvaj 25 minuta do mekoće, posoli."],
    },
    "chicken_rice": {
        "ru": ["Нарежь филе кубиками, обжарь 7 минут.", "Добавь овощную смесь, жарь 5 минут.", "Всыпь рис, залей водой 1:2, туши под крышкой 15 минут."],
        "sr": ["Iseci belo meso na kockice i prži 7 minuta.", "Dodaj mešano povrće i prži 5 minuta.", "Dodaj pirinač, nalij vodu 1:2 i dinstaj poklopljeno 15 minuta."],
    },
    "chicken_buckwheat": {
        "ru": ["Прокрути филе с луком, добавь яйцо и соль.", "Сформируй котлеты, обжарь по 5–6 минут с каждой стороны.", "Отвари гречку: 1 часть крупы на 2 части воды, 15 минут."],
        "sr": ["Sameljite meso sa lukom, dodaj jaje i so.", "Oblikuj ćufte i prži 5–6 minuta sa svake strane.", "Skuvaj heljdu: 1 deo heljde na 2 dela vode, 15 minuta."],
    },
    "pasta_bolognese": {
        "ru": ["Обжарь лук, добавь фарш и жарь 7 минут.", "Влей протёртые томаты, туши 10 минут, посоли.", "Отвари пасту, смешай с соусом."],
        "sr": ["Prodinstaj luk, dodaj mleveno meso i prži 7 minuta.", "Dodaj pasirani paradajz, dinstaj 10 minuta i posoli.", "Skuvaj testeninu i pomešaj sa sosom."],
    },
    "pasta_tuna": {
        "ru": ["Отвари макароны.", "Обжарь чеснок, добавь томаты и тунца, прогрей 5 минут.", "Смешай соус с макаронами."],
        "sr": ["Skuvaj testeninu.", "Prodinstaj beli luk, dodaj paradajz i tunjevinu, zagrevaj 5 minuta.", "Pomešaj sos sa testeninom."],
    },
    "hake_potato": {
        "ru": ["Отвари картофель, разомни с молоком и маслом.", "Посоли хека, сбрызни лимоном.", "Обжарь или запеки рыбу 15–20 минут.", "Подавай с пюре."],
        "sr": ["Skuvaj krompir i izgnječi ga sa mlekom i maslacem.", "Posoli oslića i poprskaj limunom.", "Prži ili zapeci ribu 15–20 minuta.", "Posluži uz pire."],
    },
    "djuvec": {
        "ru": ["Обжарь бёдра до корочки, убери со сковороды.", "Обжарь лук, перец и помидоры 5 минут.", "Добавь рис, воду 1:2, сверху курицу.", "Туши или запекай 25–30 минут."],
        "sr": ["Zapeci batake do korice i skloni ih.", "Prodinstaj luk, papriku i paradajz 5 minuta.", "Dodaj pirinač, vodu 1:2, preko stavi piletinu.", "Dinstaj ili peci 25–30 minuta."],
    },
    "stuffed_pepper": {
        "ru": ["Смешай фарш с рисом, луком и солью.", "Начини очищенные перцы.", "Залей протёртыми томатами и туши 40 минут под крышкой.", "Подавай со сметаной."],
        "sr": ["Pomešaj mleveno meso sa pirinčem, lukom i solju.", "Napuni očišćene paprike.", "Prelij pasiranim paradajzom i dinstaj 40 minuta poklopljeno.", "Posluži sa pavlakom."],
    },
    "musaka": {
        "ru": ["Нарежь картофель тонкими кружками.", "Обжарь фарш с луком.", "Выложи слоями: картофель, фарш, картофель.", "Залей смесью яйца с молоком, запекай 40 минут при 190 °C."],
        "sr": ["Iseci krompir na tanke kolutove.", "Isprži mleveno meso sa lukom.", "Slaži redove: krompir, meso, krompir.", "Prelij jajima umućenim sa mlekom i peci 40 minuta na 190 °C."],
    },
    "rice_liver": {
        "ru": ["Обжарь лук с морковью.", "Добавь печень, жарь 7–8 минут.", "Отвари рис и подай с печенью."],
        "sr": ["Prodinstaj luk i šargarepu.", "Dodaj džigericu i prži 7–8 minuta.", "Skuvaj pirinač i posluži uz džigericu."],
    },
    "chick_stew": {
        "ru": ["Обжарь лук, добавь кабачок и помидоры.", "Туши 10 минут, добавь нут из банки.", "Прогрей 5 минут, посоли, добавь специи."],
        "sr": ["Prodinstaj luk, dodaj tikvice i paradajz.", "Dinstaj 10 minuta, dodaj leblebiju iz konzerve.", "Zagrevaj 5 minuta, posoli i začini."],
    },
    "turkey_veg": {
        "ru": ["Нарежь индейку, обжарь 8 минут.", "Добавь кабачок, перец и морковь.", "Туши под крышкой 15 минут, посоли."],
        "sr": ["Iseci ćuretinu i prži 8 minuta.", "Dodaj tikvice, papriku i šargarepu.", "Dinstaj poklopljeno 15 minuta i posoli."],
    },
    "potato_mush_stew": {
        "ru": ["Обжарь лук и грибы 7 минут.", "Добавь картофель кубиками и воду до половины.", "Туши 20 минут, добавь сметану и прогрей."],
        "sr": ["Prodinstaj luk i pečurke 7 minuta.", "Dodaj krompir na kockice i vodu do pola.", "Dinstaj 20 minuta, dodaj pavlaku i zagrej."],
    },
    "pork_stew": {
        "ru": ["Нарежь свинину, обжарь до корочки.", "Добавь лук и томатную пасту, залей водой.", "Туши 40 минут до мягкости.", "Подавай с картофельным пюре."],
        "sr": ["Iseci svinjetinu i zapeci do korice.", "Dodaj luk i paradajz pire, nalij vodu.", "Dinstaj 40 minuta do mekoće.", "Posluži uz pire krompir."],
    },
    "spinach_rice": {
        "ru": ["Обжарь лук, добавь шпинат и прогрей.", "Всыпь рис, залей водой 1:2, туши 15 минут.", "Подавай с варёным яйцом."],
        "sr": ["Prodinstaj luk, dodaj spanać i zagrej.", "Dodaj pirinač, nalij vodu 1:2 i dinstaj 15 minuta.", "Posluži sa kuvanim jajetom."],
    },
    "cutlets_mash": {
        "ru": ["Смешай фарш с размоченным хлебом, яйцом и солью.", "Сформируй котлеты, обжарь по 6–7 минут с каждой стороны.", "Отвари картофель, разомни с молоком и маслом."],
        "sr": ["Pomešaj mleveno meso sa namočenim hlebom, jajetom i solju.", "Oblikuj ćufte i prži 6–7 minuta sa svake strane.", "Skuvaj krompir i izgnječi sa mlekom i maslacem."],
    },
    "chicken_bake": {
        "ru": ["Натри бёдра солью, чесноком и маслом.", "Выложи с дольками картофеля на противень.", "Запекай 45 минут при 200 °C до румяной корочки."],
        "sr": ["Natrljaj batake solju, belim lukom i uljem.", "Poređaj sa krompirom na pleh.", "Peci 45 minuta na 200 °C do rumene korice."],
    },
    "fish_cutlets": {
        "ru": ["Прокрути хека с хлебом, добавь яйцо и соль.", "Сформируй котлеты, обжарь по 5 минут с каждой стороны.", "Подавай с картофельным пюре."],
        "sr": ["Sameljite oslića sa hlebom, dodaj jaje i so.", "Oblikuj pljeskavice i prži 5 minuta sa svake strane.", "Posluži uz pire krompir."],
    },
    "buck_mushroom": {
        "ru": ["Обжарь лук и грибы до золотистости.", "Добавь гречку и воду 1:2.", "Туши под крышкой 15 минут, посоли."],
        "sr": ["Prodinstaj luk i pečurke do zlatne boje.", "Dodaj heljdu i vodu 1:2.", "Dinstaj poklopljeno 15 minuta i posoli."],
    },
    "sarma_lazy": {
        "ru": ["Нашинкуй капусту, обжарь с луком 7 минут.", "Добавь фарш, жарь 7 минут.", "Всыпь рис, залей томатами, туши 25 минут.", "Подавай со сметаной."],
        "sr": ["Iseckaj kupus i prodinstaj sa lukom 7 minuta.", "Dodaj mleveno meso i prži 7 minuta.", "Dodaj pirinač, prelij paradajzom i dinstaj 25 minuta.", "Posluži sa pavlakom."],
    },
    "tortilla_chicken": {
        "ru": ["Обжарь полоски курицы 7–8 минут.", "Нарежь овощи, разогрей тортилью.", "Собери: сметана, курица, овощи, сыр — и сверни."],
        "sr": ["Prži trakice piletine 7–8 minuta.", "Iseci povrće i zagrej tortilju.", "Složi: pavlaka, piletina, povrće, sir — i uvij."],
    },
    "pilav": {
        "ru": ["Обжарь курицу до корочки.", "Добавь лук и морковь, жарь 5 минут.", "Всыпь рис, чеснок, залей водой 1:2.", "Туши под крышкой 20 минут не перемешивая."],
        "sr": ["Zapeci piletinu do korice.", "Dodaj luk i šargarepu, prži 5 minuta.", "Dodaj pirinač, beli luk i vodu 1:2.", "Dinstaj poklopljeno 20 minuta bez mešanja."],
    },
    "veg_stew_dinner": {
        "ru": ["Обжарь курицу 7 минут.", "Добавь картофель, кабачок, морковь и лук.", "Залей водой до половины, туши 25 минут."],
        "sr": ["Prži piletinu 7 minuta.", "Dodaj krompir, tikvice, šargarepu i luk.", "Nalij vodu do pola i dinstaj 25 minuta."],
    },
    "mac_cheese": {
        "ru": ["Отвари макароны.", "Растопи масло с молоком, добавь тёртый сыр.", "Смешай соус с макаронами и прогрей."],
        "sr": ["Skuvaj makarone.", "Istopi maslac sa mlekom, dodaj rendani sir.", "Pomešaj sos sa makaronama i zagrej."],
    },
    "baked_fish_veg": {
        "ru": ["Нарежь овощи, выложи на противень с рыбой.", "Посоли, сбрызни маслом и лимоном.", "Запекай 30 минут при 190 °C."],
        "sr": ["Iseci povrće i poređaj na pleh sa ribom.", "Posoli, poprskaj uljem i limunom.", "Peci 30 minuta na 190 °C."],
    },
    "beans_sausage_free": {
        "ru": ["Отвари фасоль до мягкости.", "Обжарь много лука до золотистости, добавь морковь и пасту.", "Смешай с фасолью и запеки 20 минут при 180 °C."],
        "sr": ["Skuvaj pasulj do mekoće.", "Prodinstaj dosta luka do zlatne boje, dodaj šargarepu i pire.", "Pomešaj sa pasuljem i zapeci 20 minuta na 180 °C."],
    },
    "zapekanka": {
        "ru": ["Смешай творог, яйцо, манку, сахар и изюм.", "Выложи в форму, смажь сметаной.", "Запекай 35–40 минут при 180 °C."],
        "sr": ["Pomešaj sir, jaje, griz, šećer i suvo grožđe.", "Stavi u kalup i premaži pavlakom.", "Peci 35–40 minuta na 180 °C."],
    },
    "potato_pancakes": {
        "ru": ["Натри картофель и лук, отожми жидкость.", "Добавь яйцо и муку, посоли.", "Жарь оладьи по 3–4 минуты с каждой стороны.", "Подавай со сметаной."],
        "sr": ["Narendaj krompir i luk, ocedi tečnost.", "Dodaj jaje i brašno, posoli.", "Prži palačinke 3–4 minuta sa svake strane.", "Posluži sa pavlakom."],
    },
    "tofu_rice": {
        "ru": ["Обжарь кубики тофу до корочки.", "Добавь брокколи и морковь, жарь 5 минут.", "Подавай с отварным рисом."],
        "sr": ["Prži kockice tofua do korice.", "Dodaj brokoli i šargarepu, prži 5 minuta.", "Posluži uz kuvani pirinač."],
    },
    "grill_chicken_salad": {
        "ru": ["Отбей филе, посоли, обжарь на гриле по 5–6 минут со стороны.", "Нарежь овощи, заправь маслом и лимоном.", "Нарежь курицу и подай с салатом."],
        "sr": ["Izlupaj belo meso, posoli i peci na grilu 5–6 minuta po strani.", "Iseci povrće i začini uljem i limunom.", "Iseci piletinu i posluži sa salatom."],
    },
    "egg_fried_rice": {
        "ru": ["Отвари рис заранее.", "Обжарь лук и морковь, сдвинь, поджарь яйцо.", "Добавь рис и кукурузу, жарь 5 минут, помешивая."],
        "sr": ["Skuvaj pirinač unapred.", "Prži luk i šargarepu, pomeri ih, isprži jaje.", "Dodaj pirinač i kukuruz, prži 5 minuta uz mešanje."],
    },
    "sardine_potato": {
        "ru": ["Отвари картофель дольками.", "Обжарь лук, добавь сардины и прогрей.", "Смешай с картофелем, посыпь зеленью."],
        "sr": ["Skuvaj krompir na kriške.", "Prodinstaj luk, dodaj sardine i zagrej.", "Pomešaj sa krompirom i pospi peršunom."],
    },
    "pita_zeljanica": {
        "ru": ["Замеси тесто из муки, йогурта и масла, раскатай два пласта.", "Смешай шпинат с сыром и яйцом.", "Собери пирог, смажь маслом.", "Выпекай 35 минут при 190 °C."],
        "sr": ["Zamesi testo od brašna, jogurta i ulja, razvuci dve kore.", "Pomešaj spanać sa sirom i jajetom.", "Složi pitu i premaži uljem.", "Peci 35 minuta na 190 °C."],
    },
}
