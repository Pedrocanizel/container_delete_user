import psycopg2


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
