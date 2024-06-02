import asyncio
import logging
import sys
from aiogram import Bot, Dispatcher, html, F
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram import types
from aiogram.types import Message
import keyboards
from filter import WebAppDataFilter
from FileManager import FileManager
import os
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("TOKEN")
dp = Dispatcher()
Filemanager = FileManager()

WaitFile = False
Waitmsg = None


@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer(f"Для запуска нажми \"Start\"", reply_markup=keyboards.StartKeyBoards)


@dp.message(WebAppDataFilter())
async def handle_web_app_data(message: types.Message, web_app_data: types.WebAppData):
    global WaitFile
    global Waitmsg
    data = web_app_data.data.split(" ")
    if data[0] == "download":
        msg = await message.answer("Отправка файлы...")
        file = Filemanager.GetFile(FileName=data[1])
        await message.answer_document(file)
        await msg.delete()
    elif data[0] == "upload":
        Waitmsg = await message.answer("Ожидание файла!")
        WaitFile = True
    elif data[0] == "delete":
        result = Filemanager.DeleteFile(data[1])
        if result == True:
            await message.answer("Файл Удален!")
        else:
            await message.answer("Ошибка!")


@dp.message(F.document | F.photo | F.video)
async def handle_document(message: types.Message, bot: Bot):
    global WaitFile
    global Waitmsg
    print(WaitFile)
    if WaitFile == True:
        document = message.document
        await message.answer("Файл сохраняется...")

        file_path = f"{document.file_id}_{document.file_name}"
        await bot.download(document, file_path)

        with open(file_path, 'rb') as file:
            content = file.read()
            Filemanager.PutFile(FileName=document.file_name, Content=content)

        os.remove(file_path)

        await message.answer("Файл сохранен успешно!")
        await Waitmsg.delete()
        WaitFile = False


async def main() -> None:
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    keyboards.WebAppUrl = "https://brief-evident-ant.ngrok-free.app"
    keyboards.Start()
    asyncio.run(main())
