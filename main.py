from aiogram import Bot, Dispatcher, types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.filters.command import Command
import random
from googletrans import Translator
import asyncio
import sqlite3
from consts import *

API_TOKEN = "7340266796:AAHsWoJi0GDhFDNb7hon7BcJB187L3I3MWY"
bot = Bot(token=API_TOKEN)
dp = Dispatcher()
translator = Translator()
conn = sqlite3.connect('progress.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS user_progress (
    user_id INTEGER PRIMARY KEY,
    progress INTEGER
)
''')
conn.commit()


def get_main_menu(user_id):
    lesson_buttons = []
    max_unlocked = get_user_progress(user_id)

    for i in range(1, 18):
        lesson_name = get_lesson_name(i)
        if i <= max_unlocked:
            lesson_buttons.append(InlineKeyboardButton(text=lesson_name, callback_data=f"lesson_{i}"))
        else:
            lesson_buttons.append(InlineKeyboardButton(text=f"{lesson_name} (закрыт)", callback_data=f"locked"))

    menu = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Переводчик", callback_data="translator")],
        [InlineKeyboardButton(text="Карточки с новыми словами", callback_data="word_cards")],
        [InlineKeyboardButton(text="Подкасты", callback_data="podcasts")],
        *[[button] for button in lesson_buttons]
    ])
    return menu


def get_lesson_name(lesson_number):
    return lesson_names.get(lesson_number, f"Урок {lesson_number} (название не установлено)")


def get_user_progress(user_id):
    cursor.execute('SELECT progress FROM user_progress WHERE user_id = ?', (user_id,))
    result = cursor.fetchone()
    return result[0] if result else 1


def set_user_progress(user_id, progress):
    cursor.execute('REPLACE INTO user_progress (user_id, progress) VALUES (?, ?)', (user_id, progress))
    conn.commit()


def get_back_button():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Вернуться", callback_data="back_to_menu")]
    ])


def get_group_buttons():
    buttons = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text=group, callback_data=f"group_{group}")] for group in word_groups.keys()
    ])
    buttons.inline_keyboard.append([InlineKeyboardButton(text="Вернуться", callback_data="back_to_menu")])
    return buttons


def get_card_buttons(group_name):
    buttons = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Следующая карточка", callback_data=f"next_card_{group_name}")],
        [InlineKeyboardButton(text="Вернуться", callback_data="back_to_menu")]
    ])
    return buttons


@dp.message(Command("start"))
async def send_welcome(message: types.Message):
    user_id = message.from_user.id
    if user_id not in user_progress:
        user_progress[user_id] = 1
    await message.answer("Привет! Я бот для изучения английского языка. Выбери раздел:",
                         reply_markup=get_main_menu(user_id))


@dp.callback_query(lambda c: c.data == "translator")
async def translator_section(callback_query: types.CallbackQuery):
    await callback_query.message.answer("Введите текст для перевода (с русского на английский):",
                                        reply_markup=get_back_button())


@dp.message()
async def translate_message(message: types.Message):
    try:
        result = translator.translate(message.text, src="auto")
        translation = f"Перевод: {result.text}"
        await message.reply(translation, reply_markup=get_back_button())
    except Exception:
        await message.reply("Произошла ошибка при переводе. Попробуйте ещё раз.", reply_markup=get_back_button())


@dp.callback_query(lambda c: c.data == "word_cards")
async def word_cards_section(callback_query: types.CallbackQuery):
    await callback_query.message.answer("Выберите группу слов:", reply_markup=get_group_buttons())


@dp.callback_query(lambda c: c.data.startswith("group_"))
async def group_handler(callback_query: types.CallbackQuery):
    group_name = callback_query.data.split("_", 1)[1]
    user_id = callback_query.from_user.id
    if user_id not in user_remaining_cards:
        user_remaining_cards[user_id] = {}

    if group_name not in user_remaining_cards[user_id]:
        user_remaining_cards[user_id][group_name] = word_groups[group_name].copy()

    if user_remaining_cards[user_id][group_name]:
        card = random.choice(user_remaining_cards[user_id][group_name])
        user_remaining_cards[user_id][group_name].remove(card)
        await callback_query.message.answer(
            f"Слово: {card['word']}\nПеревод: {card['translation']}\nПример: {card['example']}",
            reply_markup=get_card_buttons(group_name)
        )
    else:
        await callback_query.message.answer(
            f"Слова закончились! Пройдите онлайн тест: [Тест по {group_name}](https://forms.yandex.8f0/)",
            reply_markup=get_back_button()
        )


@dp.callback_query(lambda c: c.data.startswith("lesson_"))
async def lesson_handler(callback_query: types.CallbackQuery):
    user_id = callback_query.from_user.id
    lesson_number = int(callback_query.data.split("_")[1])

    max_unlocked = get_user_progress(user_id)

    if lesson_number > max_unlocked:
        await callback_query.answer("Этот урок пока недоступен.", show_alert=True)
    else:
        if lesson_number:
            lesson_text = d[lesson_number]
        else:
            lesson_name = get_lesson_name(lesson_number)
            lesson_text = f"Вы открыли Урок {lesson_number}!"

        await callback_query.message.answer(lesson_text, reply_markup=get_back_button(), parse_mode="Markdown")

        if max_unlocked == lesson_number and lesson_number < 17:
            set_user_progress(user_id, lesson_number + 1)


@dp.callback_query(lambda c: c.data.startswith("next_card_"))
async def next_card(callback_query: types.CallbackQuery):
    user_id = callback_query.from_user.id
    group_name = callback_query.data.split("_", 2)[2]
    remaining_cards = user_remaining_cards.get(user_id, {}).get(group_name, [])

    if not remaining_cards:
        remaining_cards = word_groups[group_name].copy()
        user_remaining_cards[user_id][group_name] = remaining_cards

        test_link = group_tests.get(group_name)

        if test_link:
            test_message = f"Слова закончились! Рекомендуется записать их в словарь и <a href='{test_link}'>проверить себя по пройденному материалу</a>"
        else:
            test_message = "Слова закончились! Тест для этой группы пока не добавлен."

        await bot.send_message(
            chat_id=callback_query.from_user.id,
            text=test_message,
            parse_mode="HTML",
            reply_markup=InlineKeyboardMarkup(inline_keyboard=[
                [InlineKeyboardButton(text="Вернуться", callback_data="back_to_menu")]
            ])
        )
    else:
        card = random.choice(remaining_cards)
        remaining_cards.remove(card)
        user_remaining_cards[user_id][group_name] = remaining_cards

        new_text = f"Слово: {card['word']}\nПеревод: {card['translation']}\nПример: {card['example']}"
        await bot.send_message(
            chat_id=callback_query.from_user.id,
            text=new_text,
            reply_markup=get_card_buttons(group_name)
        )

    await callback_query.answer()


@dp.callback_query(lambda c: c.data == "back_to_menu")
async def back_to_menu(callback_query: types.CallbackQuery):
    user_id = callback_query.from_user.id
    await callback_query.message.answer("Выбери раздел:", reply_markup=get_main_menu(user_id))


@dp.callback_query(lambda c: c.data.startswith("lesson_"))
async def lesson_handler(callback_query: types.CallbackQuery):
    user_id = callback_query.from_user.id
    lesson_number = int(callback_query.data.split("_")[1])

    if lesson_number > user_progress.get(user_id, 1):
        await callback_query.answer("Этот урок пока недоступен.", show_alert=True)
    else:
        lesson_text = f"Вы открыли Урок {lesson_number}!"
        await callback_query.message.answer(lesson_text, reply_markup=get_back_button())

        if user_progress[user_id] == lesson_number and lesson_number < 17:
            user_progress[user_id] += 1


@dp.callback_query(lambda c: c.data == "locked")
async def locked_handler(callback_query: types.CallbackQuery):
    await callback_query.answer("Этот урок пока недоступен. Пройдите предыдущие уроки.", show_alert=True)


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())