from django.shortcuts import render

# Create your views here.
import requests
from datetime import datetime


def sent_telegram(text: str):
    TOKEN = "6297936343:AAFjqRlTyyaKmX2p2SBrNx6RUSkYmA3mGdE"
    chat_id = "6102172794"
    now = str(datetime.now())
    message =  now + "\n" + text
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&text={message}"
    print(requests.get(url).json()) # Эта строка отсылает сообщение

