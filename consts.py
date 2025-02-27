user_progress = {}
user_remaining_cards = {}
group_tests = {
    "Группа 1. Окружающий мир": "https://forms.yandex.ru/u/67a8ebf3e010db44b81208f0/",
    "Группа 2. Семья": "https://my.mts-link.ru/form-passing/1efe70a6-8aa2-65d0-aa33-04421acbfbde/view",
}

lesson_names = {
    1: "Урок 1. Приветствия и прощания",
    2: "Урок 2. Множественное число существительных",
    3: "Урок 3. Форма обоих чисел существительных",
    4: "Урок 4. Исчисляемые и неисчисляемые  существительные",
    5: "Урок 5. Much и Many",
    6: "Урок 6. A lot of, Little и A little",
    7: "Урок 7. Few и A few",
    8: "Урок 8. Артикли",
    9: "Урок 9. Особые случаи употребления артиклей",
    10: "Урок 10. Оборот There + To be",
    11: "Урок 11. Степени сравнения прилагательных",
    12: "Урок 12. Сравнительные обороты",
    13: "Урок 13. Степени сравнения наречий",
    14: "Урок 14. Present Simple",
    15: "Урок 15. Present Continuous",
    16: "Урок 16. Past Simple",
    17: "Урок 17. Практика по всем временам"
}

word_groups = {
    "Группа 1. Окружающий мир": [
        {"word": "air", "translation": "воздух", "example": "The air is fresh."},
        {"word": "wind", "translation": "ветер", "example": "The wind is strong."},
        {"word": "water", "translation": "вода", "example": "I drink water."},
        {"word": "west", "translation": "запад", "example": "The sun sets in the west."},
        {"word": "east", "translation": "восток", "example": "The sun rises in the east."},
        {"word": "north", "translation": "север", "example": "We live in the north."},
        {"word": "south", "translation": "юг", "example": "It is warm in the south."},
        {"word": "tree", "translation": "дерево", "example": "The tree is tall."},
        {"word": "sea", "translation": "море", "example": "I swim in the sea."},
        {"word": "ocean", "translation": "океан", "example": "The ocean is big."},
        {"word": "rock", "translation": "скала", "example": "The rock is hard."},
        {"word": "plant", "translation": "растение", "example": "The plant is green."},
        {"word": "flower", "translation": "цветок", "example": "This flower is beautiful."},
        {"word": "forest", "translation": "лес", "example": "The forest is quiet."},
        {"word": "person", "translation": "личность", "example": "This person is friendly."},
        {"word": "night", "translation": "ночь", "example": "It is dark at night."},
        {"word": "morning", "translation": "утро", "example": "It is morning now."},
        {"word": "day", "translation": "день", "example": "Today is a good day."},
        {"word": "evening", "translation": "вечер", "example": "It is evening now."},
        {"word": "life", "translation": "жизнь", "example": "Life is beautiful."},
        {"word": "mountain", "translation": "гора", "example": "The mountain is high."},
        {"word": "land", "translation": "земля", "example": "The land is dry."},
        {"word": "house", "translation": "дом", "example": "This is my house."},
        {"word": "fire", "translation": "огонь", "example": "The fire is warm."},
        {"word": "country", "translation": "страна", "example": "Russia is a big country."},
        {"word": "animal", "translation": "животное", "example": "The dog is an animal."},
        {"word": "bird", "translation": "птица", "example": "A bird is flying."},
        {"word": "fish", "translation": "рыба", "example": "The fish is in the water."},
        {"word": "insect", "translation": "насекомое", "example": "An insect is on the leaf."},
        {"word": "city", "translation": "город", "example": "I live in a city."},
        {"word": "world", "translation": "мир", "example": "The world is beautiful."}
    ],
    "Группа 2. Семья": [
        {"word": "boy", "translation": "мальчик", "example": "The boy is playing with a ball."},
        {"word": "girl", "translation": "девочка", "example": "The girl is reading a book."},
        {"word": "mother", "translation": "мама", "example": "The mother is cooking dinner."},
        {"word": "father", "translation": "отец", "example": "The father is working in the office."},
        {"word": "son", "translation": "сын", "example": "The son is playing outside."},
        {"word": "daughter", "translation": "дочь", "example": "The daughter is singing a song."},
        {"word": "baby", "translation": "малыш", "example": "The baby is sleeping in the crib."},
        {"word": "family", "translation": "семья", "example": "My family is very important to me."},
        {"word": "grand mother", "translation": "бабушка", "example": "My grandmother is very kind."},
        {"word": "grand father", "translation": "дедушка", "example": "My grandfather tells great stories."},
        {"word": "children", "translation": "дети", "example": "The children are playing in the park."},
        {"word": "home", "translation": "дом", "example": "We live in a big home."},
        {"word": "love", "translation": "любовь", "example": "They feel love for each other."},
        {"word": "apartment", "translation": "квартира", "example": "We live in a small apartment."},
        {"word": "joy", "translation": "радость", "example": "The joy of Christmas is everywhere."},
        {"word": "nephew", "translation": "племянник", "example": "My nephew is visiting us this weekend."},
        {"word": "aunt", "translation": "тётя", "example": "My aunt makes the best cookies."},
        {"word": "uncle", "translation": "дядя", "example": "My uncle is a doctor."},
        {"word": "cousin", "translation": "двоюродная сестра или брат",
         "example": "I play with my cousin every summer."},
        {"word": "man", "translation": "мужчина", "example": "The man is walking in the park."},
        {"word": "woman", "translation": "женщина", "example": "The woman is shopping in the mall."},
        {"word": "child", "translation": "ребёнок", "example": "The child is playing with toys."},
        {"word": "sister", "translation": "сестра", "example": "My sister is very creative."},
        {"word": "brother", "translation": "брат", "example": "My brother is playing football."},
        {"word": "relatives", "translation": "родственники", "example": "We visit our relatives every year."},
        {"word": "friend", "translation": "друг", "example": "My friend is coming to my party."},
        {"word": "wife", "translation": "жена", "example": "His wife is very kind."},
        {"word": "husband", "translation": "муж", "example": "Her husband is a teacher."},
        {"word": "address", "translation": "адрес", "example": "I wrote down the address on the paper."},
        {"word": "happiness", "translation": "счастье", "example": "Happiness is spending time with loved ones."},
        {"word": "people", "translation": "люди", "example": "People from different countries came to the event."}
    ]
}

lesson_text1 = (
    "Добро пожаловать в Урок 1: Приветствия и прощания!\n\n"
    "Изучите материалы урока, перейдя по ссылке ниже:\n"
    "[Теоритическая часть](https://telegra.ph/Urok-1-Privetstviya-i-proshchaniya-01-09)\n"
    "Практическая часть:\n"
    "    [Тест 1](https://wellemo.com/quiz/take/1efd34da-9fd0-6ac8-92ac-f1947c49ebe7/ru/)\n"
    "[Словарь](https://wooordhunt.ru/)"
)

lesson_text2 = (
    "Добро пожаловать в Урок 2: Образование множественного числа существительных!\n\n"
    "Изучите материалы урока, перейдя по ссылке ниже:\n"
    "[Теоритическая часть](https://telegra.ph/Urok-2-Obrazovanie-mnozhestvennogo-chisla-sushchestvitelnyh-01-16)\n"
    "Практическая часть:\n"
    "    [Тест 1](https://myefe.ru/quizzes/tests-plurals)\n"
    "    [Тест 2](https://englishweb.ru/grammar/plurals-test.html)\n"
    "[Словарь](https://wooordhunt.ru/)"
)

lesson_text3 = (
    "Добро пожаловать в Урок 3: Существительные, имеющие одну форму единственного и множественного числа!\n\n"
    "Изучите материалы урока, перейдя по ссылке ниже:\n"
    "[Теоритическая часть](https://telegra.ph/Urok-3-Sushchestvitelnye-imeyushchie-odnu-formu-edinstvennogo-i-mnozhestvennogo-chisla-02-01)\n"
    "Практическая часть:\n"
    "    [Тест 1](https://englishka.ru/tests/test-mnozhestvennoe-chislo-sushchestvitelnyh-v-anglijskom-yazyke/)\n"
    "[Словарь](https://wooordhunt.ru/)"
)

lesson_text4 = (
    "Добро пожаловать в Урок 4: Исчисляемые и неисчисляемые  существительные!\n\n"
    "Изучите материалы урока, перейдя по ссылке ниже:\n"
    "[Теоритическая часть](https://telegra.ph/Urok-4-Okonchaniya-v-anglijskom-yazyke-02-01)\n"
    "Практическая часть:\n"
    "    [Тест 1](https://englishweb.ru/grammar/count-nouns-test.html)\n"
    "    [Тест 2](https://solncesvet.ru/tests/test-na-temu-ischislyaemye-i-neischislyaemye-sushchestvitelnye-v-angliyskom-yazyke/)\n"
    "[Словарь](https://wooordhunt.ru/)"
)

lesson_text5 = (
    "Добро пожаловать в Урок 5: Much и many в английском языке!\n\n"
    "Изучите материалы урока, перейдя по ссылке ниже:\n"
    "[Теоритическая часть](https://telegra.ph/Urok-6-Much-i-many-v-anglijskom-yazyke-02-03)\n"
    "Практическая часть:\n"
    "    [Тест 1](https://thelang.ru/tests/much-many)\n"
    "    [Тест 2](https://englishka.ru/tests/test-uprazhnenie-na-much-many-few-little/)\n"
    "[Словарь](https://wooordhunt.ru/)"
)

lesson_text6 = (
    "Добро пожаловать в Урок 6: Слова a lot of, little, a little!\n\n"
    "Изучите материалы урока, перейдя по ссылке ниже:\n"
    "[Теоритическая часть](https://telegra.ph/Urok-7-Slova-a-lot-of-little-a-little-02-04)\n"
    "Практическая часть:\n"
    "    [Тест 1](https://myefe.ru/quizzes/tests-few-little-many-much)\n"
    "    [Тест 2](https://test-english.com/grammar-points/a1/much-many-lot-little-few/)\n"
    "[Словарь](https://wooordhunt.ru/)"
)

lesson_text7 = (
    "Добро пожаловать в Урок 7: Слова few, a few!\n\n"
    "Изучите материалы урока, перейдя по ссылке ниже:\n"
    "[Теоритическая часть](https://telegra.ph/Urok-8-Slova-few-a-few-02-04)\n"
    "Практическая часть:\n"
    "    [Тест 1](https://myefe.ru/quizzes/tests-few-little-many-much/test-1)\n"
    "    [Тест 2](https://www.native-english.ru/tests/little-a-little-few-a-few)\n"
    "[Словарь](https://wooordhunt.ru/)"
)

lesson_text8 = (
    "Добро пожаловать в Урок 8: Артикли в английском языке!\n\n"
    "Изучите материалы урока, перейдя по ссылке ниже:\n"
    "[Теоритическая часть](https://telegra.ph/Urok-9-Artikli-v-anglijskom-yazyke-02-04)\n"
    "Практическая часть:\n"
    "    [Тест 1](https://englishweb.ru/grammar/test/test-articles.html)\n"
    "    [Тест 2](https://englishka.ru/tests/test-na-artikli-v-anglijskom/)\n"
    "[Словарь](https://wooordhunt.ru/)"
)

lesson_text9 = (
    "Добро пожаловать в Урок 9: Специальные случаи употребления артиклей!\n\n"
    "Изучите материалы урока, перейдя по ссылке ниже:\n"
    "[Теоритическая часть](https://telegra.ph/Urok-10-Specialnye-sluchai-upotrebleniya-artiklej-02-05)\n"
    "Практическая часть:\n"
    "    [Тест 1](https://engblog.ru/test-articles-1)\n"
    "    [Тест 2](https://www.native-english.ru/tests/articles)\n"
    "[Словарь](https://wooordhunt.ru/)"
)

lesson_text10 = (
    "Добро пожаловать в Урок 10: Оборот There + to be!\n\n"
    "Изучите материалы урока, перейдя по ссылке ниже:\n"
    "[Теоритическая часть](https://telegra.ph/Urok-11-Oborot-There--to-be-02-06)\n"
    "Практическая часть:\n"
    "    [Тест 1](https://onlinetestpad.com/ru/test/308614-there-to-be)\n"
    "    [Тест 2](https://upupenglish.ru/there-is-are-exercises/)\n"
    "[Словарь](https://wooordhunt.ru/)"
)

lesson_text11 = (
    "Добро пожаловать в Урок 11: Степени сравнения прилагательных!\n\n"
    "Изучите материалы урока, перейдя по ссылке ниже:\n"
    "[Теоритическая часть](https://telegra.ph/Urok-12-Stepeni-sravneniya-prilagatelnyh-02-07)\n"
    "Практическая часть:\n"
    "    [Тест 1](https://englishweb.ru/grammar/comparatives-test.html)\n"
    "    [Тест 2](https://englishka.ru/tests/test-na-stepeni-sravneniya-v-anglijskom/)\n"
    "[Словарь](https://wooordhunt.ru/)"
)

lesson_text12 = (
    "Добро пожаловать в Урок 12: Сравнительные обороты!\n\n"
    "Изучите материалы урока, перейдя по ссылке ниже:\n"
    "[Теоритическая часть](https://telegra.ph/Urok-13-Sravnitelnye-oboroty-02-07)\n"
    "Практическая часть:\n"
    "    [Тест 1](https://engblog.ru/test-degrees-of-comparison)\n"
    "    [Тест 2](https://www.native-english.ru/tests/degrees-of-comparison)\n"
    "[Словарь](https://wooordhunt.ru/)"
)

lesson_text13 = (
    "Добро пожаловать в Урок 13: Степени сравнения наречий!\n\n"
    "Изучите материалы урока, перейдя по ссылке ниже:\n"
    "[Теоритическая часть](https://telegra.ph/Urok-14-Stepeni-sravneniya-narechij-02-07)\n"
    "Практическая часть:\n"
    "    [Тест 1](https://englika.ru/tests/test-na-stepeni-sravnenija-narechij-v-anglijskom-jazyke)\n"
    "    [Тест 2](https://skyeng.ru/exercises/adverbs-degrees-of-comparison/)\n"
    "[Словарь](https://wooordhunt.ru/)"
)

lesson_text14 = (
    "Добро пожаловать в Урок 14: Простое настоящее время. Present Simple!\n\n"
    "Изучите материалы урока, перейдя по ссылке ниже:\n"
    "[Теоритическая часть](https://telegra.ph/Urok-15-Prostoe-nastoyashchee-vremya-Present-Simple-02-07)\n"
    "Практическая часть:\n"
    "    [Тест 1](https://myefe.ru/quizzes/tests-present-simple)\n"
    "    [Тест 2](https://englishweb.ru/grammar/test/test-present-simple-beginner.html)\n"
    "    [Тест 3](https://englishka.ru/tests/test-na-present-simple/)\n"
    "    [Тест 4](https://skyeng.ru/testy-po-anglijskomu-yazyku/present-simple/)\n"
    "    [Тест 5](https://ru.stegmax.com/tests/present-simple-placement-test-elementary/)\n"
    "[Словарь](https://wooordhunt.ru/)"
)

lesson_text15 = (
    "Добро пожаловать в Урок 15: Настоящее длительное время. Present Continuous!\n\n"
    "Изучите материалы урока, перейдя по ссылке ниже:\n"
    "[Теоритическая часть](https://telegra.ph/Urok-16-Nastoyashchee-dlitelnoe-vremya-Present-Continuous-02-07)\n"
    "Практическая часть:\n"
    "    [Тест 1](https://myefe.ru/?s=Present%20Continuous&msui_c=quiz)\n"
    "    [Тест 2](https://englishweb.ru/grammar/test/test-present-continuous.html)\n"
    "    [Тест 3](https://puzzle-english.com/level-test/present-continuous)\n"
    "    [Тест 4](https://ru.stegmax.com/tests/present-continuous-placement-test-elementary/)\n"
    "    [Тест 5](https://www.memorysecrets.ru/english/en-tests/test-po-anglijskomu-yazyku-present-continuous.html)\n"
    "[Словарь](https://wooordhunt.ru/)"
)

lesson_text16 = (
    "Добро пожаловать в Урок 16: Простое прошедшее время. Past Simple!\n\n"
    "Изучите материалы урока, перейдя по ссылке ниже:\n"
    "[Теоритическая часть](https://telegra.ph/Urok-17-02-08)\n"
    "Практическая часть:\n"
    "    [Тест 1](https://myefe.ru/quizzes/tests-past-simple)\n"
    "    [Тест 2](https://skyeng.ru/exercises/ed/)\n"
    "    [Тест 3](https://ru.stegmax.com/tests/past-simple-placement-test-elementary/)\n"
    "    [Тест 4](https://puzzle-english.com/level-test/past-simple-test)\n"
    "    [Тест 5](https://englishweb.ru/grammar/test/test-past-simple.html)\n"
    "    [Тест 6](https://lim-english.com/tests/test-na-past-simple/)\n"
    "[Словарь](https://wooordhunt.ru/)"
)

lesson_text17 = (
    "Добро пожаловать в Урок 17: Практика по пройденным временам!\n\n"
    "Практическая часть:\n"
    "    [Тест 1](https://wordwall.net/resource/13706334/present-simple-present-continuous-past-simple)\n"
    "    [Тест 2](https://skyeng.ru/exercises/present-simple-present-continuous-past-simple/)\n"
    "    [Тест 3](https://testedu.ru/test/english-language/7-klass/present-simplepresent-continuouspast-simplepast-continuous.html)\n"
    "[Словарь](https://wooordhunt.ru/)"
)
