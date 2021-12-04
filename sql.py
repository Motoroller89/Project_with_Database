import psycopg2
import psycopg2.extras
from psycopg2 import sql
from config import host,user,password,db_name



def date():
    conn = psycopg2.connect (
            dbname = db_name,
            user = user,
            host = host,
            password = password
        )

    cursor = conn.cursor()
    return cursor

def return_records():
    cursor = date()
    sql_object = sql.SQL(
         "SELECT * FROM suppliers;"
    ).format(

        sql.Identifier('suppliers')
    )

    try:
        cursor.execute(sql_object)
        table_data = cursor.fetchall()
        cursor.close()

    except Exception as err:
        print ("PostgreSQL psycopg2 cursor.execute() ERROR:", err)
        table_data = None

    return table_data



def name_company(description):
    cursor = date()
    sql_object = sql.SQL(
         f"SELECT * FROM suppliers where company_name like '{description}%'"
    ).format(

        sql.Identifier('suppliers')
    )

    try:
        cursor.execute(sql_object)
        table_data = cursor.fetchall()
        cursor.close()

    except Exception as err:
        print ("PostgreSQL psycopg2 cursor.execute() ERROR:", err)
        table_data = None

    return table_data

