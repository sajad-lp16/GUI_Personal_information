import sqlite3


def connect():
    conn = sqlite3.connect('data.db')
    cursor = conn.cursor()
    command = """
    create table if not exists user(
    id integer primary key,
    name varchar(30),
    last varchar(30),
    code varchar(11),
    address varchar(100),
    phone varchar(15),
    birth varchar(15))
    """
    cursor.execute(command)
    conn.commit()
    conn.close()


def create(name='', last='', code='', address='', phone='', birth=''):
    if search(code=code):
        return 404
    conn = sqlite3.connect('data.db')
    cursor = conn.cursor()
    command = """
        insert into user values (NULL,?,?,?,?,?,?)
        """
    cursor.execute(command, (name, last, code, address, phone, birth))
    conn.commit()
    conn.close()


def search(name='', last='', code='', address='', phone='', birth=''):
    conn = sqlite3.connect('data.db')
    cursor = conn.cursor()
    command = """
    SELECT * FROM user WHERE name=? OR last=? OR code=? OR address=? OR phone=?
    OR birth=?
            """
    cursor.execute(command, (name, last, code, address, phone, birth))
    data = cursor.fetchall()
    conn.close()
    return data


def view():
    conn = sqlite3.connect('data.db')
    cursor = conn.cursor()
    command = """
              select * from user
              """
    cursor.execute(command)
    data = cursor.fetchall()
    conn.close()
    return data


def update(id, name, last, code, address, phone, birth):
    conn = sqlite3.connect('data.db')
    cursor = conn.cursor()
    command = """
            update user set name=?, last=?, code=?, address=?, phone=?, birth=?
            where id=?
            """
    cursor.execute(command, (name, last, code, address, phone, birth, id))
    conn.commit()
    conn.close()


def delete(id):
    conn = sqlite3.connect('data.db')
    cursor = conn.cursor()
    command = """
                delete from user where id=?
                """
    cursor.execute(command, (id,))
    conn.commit()
    conn.close()


connect()
