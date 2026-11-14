# -*- coding: utf-8 -*-
"""Sedmica seed data: ingredients (RSD prices, Serbian stores) and recipes.

Prices are realistic averages for Serbia (late 2026). base price = Maxi;
per-store multipliers applied in generator.
"""

STORES = [
    {"id": "lidl", "name": "Lidl", "mult": 0.93, "tag_ru": "дешевле всего", "tag_sr": "najjeftinije"},
    {"id": "maxi", "name": "Maxi", "mult": 1.0, "tag_ru": "рядом с домом", "tag_sr": "u komšiluku"},
    {"id": "idea", "name": "Idea", "mult": 1.02, "tag_ru": "рядом с домом", "tag_sr": "u komšiluku"},
    {"id": "univer", "name": "Univerexport", "mult": 1.0, "tag_ru": "низкие цены", "tag_sr": "niske cene"},
    {"id": "dis", "name": "DIS", "mult": 0.95, "tag_ru": "дискаунтер", "tag_sr": "diskonter"},
    {"id": "aroma", "name": "Aroma", "mult": 1.04, "tag_ru": "у дома", "tag_sr": "u blizini"},
    {"id": "roda", "name": "Roda", "mult": 0.98, "tag_ru": "большой выбор", "tag_sr": "veliki izbor"},
    {"id": "tempo", "name": "Tempo", "mult": 0.96, "tag_ru": "гипермаркет", "tag_sr": "hipermarket"},
]

CITIES = ["Beograd", "Novi Sad", "Niš", "Kragujevac", "Subotica", "Pančevo", "Zrenjanin", "Čačak", "Kraljevo", "Novi Pazar"]

ALLERGENS = [
    {"id": "nuts", "ru": "Орехи", "sr": "Orašasti plodovi", "emoji": "🥜"},
    {"id": "peanut", "ru": "Арахис", "sr": "Kikiriki", "emoji": "🥜"},
    {"id": "milk", "ru": "Молоко", "sr": "Mleko", "emoji": "🥛"},
    {"id": "eggs", "ru": "Яйца", "sr": "Jaja", "emoji": "🥚"},
    {"id": "gluten", "ru": "Глютен", "sr": "Gluten", "emoji": "🌾"},
    {"id": "fish", "ru": "Рыба", "sr": "Riba", "emoji": "🐟"},
    {"id": "seafood", "ru": "Морепродукты", "sr": "Morski plodovi", "emoji": "🦐"},
    {"id": "soy", "ru": "Соя", "sr": "Soja", "emoji": "🫘"},
]

EQUIPMENT = [
    {"id": "stove", "ru": "Плита", "sr": "Šporet", "emoji": "🔥"},
    {"id": "oven", "ru": "Духовка", "sr": "Rerna", "emoji": "🥧"},
    {"id": "micro", "ru": "Микроволновка", "sr": "Mikrotalasna", "emoji": "📡"},
    {"id": "multi", "ru": "Мультиварка", "sr": "Multikuker", "emoji": "🍲"},
    {"id": "airfryer", "ru": "Аэрогриль", "sr": "Air fryer", "emoji": "🌀"},
    {"id": "blender", "ru": "Блендер", "sr": "Blender", "emoji": "🥤"},
    {"id": "grillpan", "ru": "Сковорода-гриль", "sr": "Gril tiganj", "emoji": "🍳"},
]

STOP_SUGGESTIONS = [
    {"ru": "Свинина", "sr": "Svinjetina"}, {"ru": "Говядина", "sr": "Junetina"},
    {"ru": "Грибы", "sr": "Pečurke"}, {"ru": "Лук", "sr": "Crni luk"},
    {"ru": "Баклажаны", "sr": "Plavi patlidžan"}, {"ru": "Печень", "sr": "Džigerica"},
    {"ru": "Творог", "sr": "Mladi sir"}, {"ru": "Тофу", "sr": "Tofu"},
    {"ru": "Брокколи", "sr": "Brokoli"}, {"ru": "Цветная капуста", "sr": "Karfiol"},
    {"ru": "Перловка", "sr": "Ječam"}, {"ru": "Сельдерей", "sr": "Celer"},
]

# categories for shopping list
CATS = {
    "meat": {"ru": "Мясо, рыба, яйца", "sr": "Meso, riba, jaja", "emoji": "🍗"},
    "dairy": {"ru": "Молочное", "sr": "Mlečni proizvodi", "emoji": "🧀"},
    "veg": {"ru": "Овощи и фрукты", "sr": "Voće i povrće", "emoji": "🥦"},
    "grocery": {"ru": "Бакалея", "sr": "Bakalnica", "emoji": "🌾"},
    "other": {"ru": "Прочее", "sr": "Ostalo", "emoji": "🧂"},
}

# ing: id, ru, sr, cat, pack (qty in base unit), unit(g|ml|pcs), pack_label_ru/sr, price RSD per pack, allergens, stop keys
def I(id, ru, sr, cat, pack, unit, lab_ru, lab_sr, price, allergens=(), stop=()):
    return {"id": id, "ru": ru, "sr": sr, "cat": cat, "pack": pack, "unit": unit,
            "lab_ru": lab_ru, "lab_sr": lab_sr, "price": price,
            "allergens": list(allergens), "stop": list(stop)}

INGREDIENTS = [
    I("chicken", "Куриное филе", "Pileće belo meso", "meat", 1000, "g", "1 кг", "1 kg", 749),
    I("chicken_legs", "Куриные бёдра", "Pileći batak", "meat", 1000, "g", "1 кг", "1 kg", 489),
    I("pork", "Свинина (лопатка)", "Svinjska plećka", "meat", 1000, "g", "1 кг", "1 kg", 699, stop=("свинина", "svinjetina")),
    I("beef_mince", "Фарш говяжий", "Mleveno juneće meso", "meat", 500, "g", "500 г", "500 g", 649, stop=("говядина", "junetina")),
    I("mince_mix", "Фарш смешанный", "Mleveno mešano meso", "meat", 500, "g", "500 г", "500 g", 449, stop=("свинина", "svinjetina")),
    I("turkey", "Индейка (филе)", "Ćureće belo meso", "meat", 500, "g", "500 г", "500 g", 629),
    I("hake", "Хек (филе)", "Oslić file", "meat", 500, "g", "500 г", "500 g", 589, allergens=("fish",)),
    I("sardines", "Сардины конс.", "Sardina konzerva", "meat", 100, "g", "банка 100 г", "konzerva 100 g", 169, allergens=("fish",)),
    I("tuna", "Тунец конс.", "Tunjevina konzerva", "meat", 160, "g", "банка 160 г", "konzerva 160 g", 329, allergens=("fish",)),
    I("eggs", "Яйца", "Jaja", "meat", 10, "pcs", "10 шт", "10 kom", 339, allergens=("eggs",)),
    I("liver", "Куриная печень", "Pileća džigerica", "meat", 500, "g", "500 г", "500 g", 269, stop=("печень", "džigerica")),

    I("milk", "Молоко 2,8%", "Mleko 2,8%", "dairy", 1000, "ml", "1 л", "1 l", 139, allergens=("milk",)),
    I("yogurt", "Йогурт", "Jogurt", "dairy", 1000, "ml", "1 л", "1 l", 189, allergens=("milk",)),
    I("kajmak", "Каймак", "Kajmak", "dairy", 250, "g", "250 г", "250 g", 379, allergens=("milk",)),
    I("cottage", "Творог (млади сыр)", "Mladi sir", "dairy", 500, "g", "500 г", "500 g", 329, allergens=("milk",), stop=("творог", "mladi sir")),
    I("sour_cream", "Сметана 20%", "Pavlaka 20%", "dairy", 400, "g", "400 г", "400 g", 219, allergens=("milk",)),
    I("cheese", "Сыр (гауда)", "Gauda sir", "dairy", 400, "g", "400 г", "400 g", 489, allergens=("milk",)),
    I("feta", "Белый сыр", "Beli sir", "dairy", 400, "g", "400 г", "400 g", 419, allergens=("milk",)),
    I("butter", "Масло сливочное", "Maslac", "dairy", 250, "g", "250 г", "250 g", 429, allergens=("milk",)),

    I("potato", "Картофель", "Krompir", "veg", 2000, "g", "2 кг", "2 kg", 199),
    I("onion", "Лук репчатый", "Crni luk", "veg", 1000, "g", "1 кг", "1 kg", 109, stop=("лук", "crni luk", "luk")),
    I("carrot", "Морковь", "Šargarepa", "veg", 1000, "g", "1 кг", "1 kg", 129),
    I("cabbage", "Капуста", "Kupus", "veg", 1500, "g", "кочан ~1,5 кг", "glavica ~1,5 kg", 149),
    I("tomato", "Помидоры", "Paradajz", "veg", 1000, "g", "1 кг", "1 kg", 249),
    I("cucumber", "Огурцы", "Krastavac", "veg", 500, "g", "500 г", "500 g", 139),
    I("pepper", "Перец сладкий", "Paprika", "veg", 1000, "g", "1 кг", "1 kg", 269),
    I("zucchini", "Кабачки", "Tikvice", "veg", 1000, "g", "1 кг", "1 kg", 199),
    I("eggplant", "Баклажаны", "Plavi patlidžan", "veg", 1000, "g", "1 кг", "1 kg", 259, stop=("баклажаны", "patlidžan")),
    I("mushrooms", "Шампиньоны", "Šampinjoni", "veg", 400, "g", "400 г", "400 g", 249, stop=("грибы", "pečurke", "šampinjoni")),
    I("broccoli", "Брокколи (зам.)", "Brokoli (zamrznut)", "veg", 400, "g", "400 г", "400 g", 229, stop=("брокколи", "brokoli")),
    I("frozen_veg", "Овощная смесь (зам.)", "Mešano povrće (zamrznuto)", "veg", 450, "g", "450 г", "450 g", 199),
    I("banana", "Бананы", "Banane", "veg", 1000, "g", "1 кг", "1 kg", 219),
    I("apple", "Яблоки", "Jabuke", "veg", 1000, "g", "1 кг", "1 kg", 139),
    I("lemon", "Лимон", "Limun", "veg", 300, "g", "300 г", "300 g", 119),
    I("garlic", "Чеснок", "Beli luk", "veg", 100, "g", "100 г", "100 g", 99),
    I("greens", "Зелень (петрушка)", "Peršun", "veg", 50, "g", "пучок", "veza", 59),
    I("spinach", "Шпинат (зам.)", "Spanać (zamrznut)", "veg", 450, "g", "450 г", "450 g", 219),

    I("rice", "Рис", "Pirinač", "grocery", 1000, "g", "1 кг", "1 kg", 219),
    I("buckwheat", "Гречка", "Heljda", "grocery", 500, "g", "500 г", "500 g", 299),
    I("pasta", "Макароны", "Testenina", "grocery", 500, "g", "500 г", "500 g", 129, allergens=("gluten",)),
    I("oats", "Овсяные хлопья", "Ovsene pahuljice", "grocery", 500, "g", "500 г", "500 g", 159, allergens=("gluten",)),
    I("flour", "Мука", "Brašno", "grocery", 1000, "g", "1 кг", "1 kg", 109, allergens=("gluten",)),
    I("bread", "Хлеб", "Hleb", "grocery", 500, "g", "векна 500 г", "vekna 500 g", 99, allergens=("gluten",)),
    I("tortilla", "Тортильи", "Tortilje", "grocery", 370, "g", "6 шт", "6 kom", 249, allergens=("gluten",)),
    I("lentils", "Чечевица", "Sočivo", "grocery", 500, "g", "500 г", "500 g", 249),
    I("beans", "Фасоль", "Pasulj", "grocery", 500, "g", "500 г", "500 g", 269),
    I("chickpeas", "Нут конс.", "Leblebija konzerva", "grocery", 400, "g", "банка 400 г", "konzerva 400 g", 189),
    I("corn", "Кукуруза конс.", "Kukuruz šećerac", "grocery", 340, "g", "банка 340 г", "konzerva 340 g", 159),
    I("tomato_paste", "Томатная паста", "Paradajz pire", "grocery", 185, "g", "185 г", "185 g", 129),
    I("passata", "Томаты протёртые", "Pasirani paradajz", "grocery", 500, "g", "500 г", "500 g", 169),
    I("oil", "Масло подсолнечное", "Suncokretovo ulje", "grocery", 1000, "ml", "1 л", "1 l", 189),
    I("sugar", "Сахар", "Šećer", "grocery", 1000, "g", "1 кг", "1 kg", 129),
    I("barley", "Перловка", "Ječam", "grocery", 500, "g", "500 г", "500 g", 179, allergens=("gluten",), stop=("перловка", "ječam")),
    I("semolina", "Манка (гриз)", "Griz", "grocery", 500, "g", "500 г", "500 g", 139, allergens=("gluten",)),

    I("salt_spices", "Соль и специи", "So i začini", "other", 1, "pcs", "набор", "set", 249),
    I("walnuts", "Грецкие орехи", "Orasi", "other", 200, "g", "200 г", "200 g", 449, allergens=("nuts",)),
    I("raisins", "Изюм", "Suvo grožđe", "other", 200, "g", "200 г", "200 g", 199),
    I("tofu", "Тофу", "Tofu", "other", 300, "g", "300 г", "300 g", 379, allergens=("soy",), stop=("тофу", "tofu")),
]

# R: id, ru, sr, meal, time, kcal/serv, emoji, equipment(any-of groups: list of lists), ings {id: qty per serving}
def R(id, ru, sr, meal, time, kcal, emoji, equip, ings, family=False):
    return {"id": id, "ru": ru, "sr": sr, "meal": meal, "time": time, "kcal": kcal,
            "emoji": emoji, "equip": equip, "ings": ings, "family": family}

RECIPES = [
    # ---------- BREAKFAST ----------
    R("oatmeal_banana", "Овсянка с бананом", "Ovsena kaša sa bananom", "breakfast", 10, 340, "🥣",
      [["stove", "micro", "multi"]], {"oats": 60, "milk": 150, "banana": 80, "sugar": 5}),
    R("oatmeal_apple", "Овсянка с яблоком и изюмом", "Ovsena kaša sa jabukom", "breakfast", 10, 330, "🍎",
      [["stove", "micro", "multi"]], {"oats": 60, "milk": 150, "apple": 80, "raisins": 10}),
    R("syrniki", "Сырники со сметаной", "Palačinke od sira sa pavlakom", "breakfast", 20, 380, "🥞",
      [["stove"]], {"cottage": 100, "eggs": 0.5, "flour": 20, "sugar": 10, "sour_cream": 30, "oil": 8}),
    R("scrambled_veg", "Яичница с овощами", "Kajgana sa povrćem", "breakfast", 15, 320, "🍳",
      [["stove"]], {"eggs": 2, "tomato": 60, "pepper": 40, "oil": 7, "bread": 40}),
    R("omelet_cheese", "Омлет с сыром", "Omlet sa sirom", "breakfast", 12, 360, "🧀",
      [["stove", "micro"]], {"eggs": 2, "milk": 40, "cheese": 25, "oil": 7, "bread": 40}),
    R("pancakes", "Блины с сахаром", "Palačinke", "breakfast", 25, 400, "🥞",
      [["stove"]], {"flour": 60, "milk": 120, "eggs": 0.5, "sugar": 15, "oil": 8}),
    R("semolina", "Манная каша", "Griz na mleku", "breakfast", 10, 300, "🥣",
      [["stove", "micro"]], {"semolina": 50, "milk": 200, "sugar": 10, "butter": 5}),
    R("toast_tuna", "Тост с тунцом и огурцом", "Tost sa tunjevinom", "breakfast", 10, 330, "🥪",
      [[]], {"bread": 60, "tuna": 40, "cucumber": 30, "sour_cream": 15}),
    R("toast_cheese", "Горячий тост с сыром", "Topli sendvič sa sirom", "breakfast", 10, 350, "🥪",
      [["stove", "oven", "airfryer", "micro"]], {"bread": 60, "cheese": 30, "butter": 8, "tomato": 40}),
    R("yogurt_bowl", "Йогурт с бананом и орехами", "Jogurt sa bananom i orasima", "breakfast", 5, 310, "🥛",
      [[]], {"yogurt": 200, "banana": 80, "walnuts": 15, "oats": 20}),
    R("cottage_bowl", "Творог со сметаной и яблоком", "Mladi sir sa pavlakom", "breakfast", 5, 300, "🍶",
      [[]], {"cottage": 120, "sour_cream": 30, "apple": 70, "sugar": 8}),
    R("smoothie", "Смузи банан-овсянка", "Smuti banana-ovas", "breakfast", 7, 290, "🥤",
      [["blender"]], {"banana": 100, "milk": 180, "oats": 30}),
    R("proja", "Проя с белым сыром", "Proja sa sirom", "breakfast", 35, 370, "🧁",
      [["oven"]], {"flour": 50, "eggs": 0.5, "yogurt": 60, "feta": 30, "oil": 10}, family=True),
    R("egg_toast_avocado", "Яйцо-пашот на тосте", "Poširano jaje na tostu", "breakfast", 12, 310, "🍞",
      [["stove"]], {"eggs": 1.5, "bread": 50, "butter": 6, "greens": 4}),
    R("fr_toast", "Гренки в яйце", "Prženice", "breakfast", 15, 360, "🍞",
      [["stove"]], {"bread": 70, "eggs": 1, "milk": 50, "oil": 8, "sugar": 8}),
    R("mushroom_omelet", "Омлет с шампиньонами", "Omlet sa šampinjonima", "breakfast", 15, 330, "🍄",
      [["stove"]], {"eggs": 2, "mushrooms": 50, "oil": 8, "bread": 40}),

    # ---------- LUNCH ----------
    R("chicken_soup", "Куриный суп с вермишелью", "Pileća supa sa rezancima", "lunch", 40, 320, "🍜",
      [["stove", "multi"]], {"chicken_legs": 100, "potato": 80, "carrot": 40, "onion": 30, "pasta": 25, "greens": 4}, family=True),
    R("borsch", "Борщ со сметаной", "Boršč sa pavlakom", "lunch", 50, 350, "🍲",
      [["stove", "multi"]], {"chicken_legs": 90, "cabbage": 100, "potato": 80, "carrot": 40, "onion": 30, "tomato_paste": 15, "sour_cream": 25}, family=True),
    R("pasulj", "Пасуль (фасолевый суп)", "Pasulj", "lunch", 60, 420, "🫘",
      [["stove", "multi"]], {"beans": 70, "onion": 40, "carrot": 40, "tomato_paste": 12, "oil": 8}, family=True),
    R("lentil_soup", "Чечевичный суп", "Čorba od sočiva", "lunch", 35, 360, "🥣",
      [["stove", "multi"]], {"lentils": 70, "carrot": 40, "onion": 30, "tomato_paste": 10, "oil": 7}, family=True),
    R("chicken_rice", "Курица с рисом и овощами", "Piletina sa pirinčem", "lunch", 35, 480, "🍛",
      [["stove", "multi"]], {"chicken": 120, "rice": 70, "frozen_veg": 80, "oil": 8}),
    R("chicken_buckwheat", "Куриные котлеты с гречкой", "Pileće ćufte sa heljdom", "lunch", 40, 460, "🍘",
      [["stove"]], {"chicken": 110, "eggs": 0.3, "buckwheat": 70, "onion": 20, "oil": 10}),
    R("pasta_bolognese", "Паста болоньезе", "Pasta bolonjeze", "lunch", 35, 520, "🍝",
      [["stove"]], {"pasta": 80, "mince_mix": 90, "passata": 80, "onion": 30, "oil": 7}),
    R("pasta_tuna", "Макароны с тунцом", "Testenina sa tunjevinom", "lunch", 20, 470, "🍝",
      [["stove"]], {"pasta": 80, "tuna": 50, "passata": 60, "garlic": 4, "oil": 6}),
    R("hake_potato", "Хек с картофельным пюре", "Oslić sa pire krompirom", "lunch", 40, 430, "🐟",
      [["stove"], ["oven", "airfryer"]], {"hake": 120, "potato": 200, "milk": 40, "butter": 8, "lemon": 15, "oil": 7}),
    R("djuvec", "Джувеч с курицей", "Pileći đuveč", "lunch", 50, 470, "🥘",
      [["oven", "stove", "multi"]], {"chicken_legs": 120, "rice": 60, "pepper": 60, "tomato": 60, "onion": 30, "oil": 8}, family=True),
    R("stuffed_pepper", "Перцы с фаршем и рисом", "Punjene paprike", "lunch", 60, 450, "🫑",
      [["stove", "oven", "multi"]], {"pepper": 150, "mince_mix": 90, "rice": 40, "onion": 25, "passata": 70, "sour_cream": 20}, family=True),
    R("musaka", "Мусака из картофеля", "Musaka od krompira", "lunch", 60, 490, "🥧",
      [["oven"]], {"potato": 200, "mince_mix": 100, "onion": 30, "eggs": 0.5, "milk": 50, "oil": 8}, family=True),
    R("rice_liver", "Печень с рисом по-домашнему", "Džigerica sa pirinčem", "lunch", 30, 420, "🍚",
      [["stove"]], {"liver": 120, "rice": 70, "onion": 40, "carrot": 30, "oil": 8}),
    R("chick_stew", "Нутовое рагу с овощами", "Varivo od leblebije", "lunch", 30, 400, "🍲",
      [["stove", "multi"]], {"chickpeas": 100, "zucchini": 80, "tomato": 70, "onion": 30, "oil": 8}),
    R("turkey_veg", "Индейка с тушёными овощами", "Ćuretina sa povrćem", "lunch", 35, 420, "🦃",
      [["stove", "airfryer"]], {"turkey": 110, "zucchini": 80, "pepper": 60, "carrot": 30, "oil": 8}),
    R("potato_mush_stew", "Картошка с грибами", "Krompir sa šampinjonima", "lunch", 35, 390, "🍄",
      [["stove", "multi"]], {"potato": 220, "mushrooms": 80, "onion": 30, "sour_cream": 30, "oil": 8}),
    R("pork_stew", "Гуляш из свинины с пюре", "Svinjski gulaš sa pireom", "lunch", 55, 520, "🍖",
      [["stove", "multi"]], {"pork": 110, "potato": 180, "onion": 35, "tomato_paste": 12, "milk": 30, "butter": 6}, family=True),
    R("spinach_rice", "Рис со шпинатом и яйцом", "Pirinač sa spanaćem", "lunch", 25, 380, "🥬",
      [["stove"]], {"rice": 70, "spinach": 90, "eggs": 1, "onion": 20, "oil": 8}),

    # ---------- DINNER ----------
    R("cutlets_mash", "Котлеты с пюре", "Ćufte sa pire krompirom", "dinner", 45, 480, "🍽️",
      [["stove"]], {"mince_mix": 100, "bread": 15, "eggs": 0.3, "potato": 180, "milk": 30, "butter": 6, "oil": 8}, family=True),
    R("chicken_bake", "Куриные бёдра с картошкой в духовке", "Batak sa krompirom iz rerne", "dinner", 50, 520, "🍗",
      [["oven", "airfryer"]], {"chicken_legs": 150, "potato": 180, "oil": 8, "garlic": 4}, family=True),
    R("fish_cutlets", "Рыбные котлеты с пюре", "Riblje pljeskavice sa pireom", "dinner", 45, 440, "🐟",
      [["stove"]], {"hake": 110, "eggs": 0.3, "bread": 15, "potato": 170, "milk": 30, "oil": 9}),
    R("buck_mushroom", "Гречка с грибами и луком", "Heljda sa šampinjonima", "dinner", 30, 380, "🍄",
      [["stove", "multi"]], {"buckwheat": 70, "mushrooms": 70, "onion": 30, "oil": 8}),
    R("sarma_lazy", "Ленивые голубцы", "Lenje sarmice", "dinner", 50, 440, "🥬",
      [["stove", "oven", "multi"]], {"mince_mix": 90, "cabbage": 120, "rice": 35, "onion": 25, "passata": 70, "sour_cream": 20}, family=True),
    R("tortilla_chicken", "Тортилья с курицей и овощами", "Tortilja sa piletinom", "dinner", 25, 460, "🌯",
      [["stove", "grillpan"]], {"tortilla": 62, "chicken": 90, "tomato": 50, "cucumber": 40, "sour_cream": 20, "cheese": 15}),
    R("pilav", "Плов с курицей", "Pilav sa piletinom", "dinner", 45, 490, "🍚",
      [["stove", "multi"]], {"rice": 75, "chicken_legs": 110, "carrot": 50, "onion": 35, "oil": 10, "garlic": 4}, family=True),
    R("veg_stew_dinner", "Овощное рагу с курицей", "Povrtno varivo sa piletinom", "dinner", 40, 410, "🥘",
      [["stove", "multi"]], {"chicken": 90, "zucchini": 90, "potato": 100, "carrot": 40, "onion": 25, "oil": 8}, family=True),
    R("mac_cheese", "Макароны с сыром", "Makarone sa sirom", "dinner", 20, 470, "🧀",
      [["stove"]], {"pasta": 85, "cheese": 35, "butter": 10, "milk": 40}),
    R("baked_fish_veg", "Хек с овощами в духовке", "Oslić sa povrćem iz rerne", "dinner", 40, 400, "🐟",
      [["oven", "airfryer"]], {"hake": 120, "zucchini": 70, "pepper": 60, "potato": 100, "oil": 9, "lemon": 15}),
    R("beans_sausage_free", "Тушёная фасоль с овощами", "Prebranac", "dinner", 55, 430, "🫘",
      [["oven", "stove", "multi"]], {"beans": 80, "onion": 50, "carrot": 30, "oil": 10, "tomato_paste": 10}, family=True),
    R("zapekanka", "Творожная запеканка", "Zapečeni mladi sir", "dinner", 50, 380, "🍮",
      [["oven", "multi"]], {"cottage": 130, "eggs": 0.7, "semolina": 25, "sugar": 15, "sour_cream": 25, "raisins": 10}, family=True),
    R("potato_pancakes", "Драники со сметаной", "Palačinke od krompira", "dinner", 35, 420, "🥔",
      [["stove"]], {"potato": 220, "eggs": 0.5, "flour": 20, "onion": 20, "oil": 12, "sour_cream": 30}),
    R("tofu_rice", "Тофу с рисом и овощами", "Tofu sa pirinčem", "dinner", 25, 390, "🍱",
      [["stove"]], {"tofu": 90, "rice": 70, "broccoli": 70, "carrot": 30, "oil": 8}),
    R("grill_chicken_salad", "Курица-гриль с салатом", "Grilovana piletina sa salatom", "dinner", 25, 380, "🥗",
      [["grillpan", "stove", "airfryer"]], {"chicken": 120, "tomato": 70, "cucumber": 60, "cabbage": 50, "oil": 8, "lemon": 10}),
    R("egg_fried_rice", "Жареный рис с яйцом и кукурузой", "Prženi pirinač sa jajetom", "dinner", 20, 410, "🍳",
      [["stove"]], {"rice": 75, "eggs": 1, "corn": 50, "carrot": 30, "onion": 20, "oil": 9}),
    R("sardine_potato", "Картофель с сардинами и зеленью", "Krompir sa sardinom", "dinner", 25, 390, "🐟",
      [["stove"]], {"potato": 220, "sardines": 50, "onion": 20, "greens": 5, "oil": 6}),
    R("pita_zeljanica", "Зеляница (пирог со шпинатом)", "Zeljanica", "dinner", 55, 450, "🥧",
      [["oven"]], {"flour": 70, "spinach": 90, "feta": 50, "eggs": 0.5, "yogurt": 40, "oil": 12}, family=True),
]

ING_BY_ID = {i["id"]: i for i in INGREDIENTS}
