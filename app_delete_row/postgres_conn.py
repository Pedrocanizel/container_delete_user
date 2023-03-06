import psycopg2
import datetime
import pandas as pd
import json


def get_connect():
    con = psycopg2.connect(host='localhost', database='bit_pro',
                           user='postgres', password='123')
    return con


def delete(email):
    conn = get_connect()
    cursor = conn.cursor()
    query = f"""DELETE FROM public.cadastro_usuario WHERE email LIKE '%{email}%';"""
    cursor.execute(query)
    conn.commit()
    conn.close()
