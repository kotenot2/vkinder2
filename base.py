import psycopg2

conn = psycopg2.connect(database="postgres", user="postgres", password="38621964")

def create_db(conn):
    with conn.cursor() as cur:
        cur.execute("""
        CREATE TABLE IF NOT EXISTS profiles(
        id_user integer UNIQUE,
        name_profiles integer UNIQUE
        );
        """)
        print('Таблица profiles создана')
        conn.commit()



def insert_profiles(conn, id_user, name_profiles):
    with conn.cursor() as cur:
        cur.execute(""" 
            INSERT INTO profiles(
            id_user, name_profiles)
            VALUES(%s, %s);
           
        """, (id_user, name_profiles))
        print('Внесены данные в тблицу')
        conn.commit()
def delete_db(conn):
    with conn.cursor() as cur:
        cur.execute("""
        DELETE from profiles;
        """)
        print('Таблица profiles очищена')
        conn.commit()

def select_profiles(conn, id_user):
    with conn.cursor() as cur:
        cur.execute(""" 
                SELEST name_profiles FROM profiles WHERE id_user = ?
                """, (id_user))
        list_profiles = cur.fetchall()


        print(list_profiles)
    return list_profiles

# create_db(conn)
# insert_profiles(conn, 305633358, name_profiles)