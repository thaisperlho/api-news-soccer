import psycopg2
from datetime import datetime

def conn():
    connection = psycopg2.connect(database="postgres", user="postgres", password="1234", host="localhost", port="5432")
    return connection

def insert(name:str, price:float, is_offer:bool, created_at:datetime, updated_at:datetime):
    sql = f"""
        insert into items(
            name, 
            price, 
            is_offer, 
            created_at, 
            updated_at
        ) values (
            '{name}',
            {price},
            {is_offer},
            '{created_at}',
            '{updated_at}'
        )
        RETURNING id
    """
    con = conn()
    cursor = con.cursor()
    cursor.execute(sql)
    con.commit()
    id = cursor.fetchone()[0]
    cursor.close()
    con.close()
    return id

def update(name:str,price:float,is_offer:bool,updated_at:datetime ,id:int):
    sql = f"""
        update items 
        set 
        name='{name}',
        price='{price}',
        is_offer='{is_offer}',
        updated_at='{updated_at}'
        where 
        id={id}"""
    con = conn()
    cursor = con.cursor()
    cursor.execute(sql)
    con.commit()
    cursor.close()
    con.close()
    return "ok"

def select(id:int):
    sql = f"""
        select * from items 
        where id={id}"""
    con = conn()
    cursor = con.cursor()
    cursor.execute(sql)
    data = cursor.fetchone()
    cursor.close()
    con.close()
    return data
    
def delete(id:int):
    sql = f"""
        delete from items 
        where id={id}"""
    con = conn()
    cursor = con.cursor()
    cursor.execute(sql)
    con.commit()
    cursor.close()
    con.close()
    return "ok"

#insert("Carlos", 500.00, False, datetime.now(), datetime.now())

#update(name="Lais",price=600.00,is_offer=True, updated_at=datetime.now(),id=5)

#data = select(2)
#print(data)

#delete(id=1)
