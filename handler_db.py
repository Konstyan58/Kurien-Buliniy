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

    async def add_client(self, nedo_id, frst_or_lst_name, username, mail=None, sity=None):
        async with aiosqlite.connect(self.pute_k_fily) as connct:
            cursor = await connct.cursor()
            await cursor.execute("""INSERT INTO Peoples (id, frst_or_lst_name, username, mail, sity) VALUES(?,?,?,?,?)""",(nedo_id, frst_or_lst_name, username, mail, sity))
            await connct.commit()
