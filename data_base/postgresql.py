import psycopg2
from config import host, user, password, db_name


def get_postgres_connection():
    """This function create connection to Postgres DB"""
    try:
        connection = psycopg2.connect(
            host=host,
            user=user,
            password=password,
            database=db_name
        )
        # connection.autocommit = True
        return connection
    except Exception as _ex:
        print('[INFO] Error while working with PostgreSQL', _ex)


async def create_table():
    connection = get_postgres_connection()
    with connection.cursor() as cursor:
        cursor.execute(
            """CREATE TABLE company(
            name varchar(50) PRIMARY KEY,
            login varchar(50) NOT NULL,
            password varchar(50) NOT NULL);"""
        )
        print("[INFO] Table created successfully")


# the cursor for performing database operations
async def conn_cur():
    connection = get_postgres_connection()
    with connection.cursor() as cursor:
        cursor.execute(
            "SELECT version();"
        )
        print(f'Server version: {cursor.fetchone()}')


async def insert_user_in_table(user_id, company):
    insert_user = f"""
            INSERT INTO users
            (id, company)
            VALUES (%s, %s)
            """

    try:
        connection = get_postgres_connection()
        cursor = connection.cursor()
        cursor.execute(
            insert_user, (user_id, company)
        )
        connection.commit()
        cursor.close()
        connection.close()
        return '[INFO] Data was successfully inserted'
    except Exception as _ex:
        print(_ex)
        return '[INFO] Error while working with PostgreSQL'


async def insert_company_in_table(name, login, password):
    insert_company = f"""
            INSERT INTO company
            (name, login, password)
            VALUES (%s, %s, %s)
            """

    try:
        connection = get_postgres_connection()
        cursor = connection.cursor()
        cursor.execute(
            insert_company, (name, login, password)
        )
        connection.commit()
        cursor.close()
        connection.close()
        return '[INFO] Data was successfully inserted'
    except Exception as _ex:
        print(_ex)
        return '[INFO] Error while working with PostgreSQL'


async def select_from_user_table():
    connection = get_postgres_connection()
    with connection.cursor() as cursor:
        cursor.execute(
            """SELECT * FROM users;"""
        )

        return cursor.fetchall()


async def select_from_company_table():
    connection = get_postgres_connection()
    with connection.cursor() as cursor:
        cursor.execute(
            """SELECT * FROM company;"""
        )

        return cursor.fetchall()


async def delete_company(name):
    del_company = f"""DELETE FROM company WHERE name = %s;"""
    # try:
    connection = get_postgres_connection()
    cursor = connection.cursor()
    cursor.execute(
        del_company, (name)
    )
    connection.commit()
    cursor.close()
    connection.close()
    return '[INFO] Data was successfully deleted'
    # except Exception as _ex:
    #     print(_ex)
    #     return '[INFO] Error while working with PostgreSQL'

# finally:
#     if connection:
#         connection.close()
#         print('[INFO] PostgreSQL connection closed')