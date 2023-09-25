import sqlite3 as sq

db = sq.connect("tg.db")
cur = db.cursor()


async def db_start():
    cur.execute("CREATE TABLE IF NOT EXISTS users("
                "id INTEGER PRIMARY KEY, "
                "subscribe BOOLEAN)")

    db.commit()


async def create_user(id, subscribe):
    try:
        cur.execute("INSERT INTO users (id, subscribe) VALUES (?, ?)", (id, subscribe))
    except:
        print("User already exists")
    db.commit()


async def subscribe(id):
    cur.execute(f"SELECT subscribe FROM users WHERE id={id}")
    temp = cur.fetchone()[0]
    if temp == 1:
        return "Вы уже подписаны на рассылку!"
    else:
        cur.execute(f"UPDATE users SET subscribe=TRUE WHERE id={id}")
        db.commit()
        return "Вы успешно подписались!"


async def unsubscribe(id):
    cur.execute(f"SELECT subscribe FROM users WHERE id={id}")
    temp = cur.fetchone()[0]
    if temp == 0:
        return "Вы уже отписаны от рассылки!"
    else:
        cur.execute(f"UPDATE users SET subscribe=FALSE WHERE id={id}")
        db.commit()
        return "Нам жаль, что мы вас расстроили! Вы успешно отписались от нашей рассылки!"


async def get_subscribers():
    cur.execute("SELECT id FROM users WHERE subscribe = 1")
    subscribers = [row[0] for row in cur.fetchall()]
    return subscribers
