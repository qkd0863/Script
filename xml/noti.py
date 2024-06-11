import sys
import time
import sqlite3
import os
import logging
import requests
import xml.etree.ElementTree as ET
from urllib.parse import quote
from datetime import date, datetime
import telepot

# Set up logging
logging.basicConfig(level=logging.INFO)

# Ensure API key and token are obtained from environment variables
API_KEY = os.getenv('API_KEY', '94c80014751c43c3aff04a8290cda503')
TOKEN = '7204520635:AAHr0LSnYCcvw70SowiNTUF_55fV7UBH464'
MAX_MSG_LENGTH = 300
BASE_URL = 'https://openapi.gg.go.kr/TBGGIBLLBR'

bot = telepot.Bot(TOKEN)

def get_data(loc_param):
    res_list = []
    queryParams = {'KEY': API_KEY, 'Type': 'xml', 'SIGUN_NM': loc_param, 'pIndex': '1', 'pSize': '1000'}
    response = requests.get(BASE_URL, params=queryParams)

    if response.status_code != 200:
        logging.error(f"Error fetching data from URL: {response.status_code}")
        return res_list

    root = ET.fromstring(response.text)
    items = root.findall('.//row')

    for item in items:
        try:
            sigun_nm = item.findtext("SIGUN_NM")
            if sigun_nm != loc_param:
                continue
            data = {
                "SIGUN_NM": item.findtext("SIGUN_NM"),
                "LOCPLC_ADDR": item.findtext("LOCPLC_ADDR"),
                "TELNO": item.findtext("TELNO"),
                "HMPG_ADDR": item.findtext("HMPG_ADDR"),
                "LIBRRY_NM": item.findtext("LIBRRY_NM"),
                "RECSROOM_OPEN_TM_INFO": item.findtext("RECSROOM_OPEN_TM_INFO"),
                "READROOM_OPEN_TM_INFO": item.findtext("READROOM_OPEN_TM_INFO"),
                "RECSROOM_REST_DE_INFO": item.findtext("RECSROOM_REST_DE_INFO"),
                "READROOM_REST_DE_INFO": item.findtext("READROOM_REST_DE_INFO"),
                "REFINE_WGS84_LAT": item.findtext("REFINE_WGS84_LAT"),
                "REFINE_WGS84_LOGT": item.findtext("REFINE_WGS84_LOGT"),
                "DMSTC_BOOK_DATA_CNT": item.findtext("DMSTC_BOOK_DATA_CNT"),
                "FRN_BOOK_DATA_CNT": item.findtext("FRN_BOOK_DATA_CNT")
            }
            row = ",".join(data.values())
            res_list.append(row)
        except Exception as e:
            logging.error(f"Error parsing item: {e}")
            continue
    return res_list

def send_message(user, msg):
    try:
        bot.sendMessage(user, msg)
    except:
        logging.error("Error sending message", exc_info=True)

def run(date_param, param='11710'):
    conn = sqlite3.connect('logs.db')
    cursor = conn.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS logs(user TEXT, log TEXT, PRIMARY KEY(user, log))')
    conn.commit()

    user_cursor = sqlite3.connect('users.db').cursor()
    user_cursor.execute('CREATE TABLE IF NOT EXISTS users(user TEXT, location TEXT, PRIMARY KEY(user, location))')
    user_cursor.execute('SELECT * from users')

    for data in user_cursor.fetchall():
        user, param = data
        logging.info(f"Processing user: {user}, location: {param}")
        res_list = get_data(param)
        msg = ''

        for r in res_list:
            try:
                cursor.execute('INSERT INTO logs(user, log) VALUES (?, ?)', (user, r))
            except sqlite3.IntegrityError:
                continue
            else:
                logging.info(f"New log entry: {r}")
                if len(r + msg) + 1 > MAX_MSG_LENGTH:
                    send_message(user, msg)
                    msg = r + '\n'
                else:
                    msg += r + '\n'
        if msg:
            send_message(user, msg)
    conn.commit()

if __name__ == '__main__':
    today = date.today()
    logging.info(f"[{today}] received token: {TOKEN}")

    bot = telepot.Bot(TOKEN)
    logging.info(bot.getMe())

    run(date.today().strftime('%Y%m'))
