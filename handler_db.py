import aiosqlite


class Database:
    def __init__(self, pute_k_fily):
        self.pute_k_fily = pute_k_fily

    async def crt_new_tbl(self):
        async with aiosqlite.connect(self.pute_k_fily) as connct:
            cursor = await connct.cursor()
            await cursor.execute("CREATE TABLE IF NOT EXISTS Peoples("
                                 "id INTEGER,"
                                 "frst_or_lst_name TEXT,"
                                 "mail TEXT,"
                                 "sity TEXT,"
                                 "username TEXT)")
            await connct.commit()

    async def tbl_for_ban(self):
        async with aiosqlite.connect(self.pute_k_fily) as connct:
            cursor = await connct.cursor()
            await cursor.execute("CREATE TABLE IF NOT EXISTS Banned("
                                 "id INTEGER,"
                                 "frst_or_lst_name TEXT,"
                                 "username TEXT,"
                                 "prichina TEXT)")
            await connct.commit()

    async def add_client(self, nedo_id, frst_or_lst_name, username, mail=None, sity=None):
        async with aiosqlite.connect(self.pute_k_fily) as connct:
            cursor = await connct.cursor()
            await cursor.execute(
                """INSERT INTO Peoples (id, frst_or_lst_name, username, mail, sity) VALUES(?,?,?,?,?)""",
                (nedo_id, frst_or_lst_name, username, mail, sity))
            await connct.commit()

    async def add_client_for_ban(self, nedo_id, frst_or_lst_name, username, prichina):
        async with aiosqlite.connect(self.pute_k_fily) as connct:
            cursor = await connct.cursor()
            await cursor.execute(
                """INSERT INTO Banned (id, frst_or_lst_name, username, prichina) VALUES(?,?,?,?)""",
                (nedo_id, frst_or_lst_name, username, prichina))
            await connct.commit()

    async def check_client_for_ban(self, nedo_id):
        async with aiosqlite.connect(self.pute_k_fily) as connct:
            cursor = await connct.cursor()
            await cursor.execute("""SELECT id,username FROM Banned WHERE id = ?""", (nedo_id,))
            answer = await cursor.fetchone()
            if answer is None:
                return False
            else:
                return True

    async def check_client(self, nedo_id):
        async with aiosqlite.connect(self.pute_k_fily) as connct:
            cursor = await connct.cursor()
            await cursor.execute("""SELECT id,username FROM Peoples WHERE id = ?""", (nedo_id,))
            answer = await cursor.fetchone()
            if answer is None:
                return False
            else:
                return True


"""
1. Сделать просто проверку, что если пользователь который пишет что-то боту и при этом он есть в базе данных бана, то написать ему: "ВЫ ЗАБАНЕНЫ!!!!1111111 =((((("
2. Для этого нужно создать функцию, которая проверяет, есть ли чел в БД (в бане), ты её уже делал...
"""
