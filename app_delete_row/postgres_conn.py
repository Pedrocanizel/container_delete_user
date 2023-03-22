import psycopg2
import pandas as pd

def get_connect():
    con = psycopg2.connect(host='bd.bitgcp.com', database='bitgcp_tables',
                           user='postgres', password='example')
    return con


def delete(name, email):
    conn = get_connect()
    cursor = conn.cursor()
    query = f"""DELETE FROM bitgcp.users WHERE search_id = '{name}-{email}';"""
    cursor.execute(query)
    conn.commit()
    conn.close()


def conferir_search_id(name, email):
    conn = get_connect()
    cursor = conn.cursor()
    query = f"""SELECT COUNT(search_id) FROM bitgcp.users WHERE search_id = '{name}-{email}'"""
    contagem = pd.read_sql_query(query, con=conn)
    contagem = contagem['count'].loc[0]
    return contagem