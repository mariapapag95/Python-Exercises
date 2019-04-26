from mapper import Database
import wrapper
import sqlite3
import time


def yes(ticker_symbol):
    with Database() as db:
        old_volume = db.cursor.execute('''SELECT trade_volume FROM holdings WHERE ticker_symbol = "{}" and user_id = {user_id};'''
                        .format(ticker_symbol, user_id = 1))
    return old_volume
print(yes("TSLA"))
