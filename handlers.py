from aiogram.types import Message
from aiogram.dispatcher.filters import Command

from main import dp
from sql import city
from sql import search_city
from sql import search_job


@dp.message_handler(Command('start'))
async def start_cmd(message: Message):
    await message.answer(f"Добро пожаловать {message.from_user.first_name} {message.from_user.last_name}!\n"
                f"Я помощник подбора вакансий. "
                f"\nВведите /city, чтобы увидеть список населенных пунктов в которых открыты вакансии.")


@dp.message_handler(Command('city'))
async def city_cmd(message: Message):
    await message.answer(await city())
    await message.answer("Выше представлен список населенных пунктов в которых есть открытые вакансии.\n"
                         "Введите название города интересующего вас в формате:\n"
                         "/search_city Населенный пункт")


@dp.message_handler(commands=['search_city'])
async def search_city_cmd(message: Message):
    s = message.get_args()
    await message.answer(f"Вы выбрали город {s}.\n"
                         f"Ниже представлены вакансии доступные в городе {s}.")
    await message.answer(await search_city(s))


@dp.message_handler(commands=['search_job'])
async def search_job_cmd(message: Message):
    s = message.get_args()
    await message.answer(f"Вы выбрали вакансии содержащие слово {s}.\n"
                         f"Ниже представлены вакансии содержащие слово {s}.")
    await message.answer(await search_job(s))


@dp.message_handler(content_types=['text'])
async def text_cmd(message: Message):
    if message.text == "Привет":
        await message.answer(f"Добро пожаловать {message.from_user.first_name} {message.from_user.last_name}!\n"
                f"Я помощник подбора вакансий. "
                f"\nВведите /city, чтобы увидеть список населенных пунктов в которых открыты вакансии.")
    elif message.text == "/help":
        await message.answer(f"Добро пожаловать {message.from_user.first_name} {message.from_user.last_name}!\n"
                f"Я помощник подбора вакансий. "
                f"\nВведите /city, чтобы увидеть список населенных пунктов в которых открыты вакансии.")
    else:
        await message.answer("Мой функционал ограничен, прошу Вас ввести одну из следующих команд для запуска сценария:"
                             " /start")
