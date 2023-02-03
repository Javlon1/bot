import sqlite3 as sq


def sql_start():
    global base, cur
    base = sq.connect('заказ.db')
    cur = base.cursor()
    if base:
        print('data base connected ')
    base.execute('CREATE TABLE IF NOT EXISTS menu(name  TEXT PRIMARY KEY, phone TEXT, address TEXT)')
    base.commit()


async def sql_add_command(state):
    async with state.proxy() as data:
        cur.execute('INSERT INFO menu VALUES (?, ?, ?)', tuple(data.values()))
        base.commit()