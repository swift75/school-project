user_progress = {}
user_remaining_cards = {}
group_tests = {
    "Группа 1. Окружающий мир": "https://forms.yandex.ru/u/67a8ebf3e010db44b81208f0/",
    "Группа 2. Семья": "https://my.mts-link.ru/form-passing/1e70a6-65d0-aa33-04421acbbde/view",
    "Группа 3. Туризм": "https://my.mts-link.ru/form-passing/1ee70a6-8aa2-65d0-aa33-04421abfbde/view",
    "Группа 4. Внешность": "https://my.mts-link.ru/form-passing/1efe70a6-8aa2-3-04421acde/view",
    "Группа 5. Школа": "https://my.mts-link.ru/form-passing/1efe70a6-8a2-aa33-04421abde/view",
    "Группа 6. Еда": "https://my.mts-link.ru/form-passing/1a6-8aa2-65d0-aa33-04421acbde/view",
    "Группа 7. Одежда": "https://my.mts-link.ru/form-passing/1efe6-2-65d0-aa-04421de/view",
    "Группа 8. Характер": "https://my.mts-link.ru/form-passing/1ef-8aa2-65d0-aa33-04421acbde/view",
    "Группа 9. Профессии": "https://my.mts-link.ru/form-passing/1efe78aa2-65d0-aa33-04421bfbde/view",
    "Группа 10. Спорт": "https://my.mts-link.ru/form-passing/1efe70-8aa2-d0-aa33-04421cbfbd/view",

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
        {"word": "air", "translation": "воздух", "translation2": "Воздух свежий.", "example": "The air is fresh."},
        {"word": "wind", "translation": "ветер", "translation2": "Ветер сильный.", "example": "The wind is strong."},
        {"word": "water", "translation": "вода", "translation2": "Я пью воду.", "example": "I drink water."},
        {"word": "west", "translation": "запад", "translation2": "Солнце садится на западе.",
         "example": "The sun sets in the west."},
        {"word": "east", "translation": "восток", "translation2": "Солнце встаёт на востоке.",
         "example": "The sun rises in the east."},
        {"word": "north", "translation": "север", "translation2": "Мы живём на севере.",
         "example": "We live in the north."},
        {"word": "south", "translation": "юг", "translation2": "На юге тепло.", "example": "It is warm in the south."},
        {"word": "tree", "translation": "дерево", "translation2": "Дерево высокое.", "example": "The tree is tall."},
        {"word": "sea", "translation": "море", "translation2": "Я плаваю в море.", "example": "I swim in the sea."},
        {"word": "ocean", "translation": "океан", "translation2": "Океан большой.", "example": "The ocean is big."},
        {"word": "rock", "translation": "скала", "translation2": "Скала твёрдая.", "example": "The rock is hard."},
        {"word": "plant", "translation": "растение", "translation2": "Растение зелёное.",
         "example": "The plant is green."},
        {"word": "flower", "translation": "цветок", "translation2": "Этот цветок красивый.",
         "example": "This flower is beautiful."},
        {"word": "forest", "translation": "лес", "translation2": "Лес тихий.", "example": "The forest is quiet."},
        {"word": "person", "translation": "личность", "translation2": "Этот человек дружелюбный.",
         "example": "This person is friendly."},
        {"word": "night", "translation": "ночь", "translation2": "Ночью темно.", "example": "It is dark at night."},
        {"word": "morning", "translation": "утро", "translation2": "Сейчас утро.", "example": "It is morning now."},
        {"word": "day", "translation": "день", "translation2": "Сегодня хороший день.",
         "example": "Today is a good day."},
        {"word": "evening", "translation": "вечер", "translation2": "Сейчас вечер.", "example": "It is evening now."},
        {"word": "life", "translation": "жизнь", "translation2": "Жизнь прекрасна.", "example": "Life is beautiful."},
        {"word": "mountain", "translation": "гора", "translation2": "Гора высокая.",
         "example": "The mountain is high."},
        {"word": "land", "translation": "земля", "translation2": "Земля сухая.", "example": "The land is dry."},
        {"word": "house", "translation": "дом", "translation2": "Это мой дом.", "example": "This is my house."},
        {"word": "fire", "translation": "огонь", "translation2": "Огонь тёплый.", "example": "The fire is warm."},
        {"word": "country", "translation": "страна", "translation2": "Россия - большая страна.",
         "example": "Russia is a big country."},
        {"word": "animal", "translation": "животное", "translation2": "Собака - это животное.",
         "example": "The dog is an animal."},
        {"word": "bird", "translation": "птица", "translation2": "Птица летит.", "example": "A bird is flying."},
        {"word": "fish", "translation": "рыба", "translation2": "Рыба в воде.", "example": "The fish is in the water."},
        {"word": "insect", "translation": "насекомое", "translation2": "На листе сидит насекомое.",
         "example": "An insect is on the leaf."},
        {"word": "city", "translation": "город", "translation2": "Я живу в городе.", "example": "I live in a city."},
        {"word": "world", "translation": "мир", "translation2": "Мир прекрасен.", "example": "The world is beautiful."}
    ],
    "Группа 2. Семья": [
        {"word": "boy", "translation": "мальчик", "translation2": "Мальчик играет с мячом.",
         "example": "The boy is playing with a ball."},
        {"word": "girl", "translation": "девочка", "translation2": "Девочка читает книгу.",
         "example": "The girl is reading a book."},
        {"word": "mother", "translation": "мама", "translation2": "Мама готовит ужин.",
         "example": "The mother is cooking dinner."},
        {"word": "father", "translation": "отец", "translation2": "Отец работает в офисе.",
         "example": "The father is working in the office."},
        {"word": "son", "translation": "сын", "translation2": "Сын играет на улице.",
         "example": "The son is playing outside."},
        {"word": "daughter", "translation": "дочь", "translation2": "Дочь поёт песню.",
         "example": "The daughter is singing a song."},
        {"word": "baby", "translation": "малыш", "translation2": "Малыш спит в кроватке.",
         "example": "The baby is sleeping in the crib."},
        {"word": "family", "translation": "семья", "translation2": "Моя семья очень важна для меня.",
         "example": "My family is very important to me."},
        {"word": "grand mother", "translation": "бабушка", "translation2": "Моя бабушка очень добрая.",
         "example": "My grandmother is very kind."},
        {"word": "grand father", "translation": "дедушка",
         "translation2": "Мой дедушка рассказывает замечательные истории.",
         "example": "My grandfather tells great stories."},
        {"word": "children", "translation": "дети", "translation2": "Дети играют в парке.",
         "example": "The children are playing in the park."},
        {"word": "home", "translation": "дом", "translation2": "Мы живём в большом доме.",
         "example": "We live in a big home."},
        {"word": "love", "translation": "любовь", "translation2": "Они испытывают любовь друг к другу.",
         "example": "They feel love for each other."},
        {"word": "apartment", "translation": "квартира", "translation2": "Мы живём в маленькой квартире.",
         "example": "We live in a small apartment."},
        {"word": "joy", "translation": "радость", "translation2": "Радость Рождества повсюду.",
         "example": "The joy of Christmas is everywhere."},
        {"word": "nephew", "translation": "племянник", "translation2": "Мой племянник приезжает к нам на выходные.",
         "example": "My nephew is visiting us this weekend."},
        {"word": "aunt", "translation": "тётя", "translation2": "Моя тётя делает лучшие печенья.",
         "example": "My aunt makes the best cookies."},
        {"word": "uncle", "translation": "дядя", "translation2": "Мой дядя - врач.",
         "example": "My uncle is a doctor."},
        {"word": "cousin", "translation": "двоюродная сестра или брат",
         "translation2": "Я играю с моим кузеном каждое лето.", "example": "I play with my cousin every summer."},
        {"word": "man", "translation": "мужчина", "translation2": "Мужчина гуляет в парке.",
         "example": "The man is walking in the park."},
        {"word": "woman", "translation": "женщина", "translation2": "Женщина делает покупки в торговом центре.",
         "example": "The woman is shopping in the mall."},
        {"word": "child", "translation": "ребёнок", "translation2": "Ребёнок играет с игрушками.",
         "example": "The child is playing with toys."},
        {"word": "sister", "translation": "сестра", "translation2": "Моя сестра очень креативная.",
         "example": "My sister is very creative."},
        {"word": "brother", "translation": "брат", "translation2": "Мой брат играет в футбол.",
         "example": "My brother is playing football."},
        {"word": "relatives", "translation": "родственники",
         "translation2": "Мы навещаем наших родственников каждый год.",
         "example": "We visit our relatives every year."},
        {"word": "friend", "translation": "друг", "translation2": "Мой друг придёт на мою вечеринку.",
         "example": "My friend is coming to my party."},
        {"word": "wife", "translation": "жена", "translation2": "Его жена очень добрая.",
         "example": "His wife is very kind."},
        {"word": "husband", "translation": "муж", "translation2": "Её муж - учитель.",
         "example": "Her husband is a teacher."},
        {"word": "address", "translation": "адрес", "translation2": "Я записал адрес на бумаге.",
         "example": "I wrote down the address on the paper."},
        {"word": "happiness", "translation": "счастье", "translation2": "Счастье — это проводить время с близкими.",
         "example": "Happiness is spending time with loved ones."},
        {"word": "people", "translation": "люди", "translation2": "Люди из разных стран приехали на мероприятие.",
         "example": "People from different countries came to the event."}
    ],
    "Группа 3. Туризм": [
        {"word": "road", "translation": "дорога", "translation2": "Дорога длинная.", "example": "The road is long."},
        {"word": "ticket", "translation": "билет", "translation2": "У меня есть билет на поезд.",
         "example": "I have a train ticket."},
        {"word": "map", "translation": "карта", "translation2": "Она смотрит на карту.",
         "example": "She is looking at the map."},
        {"word": "motel", "translation": "мотель", "translation2": "Мы остановились в маленьком мотеле.",
         "example": "We stayed at a small motel."},
        {"word": "highway", "translation": "шоссе", "translation2": "Шоссе загружено.",
         "example": "The highway is busy."},
        {"word": "reception", "translation": "ресепшн", "translation2": "Обратитесь на ресепшн за помощью.",
         "example": "Go to the reception for help."},
        {"word": "wallet", "translation": "бумажник", "translation2": "Мой бумажник в сумке.",
         "example": "My wallet is in my bag."},
        {"word": "bank", "translation": "банк", "translation2": "Он работает в банке.",
         "example": "He works at a bank."},
        {"word": "subway", "translation": "метро", "translation2": "Метро быстрое.", "example": "The subway is fast."},
        {"word": "cab", "translation": "такси", "translation2": "Мы поехали домой на такси.",
         "example": "We took a cab home."},
        {"word": "parking", "translation": "парковка", "translation2": "Парковка заполнена.",
         "example": "The parking is full."},
        {"word": "food order", "translation": "заказ еды", "translation2": "Мой заказ еды готов.",
         "example": "My food order is ready."},
        {"word": "cash", "translation": "наличные", "translation2": "Я заплатил наличными.",
         "example": "I paid with cash."},
        {"word": "passport", "translation": "паспорт", "translation2": "Покажите паспорт в аэропорту.",
         "example": "Show your passport at the airport."},
        {"word": "permission", "translation": "разрешение", "translation2": "Мне нужно разрешение, чтобы уйти.",
         "example": "I need permission to go."},
        {"word": "lawyer", "translation": "адвокат", "translation2": "Этот адвокат очень умный.",
         "example": "The lawyer is very smart."},
        {"word": "problem", "translation": "проблема", "translation2": "У нас небольшая проблема.",
         "example": "We have a small problem."},
        {"word": "waiting room", "translation": "зал ожидания", "translation2": "Сядьте в зале ожидания.",
         "example": "Sit in the waiting room."},
        {"word": "transfer", "translation": "пересадка", "translation2": "У нас пересадка в Париже.",
         "example": "We have a transfer in Paris."},
        {"word": "bag", "translation": "сумка", "translation2": "Её сумка тяжёлая.", "example": "Her bag is heavy."},
        {"word": "suitcase", "translation": "чемодан", "translation2": "Мой чемодан синий.",
         "example": "My suitcase is blue."},
        {"word": "property", "translation": "имущество", "translation2": "Это частное имущество.",
         "example": "This is private property."},
        {"word": "law", "translation": "закон", "translation2": "Закон важен.", "example": "The law is important."},
        {"word": "police station", "translation": "полицейский участок",
         "translation2": "Он пошёл в полицейский участок.", "example": "He went to the police station."},
        {"word": "price", "translation": "цена", "translation2": "Цена слишком высокая.",
         "example": "The price is too high."},
        {"word": "price list", "translation": "ценник", "translation2": "Проверьте ценник.",
         "example": "Check the price list."},
        {"word": "courier", "translation": "курьер", "translation2": "Курьер доставил мой пакет.",
         "example": "The courier delivered my package."},
        {"word": "delivery", "translation": "доставка", "translation2": "Доставка опаздывает.",
         "example": "The delivery is late."},
        {"word": "location", "translation": "местоположение", "translation2": "Местоположение идеальное.",
         "example": "The location is perfect."},
        {"word": "route", "translation": "маршрут", "translation2": "Это лучший маршрут.",
         "example": "This is the best route."},
        {"word": "agreement", "translation": "договор", "translation2": "Мы подписали договор.",
         "example": "We signed the agreement."},
        {"word": "hospital", "translation": "больница", "translation2": "Он в больнице.",
         "example": "He is in the hospital."},
        {"word": "ambulance", "translation": "скорая помощь", "translation2": "Вызовите скорую помощь!",
         "example": "Call an ambulance!"}
    ],
    "Группа 4. Внешность": [
        {"word": "appearance", "translation": "внешность", "example": "She has a beautiful appearance.",
         "translation2": "У неё красивая внешность."},
        {"word": "height", "translation": "рост", "example": "His height is 180 cm.",
         "translation2": "Его рост – 180 см."},
        {"word": "tall", "translation": "высокий", "example": "He is very tall.", "translation2": "Он очень высокий."},
        {"word": "short", "translation": "низкий", "example": "She is quite short.",
         "translation2": "Она довольно низкая."},
        {"word": "middle-sized", "translation": "среднего роста", "example": "He is middle-sized.",
         "translation2": "Он среднего роста."},
        {"word": "build", "translation": "телосложение", "example": "She has a slim build.",
         "translation2": "У неё стройное телосложение."},
        {"word": "thin", "translation": "худой", "example": "He is very thin.", "translation2": "Он очень худой."},
        {"word": "fat", "translation": "толстый", "example": "The cat is fat.", "translation2": "Кот толстый."},
        {"word": "slim", "translation": "стройный (о девушке)", "example": "She is slim and beautiful.",
         "translation2": "Она стройная и красивая."},
        {"word": "athletic", "translation": "мускулистый (спортивный)", "example": "He has an athletic body.",
         "translation2": "У него мускулистое тело."},
        {"word": "hair colour", "translation": "цвет волос", "example": "Her hair colour is blond.",
         "translation2": "Цвет её волос – блонд."},
        {"word": "fair", "translation": "светлые", "example": "She has fair hair.",
         "translation2": "У неё светлые волосы."},
        {"word": "dark", "translation": "темные", "example": "He has dark hair.",
         "translation2": "У него тёмные волосы."},
        {"word": "black", "translation": "черные", "example": "Her hair is black.",
         "translation2": "Её волосы чёрные."},
        {"word": "brown", "translation": "коричневые", "example": "He has brown hair.",
         "translation2": "У него коричневые волосы."},
        {"word": "red", "translation": "рыжие", "example": "She has red hair.", "translation2": "У неё рыжие волосы."},
        {"word": "blond", "translation": "очень светлые", "example": "His hair is blond.",
         "translation2": "Его волосы очень светлые."},
        {"word": "hair", "translation": "волосы", "example": "Her hair is long.",
         "translation2": "У неё длинные волосы."},
        {"word": "short", "translation": "короткие", "example": "He has short hair.",
         "translation2": "У него короткие волосы."},
        {"word": "long", "translation": "длинные", "example": "She has long hair.",
         "translation2": "У неё длинные волосы."},
        {"word": "straight", "translation": "прямые", "example": "His hair is straight.",
         "translation2": "У него прямые волосы."},
        {"word": "wavy", "translation": "волнистые", "example": "She has wavy hair.",
         "translation2": "У неё волнистые волосы."},
        {"word": "curly", "translation": "кудрявые", "example": "He has curly hair.",
         "translation2": "У него кудрявые волосы."},
        {"word": "thick", "translation": "густые", "example": "Her hair is thick.",
         "translation2": "У неё густые волосы."},
        {"word": "thin", "translation": "редкие", "example": "His hair is thin.",
         "translation2": "У него редкие волосы."},
        {"word": "eyes", "translation": "глаза", "example": "Her eyes are blue.", "translation2": "Её глаза голубые."},
        {"word": "big", "translation": "большие", "example": "He has big eyes.",
         "translation2": "У него большие глаза."},
        {"word": "little", "translation": "маленькие", "example": "She has little eyes.",
         "translation2": "У неё маленькие глаза."},
        {"word": "green", "translation": "зеленые", "example": "His eyes are green.",
         "translation2": "У него зелёные глаза."},
        {"word": "blue", "translation": "голубые", "example": "She has blue eyes.",
         "translation2": "У неё голубые глаза."},
        {"word": "brown (hazel)", "translation": "карие", "example": "His eyes are brown.",
         "translation2": "У него карие глаза."},
        {"word": "face", "translation": "лицо", "example": "She has a round face.",
         "translation2": "У неё круглое лицо."},
        {"word": "round", "translation": "круглое", "example": "His face is round.",
         "translation2": "У него круглое лицо."},
        {"word": "oval", "translation": "овальное", "example": "She has an oval face.",
         "translation2": "У неё овальное лицо."},
        {"word": "nose", "translation": "нос", "example": "His nose is long.", "translation2": "У него длинный нос."},
        {"word": "long", "translation": "длинный", "example": "She has a long nose.",
         "translation2": "У неё длинный нос."},
        {"word": "straight", "translation": "прямой", "example": "His nose is straight.",
         "translation2": "У него прямой нос."},
        {"word": "turned up", "translation": "вздернутый", "example": "She has a turned-up nose.",
         "translation2": "У неё вздёрнутый нос."},
        {"word": "mouth", "translation": "рот", "example": "His mouth is small.",
         "translation2": "У него маленький рот."},
        {"word": "lips", "translation": "губы", "example": "Her lips are full.", "translation2": "У неё полные губы."},
        {"word": "teeth", "translation": "зубы", "example": "His teeth are white.",
         "translation2": "У него белые зубы."},
        {"word": "ears", "translation": "уши", "example": "She has small ears.",
         "translation2": "У неё маленькие уши."},
        {"word": "forehead", "translation": "лоб", "example": "His forehead is wide.",
         "translation2": "У него широкий лоб."},
        {"word": "neck", "translation": "шея", "example": "She has a long neck.", "translation2": "У неё длинная шея."},
        {"word": "body", "translation": "туловище", "example": "His body is strong.",
         "translation2": "У него крепкое туловище."},
        {"word": "arms", "translation": "руки", "example": "She has long arms.", "translation2": "У неё длинные руки."},
        {"word": "hands", "translation": "руки (кисти рук)", "example": "His hands are big.",
         "translation2": "У него большие кисти рук."},
        {"word": "legs", "translation": "ноги", "example": "She has long legs.", "translation2": "У неё длинные ноги."},
        {"word": "knees", "translation": "колени", "example": "His knees hurt.",
         "translation2": "У него болят колени."},
        {"word": "feet", "translation": "ступни", "example": "Her feet are small.",
         "translation2": "У неё маленькие ступни."}
    ],
    "Группа 5. Школа": [
        {"word": "to do homework", "translation": "делать домашнюю работу",
         "example": "I do my homework every evening.", "translation2": "Я делаю домашнюю работу каждый вечер."},
        {"word": "mark in Maths", "translation": "отметка по математике", "example": "I got a good mark in Maths.",
         "translation2": "Я получил хорошую отметку по математике."},
        {"word": "to get good (bad) marks", "translation": "получать отметки", "example": "She always gets good marks.",
         "translation2": "Она всегда получает хорошие отметки."},
        {"word": "to give marks", "translation": "ставить отметки", "example": "The teacher gives marks for our work.",
         "translation2": "Учитель ставит отметки за нашу работу."},
        {"word": "to make new friends", "translation": "заводить новых друзей",
         "example": "He made new friends at school.", "translation2": "Он завёл новых друзей в школе."},
        {"word": "to have 5 or 6 lessons a day", "translation": "иметь 5 или 6 уроков в день",
         "example": "We have 6 lessons today.", "translation2": "У нас сегодня 6 уроков."},
        {"word": "to learn", "translation": "учить, узнавать", "example": "We learn a lot at school.",
         "translation2": "Мы много узнаем в школе."},
        {"word": "to learn new things", "translation": "узнавать новое", "example": "I love to learn new things.",
         "translation2": "Я люблю узнавать новое."},
        {"word": "to learn by heart", "translation": "учить наизусть", "example": "We learned a poem by heart.",
         "translation2": "Мы выучили стихотворение наизусть."},
        {"word": "to ask questions", "translation": "задавать вопросы", "example": "The students ask many questions.",
         "translation2": "Ученики задают много вопросов."},
        {"word": "to answer questions", "translation": "отвечать на вопросы",
         "example": "She answered all the questions correctly.",
         "translation2": "Она правильно ответила на все вопросы."},
        {"word": "to do sums", "translation": "решать примеры", "example": "We did sums in the Maths lesson.",
         "translation2": "Мы решали примеры на уроке математики."},
        {"word": "to solve problems", "translation": "решать задачи", "example": "He likes to solve problems.",
         "translation2": "Он любит решать задачи."},
        {"word": "to get smarter", "translation": "становиться умнее", "example": "Reading books helps to get smarter.",
         "translation2": "Чтение книг помогает становиться умнее."},
        {"word": "to have fun during breaks", "translation": "веселиться на переменах",
         "example": "We have fun during breaks.", "translation2": "Мы веселимся на переменах."},
        {"word": "to recite poems", "translation": "рассказывать стихи", "example": "She recites poems beautifully.",
         "translation2": "Она красиво рассказывает стихи."},
        {"word": "to enjoy school parties", "translation": "развлекаться на школьных вечеринках",
         "example": "We enjoy school parties a lot.", "translation2": "Мы очень любим школьные вечеринки."},
        {"word": "to study", "translation": "учиться", "example": "He studies hard for exams.",
         "translation2": "Он усердно учится к экзаменам."},
        {"word": "to work hard", "translation": "упорно работать", "example": "She works hard every day.",
         "translation2": "Она усердно работает каждый день."},
        {"word": "to do my best", "translation": "очень стараться", "example": "I always do my best.",
         "translation2": "Я всегда очень стараюсь."},
        {"word": "lesson", "translation": "урок", "example": "The lesson was interesting.",
         "translation2": "Урок был интересным."},
        {"word": "English lesson", "translation": "урок английского языка",
         "example": "We had an English lesson today.", "translation2": "У нас сегодня был урок английского языка."},
        {"word": "English teacher", "translation": "учитель английского языка",
         "example": "Our English teacher is very kind.", "translation2": "Наш учитель английского языка очень добрый."},
        {"word": "strict", "translation": "строгий", "example": "The teacher is strict but fair.",
         "translation2": "Учитель строгий, но справедливый."},
        {"word": "kind", "translation": "добрый", "example": "She is very kind to everyone.",
         "translation2": "Она очень добра ко всем."},
        {"word": "subject", "translation": "предмет", "example": "Maths is my favorite subject.",
         "translation2": "Математика — мой любимый предмет."},
        {"word": "at the lesson", "translation": "на уроке", "example": "We read a new text at the lesson.",
         "translation2": "Мы читали новый текст на уроке."},
        {"word": "at school", "translation": "на занятиях в школе", "example": "I meet my friends at school.",
         "translation2": "Я встречаю друзей на занятиях в школе."},
        {"word": "to be in the … form", "translation": "быть в … классе", "example": "She is in the sixth form.",
         "translation2": "Она в шестом классе."},
        {"word": "(in) the timetable", "translation": "в расписании", "example": "Maths is in the timetable on Monday.",
         "translation2": "Математика есть в расписании на понедельник."},
        {"word": "lunch break", "translation": "большая перемена",
         "example": "We eat in the cafeteria during the lunch break.",
         "translation2": "Мы едим в столовой во время большой перемены."},
        {"word": "to wear a uniform", "translation": "носить форму", "example": "We have to wear a uniform at school.",
         "translation2": "Мы должны носить форму в школе."}
    ],
    "Группа 6. Еда": [
        {"word": "a sandwich", "translation": "бутерброд", "example": "I had a sandwich for breakfast.",
         "translation2": "Я поел бутерброд на завтрак."},
        {"word": "toast", "translation": "поджаренный хлеб", "example": "She likes toast with jam.",
         "translation2": "Ей нравится поджаренный хлеб с вареньем."},
        {"word": "a cake", "translation": "торт, пирожное", "example": "We bought a cake for the party.",
         "translation2": "Мы купили торт для вечеринки."},
        {"word": "a bun", "translation": "булочка", "example": "I will have a bun with my coffee.",
         "translation2": "Я возьму булочку с кофе."},
        {"word": "tea", "translation": "чай", "example": "She drinks tea every morning.",
         "translation2": "Она пьет чай каждое утро."},
        {"word": "coffee", "translation": "кофе", "example": "He prefers coffee to tea.",
         "translation2": "Он предпочитает кофе чаю."},
        {"word": "sugar", "translation": "сахар", "example": "I don't like sugar in my tea.",
         "translation2": "Я не люблю сахар в чае."},
        {"word": "porridge", "translation": "каша", "example": "My mom makes porridge for breakfast.",
         "translation2": "Моя мама готовит кашу на завтрак."},
        {"word": "cheese", "translation": "сыр", "example": "I like cheese on my sandwich.",
         "translation2": "Мне нравится сыр на бутерброде."},
        {"word": "sausage", "translation": "колбаса", "example": "I had sausage with eggs for breakfast.",
         "translation2": "Я поел колбасу с яйцами на завтрак."},
        {"word": "sausages", "translation": "сосиски", "example": "She fried some sausages for lunch.",
         "translation2": "Она пожарила сосиски на обед."},
        {"word": "salt", "translation": "соль", "example": "Don't forget to add salt to the soup.",
         "translation2": "Не забудь добавить соль в суп."},
        {"word": "pepper", "translation": "перец", "example": "I like to add pepper to my salad.",
         "translation2": "Мне нравится добавлять перец в салат."},
        {"word": "salad", "translation": "салат", "example": "We had a vegetable salad for dinner.",
         "translation2": "Мы поели овощной салат на ужин."},
        {"word": "soup", "translation": "суп", "example": "I love chicken soup.",
         "translation2": "Я люблю куриный суп."},
        {"word": "meat", "translation": "мясо", "example": "The meat was tender and delicious.",
         "translation2": "Мясо было мягким и вкусным."},
        {"word": "chicken", "translation": "курица", "example": "She is cooking chicken for dinner.",
         "translation2": "Она готовит курицу на ужин."},
        {"word": "fish", "translation": "рыба", "example": "We had fish for lunch.",
         "translation2": "Мы поели рыбу на обед."},
        {"word": "cutlets", "translation": "котлеты", "example": "I made some cutlets for dinner.",
         "translation2": "Я приготовил котлеты на ужин."},
        {"word": "potatoes", "translation": "картошка", "example": "We had mashed potatoes with meat.",
         "translation2": "Мы поели пюре с мясом."},
        {"word": "tomatoes", "translation": "помидоры", "example": "Tomatoes are my favorite vegetable.",
         "translation2": "Помидоры — мои любимые овощи."},
        {"word": "vegetables", "translation": "овощи", "example": "I prefer fresh vegetables in my salad.",
         "translation2": "Мне нравятся свежие овощи в салате."},
        {"word": "bread", "translation": "хлеб", "example": "I always buy fresh bread.",
         "translation2": "Я всегда покупаю свежий хлеб."},
        {"word": "butter", "translation": "масло", "example": "She spread butter on her toast.",
         "translation2": "Она намазала масло на поджаренный хлеб."},
        {"word": "a drink", "translation": "напиток", "example": "I would like a cold drink.",
         "translation2": "Я бы хотел холодный напиток."},
        {"word": "milk", "translation": "молоко", "example": "He drinks milk every morning.",
         "translation2": "Он пьет молоко каждое утро."},
        {"word": "juice", "translation": "сок", "example": "She likes orange juice.",
         "translation2": "Ей нравится апельсиновый сок."},
        {"word": "coca-cola", "translation": "кока-кола", "example": "I had a Coca-Cola with my lunch.",
         "translation2": "Я выпил кока-колу с обедом."},
        {"word": "mineral water", "translation": "минеральная вода", "example": "He prefers mineral water to soda.",
         "translation2": "Он предпочитает минеральную воду газировке."},
        {"word": "an ice-cream", "translation": "мороженое", "example": "We had ice cream for dessert.",
         "translation2": "Мы поели мороженое на десерт."},
        {"word": "fruit", "translation": "фрукты", "example": "I eat a lot of fruit every day.",
         "translation2": "Я ем много фруктов каждый день."},
        {"word": "to have for breakfast", "translation": "есть на завтрак",
         "example": "I have eggs and toast for breakfast.", "translation2": "Я ем яйца и тосты на завтрак."},
        {"word": "to have light (big) breakfast", "translation": "есть легкий (плотный) завтрак",
         "example": "I usually have a light breakfast.", "translation2": "Обычно я ем легкий завтрак."},
        {"word": "to have no breakfast at all", "translation": "совсем не завтракать",
         "example": "He has no breakfast at all.", "translation2": "Он совсем не завтракает."},
        {"word": "to have for lunch", "translation": "есть на ланч", "example": "I have a sandwich for lunch.",
         "translation2": "Я ем бутерброд на ланч."},
        {"word": "to have for dinner", "translation": "есть на ужин", "example": "We have chicken for dinner.",
         "translation2": "Мы едим курицу на ужин."}
    ],
    "Группа 7. Одежда": [
        {"word": "to wear", "translation": "носить (быть одетым в)", "example": "She wears a dress every day.",
         "translation2": "Она носит платье каждый день."},
        {"word": "to put on", "translation": "надеть (на себя) что-либо",
         "example": "He put on his jacket before going outside.",
         "translation2": "Он надел куртку перед тем, как выйти на улицу."},
        {"word": "to take off", "translation": "снять с себя", "example": "She took off her shoes after work.",
         "translation2": "Она сняла туфли после работы."},
        {"word": "to dress", "translation": "одеться", "example": "I need to dress for the party.",
         "translation2": "Мне нужно одеться для вечеринки."},
        {"word": "to undress", "translation": "раздеться", "example": "He undressed quickly after coming home.",
         "translation2": "Он быстро разделся, когда пришел домой."},
        {"word": "jeans", "translation": "джинсы", "example": "She is wearing jeans today.",
         "translation2": "Сегодня она носит джинсы."},
        {"word": "trousers", "translation": "брюки", "example": "He prefers to wear trousers to work.",
         "translation2": "Он предпочитает носить брюки на работу."},
        {"word": "shorts", "translation": "шорты", "example": "I like wearing shorts in the summer.",
         "translation2": "Мне нравится носить шорты летом."},
        {"word": "dress", "translation": "платье", "example": "She wore a beautiful dress to the party.",
         "translation2": "Она надела красивое платье на вечеринку."},
        {"word": "jacket", "translation": "куртка", "example": "I need a warm jacket for winter.",
         "translation2": "Мне нужна теплая куртка для зимы."},
        {"word": "coat", "translation": "пальто", "example": "He bought a new coat for the cold weather.",
         "translation2": "Он купил новое пальто для холодной погоды."},
        {"word": "T-shirt", "translation": "футболка", "example": "I wear a T-shirt when I go to the gym.",
         "translation2": "Я ношу футболку, когда иду в спортзал."},
        {"word": "shirt", "translation": "рубашка", "example": "He always wears a white shirt to work.",
         "translation2": "Он всегда носит белую рубашку на работу."},
        {"word": "skirt", "translation": "юбка", "example": "She wore a skirt to the office today.",
         "translation2": "Сегодня она надела юбку в офис."},
        {"word": "blouse", "translation": "блузка", "example": "I have a new blouse for the meeting.",
         "translation2": "У меня есть новая блузка для встречи."},
        {"word": "sweater", "translation": "свитер", "example": "It's cold outside, so I'm wearing a sweater.",
         "translation2": "На улице холодно, поэтому я надел свитер."},
        {"word": "cap", "translation": "шапка, кепка", "example": "He wore a cap to protect himself from the sun.",
         "translation2": "Он надел кепку, чтобы защититься от солнца."},
        {"word": "scarf", "translation": "шарф", "example": "She tied a scarf around her neck.",
         "translation2": "Она завязала шарф вокруг шеи."},
        {"word": "shoes", "translation": "туфли", "example": "I bought new shoes for the event.",
         "translation2": "Я купил новые туфли для мероприятия."},
        {"word": "boots", "translation": "ботинки", "example": "These boots are perfect for winter.",
         "translation2": "Эти ботинки идеально подходят для зимы."}
    ],
    "Группа 8. Характер": [
        {"word": "typical", "translation": "типичный", "example": "It’s typical for her to be late.",
         "translation2": "Это типично для неё — опаздывать."},
        {"word": "close", "translation": "близкий", "example": "She is very close to her family.",
         "translation2": "Она очень близка со своей семьей."},
        {"word": "loving", "translation": "любящий", "example": "He is a loving father.",
         "translation2": "Он любящий отец."},
        {"word": "friendly", "translation": "дружелюбный", "example": "The dog is very friendly.",
         "translation2": "Собака очень дружелюбная."},
        {"word": "caring", "translation": "заботливый", "example": "She is a caring person.",
         "translation2": "Она заботливый человек."},
        {"word": "independent", "translation": "независимый", "example": "He is an independent individual.",
         "translation2": "Он независимый человек."},
        {"word": "smart", "translation": "сообразительный, находчивый", "example": "She is a smart student.",
         "translation2": "Она сообразительная студентка."},
        {"word": "clever", "translation": "умный", "example": "He gave a clever answer.",
         "translation2": "Он дал умный ответ."},
        {"word": "serious", "translation": "серьезный", "example": "She had a serious look on her face.",
         "translation2": "У неё было серьезное выражение лица."},
        {"word": "kind", "translation": "добрый", "example": "He is very kind to animals.",
         "translation2": "Он очень добр к животным."},
        {"word": "lazy", "translation": "ленивый", "example": "Don’t be lazy, help your parents.",
         "translation2": "Не будь ленивым, помоги своим родителям."},
        {"word": "busy", "translation": "деловой", "example": "She is always busy with work.",
         "translation2": "Она всегда занята работой."},
        {"word": "bossy", "translation": "любящий командовать", "example": "He is a bit bossy with his friends.",
         "translation2": "Он немного любит командовать своими друзьями."},
        {"word": "naughty", "translation": "непослушный", "example": "The child is being naughty today.",
         "translation2": "Ребёнок сегодня непослушный."},
        {"word": "noisy", "translation": "шумный", "example": "The noisy children disturbed the class.",
         "translation2": "Шумные дети мешали на уроке."},
        {"word": "creative", "translation": "творческий", "example": "She is very creative in her art.",
         "translation2": "Она очень творческая в своём искусстве."},
        {"word": "strong", "translation": "сильный", "example": "He is strong enough to lift that box.",
         "translation2": "Он достаточно силён, чтобы поднять эту коробку."},
        {"word": "brave", "translation": "храбрый", "example": "The brave soldier fought for his country.",
         "translation2": "Храбрый солдат сражался за свою страну."},
        {"word": "active", "translation": "активный", "example": "She is very active in sports.",
         "translation2": "Она очень активна в спорте."},
        {"word": "quiet", "translation": "тихий", "example": "The library is a quiet place.",
         "translation2": "Библиотека — это тихое место."},
        {"word": "angry", "translation": "злой, сердитый", "example": "He was angry at the delay.",
         "translation2": "Он был злой из-за задержки."},
        {"word": "talkative", "translation": "разговорчивый", "example": "She is very talkative at school.",
         "translation2": "Она очень разговорчивая в школе."},
        {"word": "helpful", "translation": "готовый помочь", "example": "He is always helpful when I need him.",
         "translation2": "Он всегда готов помочь, когда мне это нужно."},
        {"word": "tidy", "translation": "аккуратный", "example": "She keeps her room tidy.",
         "translation2": "Она держит свою комнату в порядке."},
        {"word": "polite", "translation": "вежливый", "example": "He is polite to everyone he meets.",
         "translation2": "Он вежлив со всеми, кого встречает."},
        {"word": "silly", "translation": "глупый", "example": "Stop making silly jokes.",
         "translation2": "Перестань рассказывать глупые шутки."},
        {"word": "honest", "translation": "честный", "example": "She is honest and trustworthy.",
         "translation2": "Она честная и заслуживающая доверия."},
        {"word": "curious", "translation": "любопытный", "example": "The curious child asked many questions.",
         "translation2": "Любопытный ребёнок задал много вопросов."},
        {"word": "shy", "translation": "застенчивый", "example": "He is too shy to speak in public.",
         "translation2": "Он слишком застенчив, чтобы говорить на публике."},
        {"word": "sociable", "translation": "общительный", "example": "She is very sociable at parties.",
         "translation2": "Она очень общительная на вечеринках."}
    ],
    "Группа 9. Профессии": [
        {"word": "my dream", "translation": "моя мечта", "example": "My dream is to travel the world.",
         "translation2": "Моя мечта — путешествовать по миру."},
        {"word": "to come true", "translation": "сбыться", "example": "I hope my dream will come true.",
         "translation2": "Я надеюсь, что моя мечта сбудется."},
        {"word": "to take exams", "translation": "сдавать экзамены", "example": "I need to take exams next week.",
         "translation2": "Мне нужно сдавать экзамены на следующей неделе."},
        {"word": "to leave school", "translation": "закончить школу",
         "example": "He is going to leave school this year.",
         "translation2": "Он собирается закончить школу в этом году."},
        {"word": "to enter an institute (a college)", "translation": "поступить в институт (колледж)",
         "example": "She wants to enter an institute next year.",
         "translation2": "Она хочет поступить в институт в следующем году."},
        {"word": "to get education", "translation": "получить образование",
         "example": "It’s important to get education for your future.",
         "translation2": "Важно получить образование для своего будущего."},
        {"word": "to find a job", "translation": "найти работу", "example": "I’m trying to find a job in my field.",
         "translation2": "Я пытаюсь найти работу в своей области."},
        {"word": "to be independent", "translation": "быть независимым",
         "example": "I want to be independent when I grow up.",
         "translation2": "Я хочу быть независимым, когда вырасту."},
        {"word": "to be interested in", "translation": "интересоваться", "example": "She is interested in science.",
         "translation2": "Она интересуется наукой."},
        {"word": "to study hard", "translation": "усердно учиться", "example": "You need to study hard to succeed.",
         "translation2": "Тебе нужно усердно учиться, чтобы добиться успеха."},
        {"word": "to be in two minds", "translation": "быть в раздумье",
         "example": "I’m in two minds about going to the party.",
         "translation2": "Я в раздумьях насчёт того, идти ли на вечеринку."},
        {"word": "to decide", "translation": "решить", "example": "I need to decide what to do next.",
         "translation2": "Мне нужно решить, что делать дальше."},
        {"word": "to make up one’s mind", "translation": "решить",
         "example": "She has made up her mind to study abroad.", "translation2": "Она решила учиться за границей."},
        {"word": "to change one’s mind", "translation": "передумать",
         "example": "He changed his mind about going to the movies.",
         "translation2": "Он передумал насчёт похода в кино."},
        {"word": "to follow my parents’ profession", "translation": "продолжить профессию родителей",
         "example": "I want to follow my parents’ profession.",
         "translation2": "Я хочу продолжить профессию своих родителей."},
        {"word": "to choose", "translation": "выбрать",
         "example": "It’s difficult to choose between these two options.",
         "translation2": "Трудно выбрать между этими двумя вариантами."},
        {"word": "to make a choice", "translation": "сделать выбор", "example": "It’s time to make a choice.",
         "translation2": "Пора сделать выбор."},
        {"word": "to the right choice", "translation": "правильный выбор",
         "example": "She made the right choice by studying law.",
         "translation2": "Она сделала правильный выбор, выбрав юриспруденцию."},
        {"word": "to the wrong choice", "translation": "неверный выбор",
         "example": "Choosing to skip class was the wrong choice.",
         "translation2": "Пропускать занятия — это был неверный выбор."},
        {"word": "to make a career", "translation": "сделать карьеру",
         "example": "He wants to make a career in medicine.", "translation2": "Он хочет сделать карьеру в медицине."},
        {"word": "to be successful", "translation": "быть успешным",
         "example": "She is determined to be successful in life.",
         "translation2": "Она решительно настроена быть успешной в жизни."}
    ],
    "Группа 10. Спорт": [
        {"word": "sport", "translation": "спорт", "example": "I love to watch sport.",
         "translation2": "Я люблю смотреть спорт."},
        {"word": "sportsman", "translation": "спортсмен", "example": "He is a famous sportsman.",
         "translation2": "Он известный спортсмен."},
        {"word": "sports (kinds of sports)", "translation": "виды спорта", "example": "There are many kinds of sports.",
         "translation2": "Существует много видов спорта."},
        {"word": "sports club", "translation": "спортивная секция",
         "example": "She joined a sports club to play tennis.",
         "translation2": "Она записалась в спортивную секцию, чтобы играть в теннис."},
        {"word": "sports school", "translation": "спортивная школа", "example": "He goes to a sports school to train.",
         "translation2": "Он ходит в спортивную школу, чтобы тренироваться."},
        {"word": "to do sports", "translation": "заниматься спортом", "example": "I want to do sports every day.",
         "translation2": "Я хочу заниматься спортом каждый день."},
        {"word": "to do wrestling", "translation": "заниматься борьбой", "example": "He decided to do wrestling.",
         "translation2": "Он решил заниматься борьбой."},
        {"word": "to play sports (games)", "translation": "играть в спортивные игры",
         "example": "We like to play sports on weekends.",
         "translation2": "Мы любим играть в спортивные игры по выходным."},
        {"word": "to play basketball (chess)", "translation": "играть в баскетбол (шахматы)",
         "example": "He loves to play basketball.", "translation2": "Он любит играть в баскетбол."},
        {"word": "to go skateboarding", "translation": "кататься на скейтборде и т.п.",
         "example": "She wants to go skateboarding today.",
         "translation2": "Она хочет кататься на скейтборде сегодня."},
        {"word": "to go in for", "translation": "заниматься", "example": "I want to go in for swimming.",
         "translation2": "Я хочу заниматься плаванием."},
        {"word": "to go in for swimming", "translation": "заниматься плаванием",
         "example": "He loves to go in for swimming.", "translation2": "Он любит заниматься плаванием."},
        {"word": "football player", "translation": "футболист", "example": "He is a famous football player.",
         "translation2": "Он известный футболист."},
        {"word": "to be a fan of …", "translation": "болельщик", "example": "She is a fan of basketball.",
         "translation2": "Она болельщик баскетбола."},
        {"word": "to join a sports club", "translation": "записаться в спортивный кружок (клуб)",
         "example": "I want to join a sports club.", "translation2": "Я хочу записаться в спортивный клуб."},
        {"word": "to take part in…. (competitions)", "translation": "принимать участие в … (соревнованиях)",
         "example": "He is going to take part in the competition.",
         "translation2": "Он собирается принять участие в соревновании."},
        {"word": "to take place in….", "translation": "проходить в …",
         "example": "The competition will take place in the stadium.",
         "translation2": "Соревнование будет проходить на стадионе."},
        {"word": "to win / to lose", "translation": "выиграть / проиграть …", "example": "I hope to win the match.",
         "translation2": "Я надеюсь выиграть матч."},
        {"word": "to win a prize / a cup", "translation": "выиграть приз / кубок",
         "example": "They won a prize in the competition.", "translation2": "Они выиграли приз на соревновании."},
        {"word": "a winner / a loser", "translation": "победитель / проигравший",
         "example": "He was the winner of the tournament.", "translation2": "Он был победителем турнира."},
        {"word": "match", "translation": "матч", "example": "The football match is tomorrow.",
         "translation2": "Футбольный матч завтра."},
        {"word": "competition", "translation": "соревнование", "example": "There will be a competition next month.",
         "translation2": "Следующим месяцем будет соревнование."},
        {"word": "to train", "translation": "тренироваться", "example": "She trains every day for the marathon.",
         "translation2": "Она тренируется каждый день для марафона."},
        {"word": "to do training", "translation": "ходить на тренировки",
         "example": "I need to do training after school.",
         "translation2": "Мне нужно ходить на тренировки после школы."},
        {"word": "at/in the skating rink", "translation": "на катке", "example": "We will skate at the skating rink.",
         "translation2": "Мы будем кататься на катке."},
        {"word": "at/in the stadium", "translation": "на стадионе", "example": "The match is at the stadium.",
         "translation2": "Матч будет на стадионе."},
        {"word": "at the football pitch", "translation": "на футбольном поле",
         "example": "He is playing at the football pitch.", "translation2": "Он играет на футбольном поле."},
        {"word": "at the sports ground", "translation": "на спортивной площадке",
         "example": "We meet at the sports ground every weekend.",
         "translation2": "Мы встречаемся на спортивной площадке каждую неделю."},
        {"word": "in the gym", "translation": "в спортивном зале", "example": "I work out in the gym every day.",
         "translation2": "Я тренируюсь в спортивном зале каждый день."},
        {"word": "in the swimming pool", "translation": "в бассейне",
         "example": "He swims in the swimming pool every morning.",
         "translation2": "Он плавает в бассейне каждое утро."}
    ]
}

d = {
    1: (
        "Добро пожаловать в Урок 1: Приветствия и прощания!\n\n"
        "Изучите материалы урока, перейдя по ссылке ниже:\n"
        "[Теоритическая часть](https://telegra.ph/Urok-1-Privetstviya-i-proshchaniya-01-09)\n"
        "Практическая часть:\n"
        "    [Тест 1](https://wellemo.com/quiz/take/1efd34da-9fd0-6ac8-92ac-f1947c49ebe7/ru/)\n"
        "[Словарь](https://wooordhunt.ru/)"
    ),

    2: (
        "Добро пожаловать в Урок 2: Образование множественного числа существительных!\n\n"
        "Изучите материалы урока, перейдя по ссылке ниже:\n"
        "[Теоритическая часть](https://telegra.ph/Urok-2-Obrazovanie-mnozhestvennogo-chisla-sushchestvitelnyh-01-16)\n"
        "Практическая часть:\n"
        "    [Тест 1](https://myefe.ru/quizzes/tests-plurals)\n"
        "    [Тест 2](https://englishweb.ru/grammar/plurals-test.html)\n"
        "[Словарь](https://wooordhunt.ru/)"
    ),

    3: (
        "Добро пожаловать в Урок 3: Существительные, имеющие одну форму единственного и множественного числа!\n\n"
        "Изучите материалы урока, перейдя по ссылке ниже:\n"
        "[Теоритическая часть](https://telegra.ph/Urok-3-Sushchestvitelnye-imeyushchie-odnu-formu-edinstvennogo-i-mnozhestvennogo-chisla-02-01)\n"
        "Практическая часть:\n"
        "    [Тест 1](https://englishka.ru/tests/test-mnozhestvennoe-chislo-sushchestvitelnyh-v-anglijskom-yazyke/)\n"
        "[Словарь](https://wooordhunt.ru/)"
    ),

    4: (
        "Добро пожаловать в Урок 4: Исчисляемые и неисчисляемые  существительные!\n\n"
        "Изучите материалы урока, перейдя по ссылке ниже:\n"
        "[Теоритическая часть](https://telegra.ph/Urok-4-Okonchaniya-v-anglijskom-yazyke-02-01)\n"
        "Практическая часть:\n"
        "    [Тест 1](https://englishweb.ru/grammar/count-nouns-test.html)\n"
        "    [Тест 2](https://solncesvet.ru/tests/test-na-temu-ischislyaemye-i-neischislyaemye-sushchestvitelnye-v-angliyskom-yazyke/)\n"
        "[Словарь](https://wooordhunt.ru/)"
    ),

    5: (
        "Добро пожаловать в Урок 5: Much и many в английском языке!\n\n"
        "Изучите материалы урока, перейдя по ссылке ниже:\n"
        "[Теоритическая часть](https://telegra.ph/Urok-6-Much-i-many-v-anglijskom-yazyke-02-03)\n"
        "Практическая часть:\n"
        "    [Тест 1](https://thelang.ru/tests/much-many)\n"
        "    [Тест 2](https://englishka.ru/tests/test-uprazhnenie-na-much-many-few-little/)\n"
        "[Словарь](https://wooordhunt.ru/)"
    ),

    6: (
        "Добро пожаловать в Урок 6: Слова a lot of, little, a little!\n\n"
        "Изучите материалы урока, перейдя по ссылке ниже:\n"
        "[Теоритическая часть](https://telegra.ph/Urok-7-Slova-a-lot-of-little-a-little-02-04)\n"
        "Практическая часть:\n"
        "    [Тест 1](https://myefe.ru/quizzes/tests-few-little-many-much)\n"
        "    [Тест 2](https://test-english.com/grammar-points/a1/much-many-lot-little-few/)\n"
        "[Словарь](https://wooordhunt.ru/)"
    ),

    7: (
        "Добро пожаловать в Урок 7: Слова few, a few!\n\n"
        "Изучите материалы урока, перейдя по ссылке ниже:\n"
        "[Теоритическая часть](https://telegra.ph/Urok-8-Slova-few-a-few-02-04)\n"
        "Практическая часть:\n"
        "    [Тест 1](https://myefe.ru/quizzes/tests-few-little-many-much/test-1)\n"
        "    [Тест 2](https://www.native-english.ru/tests/little-a-little-few-a-few)\n"
        "[Словарь](https://wooordhunt.ru/)"
    ),

    8: (
        "Добро пожаловать в Урок 8: Артикли в английском языке!\n\n"
        "Изучите материалы урока, перейдя по ссылке ниже:\n"
        "[Теоритическая часть](https://telegra.ph/Urok-9-Artikli-v-anglijskom-yazyke-02-04)\n"
        "Практическая часть:\n"
        "    [Тест 1](https://englishweb.ru/grammar/test/test-articles.html)\n"
        "    [Тест 2](https://englishka.ru/tests/test-na-artikli-v-anglijskom/)\n"
        "[Словарь](https://wooordhunt.ru/)"
    ),

    9: (
        "Добро пожаловать в Урок 9: Специальные случаи употребления артиклей!\n\n"
        "Изучите материалы урока, перейдя по ссылке ниже:\n"
        "[Теоритическая часть](https://telegra.ph/Urok-10-Specialnye-sluchai-upotrebleniya-artiklej-02-05)\n"
        "Практическая часть:\n"
        "    [Тест 1](https://engblog.ru/test-articles-1)\n"
        "    [Тест 2](https://www.native-english.ru/tests/articles)\n"
        "[Словарь](https://wooordhunt.ru/)"
    ),

    10: (
        "Добро пожаловать в Урок 10: Оборот There + to be!\n\n"
        "Изучите материалы урока, перейдя по ссылке ниже:\n"
        "[Теоритическая часть](https://telegra.ph/Urok-11-Oborot-There--to-be-02-06)\n"
        "Практическая часть:\n"
        "    [Тест 1](https://onlinetestpad.com/ru/test/308614-there-to-be)\n"
        "    [Тест 2](https://upupenglish.ru/there-is-are-exercises/)\n"
        "[Словарь](https://wooordhunt.ru/)"
    ),

    11: (
        "Добро пожаловать в Урок 11: Степени сравнения прилагательных!\n\n"
        "Изучите материалы урока, перейдя по ссылке ниже:\n"
        "[Теоритическая часть](https://telegra.ph/Urok-12-Stepeni-sravneniya-prilagatelnyh-02-07)\n"
        "Практическая часть:\n"
        "    [Тест 1](https://englishweb.ru/grammar/comparatives-test.html)\n"
        "    [Тест 2](https://englishka.ru/tests/test-na-stepeni-sravneniya-v-anglijskom/)\n"
        "[Словарь](https://wooordhunt.ru/)"
    ),

    12: (
        "Добро пожаловать в Урок 12: Сравнительные обороты!\n\n"
        "Изучите материалы урока, перейдя по ссылке ниже:\n"
        "[Теоритическая часть](https://telegra.ph/Urok-13-Sravnitelnye-oboroty-02-07)\n"
        "Практическая часть:\n"
        "    [Тест 1](https://engblog.ru/test-degrees-of-comparison)\n"
        "    [Тест 2](https://www.native-english.ru/tests/degrees-of-comparison)\n"
        "[Словарь](https://wooordhunt.ru/)"
    ),

    13: (
        "Добро пожаловать в Урок 13: Степени сравнения наречий!\n\n"
        "Изучите материалы урока, перейдя по ссылке ниже:\n"
        "[Теоритическая часть](https://telegra.ph/Urok-14-Stepeni-sravneniya-narechij-02-07)\n"
        "Практическая часть:\n"
        "    [Тест 1](https://englika.ru/tests/test-na-stepeni-sravnenija-narechij-v-anglijskom-jazyke)\n"
        "    [Тест 2](https://skyeng.ru/exercises/adverbs-degrees-of-comparison/)\n"
        "[Словарь](https://wooordhunt.ru/)"
    ),

    14: (
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
    ),

    15: (
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
    ),

    16: (
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
    ),

    17: (
        "Добро пожаловать в Урок 17: Практика по пройденным временам!\n\n"
        "Практическая часть:\n"
        "    [Тест 1](https://wordwall.net/resource/13706334/present-simple-present-continuous-past-simple)\n"
        "    [Тест 2](https://skyeng.ru/exercises/present-simple-present-continuous-past-simple/)\n"
        "    [Тест 3](https://testedu.ru/test/english-language/7-klass/present-simplepresent-continuouspast-simplepast-continuous.html)\n"
        "[Словарь](https://wooordhunt.ru/)"
    )
}
