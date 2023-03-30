from django.shortcuts import render

# Create your views here.
import requests
from datetime import datetime


def sent_telegram(text: str):
    TOKEN = "1756029562:AAH3F4kVnd2mugso-h89Urepi1JVDE8LNwg"
    chat_id = "505383004"
    now = str(datetime.now())
    message =  now + "\n" + text
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&text={message}"
    print(requests.get(url).json()) # Эта строка отсылает сообщение

