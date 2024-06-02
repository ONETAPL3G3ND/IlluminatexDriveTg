from aiogram.utils.keyboard import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.keyboard import WebAppInfo

WebAppUrl = ""
def Start():
    global StartKeyBoards
    StartKey = KeyboardButton(text="Start", web_app=WebAppInfo(url=WebAppUrl))
    StartKeyBoards = ReplyKeyboardMarkup(keyboard=[[StartKey]], resize_keyboard=True)
