#!/usr/bin/python
# coding=utf-8

import io
import sys
import time
import sqlite3
import telepot
import logging
from datetime import date, datetime
import noti

# Set up logging
logging.basicConfig(level=logging.INFO)

# Ensure UTF-8 encoding for standard output
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')

def reply_apt_data(user, loc_param):
    logging.info(f"User {user} requested data for location: {loc_param}")
    res_list = noti.get_data(loc_param)
    msg = ''
    for r in res_list:
        logging.info(f"Data: {r}")
        if len(r + msg) + 1 > noti.MAX_MSG_LENGTH:
            noti.send_message(user, msg)
            msg = r + '\n'
        else:
            msg += r + '\n'
    if msg:
        noti.send_message(user, msg)
    else:
        noti.send_message(user, f'{loc_param}에 해당하는 데이터가 없습니다.')

def save(user, loc_param):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS users(user TEXT, location TEXT, PRIMARY KEY(user, location))')
    try:
        cursor.execute('INSERT INTO users(user, location) VALUES (?, ?)', (user, loc_param))
    except sqlite3.IntegrityError:
        noti.send_message(user, '이미 해당 정보가 저장되어 있습니다.')
    else:
        noti.send_message(user, '저장되었습니다.')
        conn.commit()
    finally:
        conn.close()

def check(user):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS users(user TEXT, location TEXT, PRIMARY KEY(user, location))')
    cursor.execute('SELECT * FROM users WHERE user = ?', (user,))
    for data in cursor.fetchall():
        row = f'id: {data[0]}, location: {data[1]}'
        noti.send_message(user, row)
    conn.close()

def check_all(user):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS users(user TEXT, location TEXT, PRIMARY KEY(user, location))')
    cursor.execute('SELECT location FROM users')
    locations = cursor.fetchall()
    conn.close()

    all_data = ''
    for location in locations:
        loc_param = location[0]
        res_list = noti.get_data(loc_param)
        if res_list:
            for r in res_list:
                if len(r + all_data) + 1 > noti.MAX_MSG_LENGTH:
                    noti.send_message(user, all_data)
                    all_data = r + '\n'
                else:
                    all_data += r + '\n'

    if all_data:
        noti.send_message(user, all_data)
    else:
        noti.send_message(user, '저장된 모든 위치에 대한 데이터가 없습니다.')

def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    if content_type != 'text':
        noti.send_message(chat_id, '난 텍스트 이외의 메시지는 처리하지 못해요.')
        return

    text = msg['text']
    args = text.split(' ')

    if text.startswith('도서관') and len(args) > 1:
        logging.info(f"Processing 도서관 데이터 request for {args[1]}")
        reply_apt_data(chat_id, args[1])
    elif text.startswith('저장') and len(args) > 1:
        logging.info(f"Processing 저장 request for {args[1]}")
        save(chat_id, args[1])
    elif text.startswith('확인'):
        logging.info("Processing 확인 request")
        check(chat_id)
    elif text.startswith('모든정보'):
        logging.info("Processing 모든정보 request")
        check_all(chat_id)
    else:
        noti.send_message(chat_id, "모르는 명령어입니다.\n도서관 [지역명] \n저장 [지역명] \n확인\n모든정보 중 하나의 명령을 입력")

if __name__ == '__main__':
    today = date.today()
    logging.info(f"[{today}] received token: {noti.TOKEN}")

    bot = telepot.Bot(noti.TOKEN)
    logging.info(bot.getMe())

    bot.message_loop(handle)
    logging.info('Listening...')

    while True:
        time.sleep(10)
