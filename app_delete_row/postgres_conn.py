import psycopg2
import datetime
import pandas as pd
import json


def get_connect():
    con = psycopg2.connect(host='localhost', database='bit_pro',
                           user='postgres', password='123')
    return con


def delete(id_user):
    conn = get_connect()
    cursor = conn.cursor()
    query = f"""DELETE FROM public.permissions_user WHERE id_user = '{id_user}';"""
    cursor.execute(query)
    conn.commit()
    conn.close()
