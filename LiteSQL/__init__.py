# =============================================================================
# Придумал и разработал - MaMush (vk.com/maks.mushtriev2, t.me/Error_mak25)
# Гитхаб - github.com/Ma-Mush/LiteSQL
# PypI - pypi.org/project/litesql/
# =============================================================================
import sqlite3
class lsql():
    def __init__(self, file):
        f = file[::-1]
        if f[:4] == "db.":
            f = f[4:]
            file = f[::-1]
        self.conn = sqlite3.connect(f"{file}.db")
        self.cursor = self.conn.cursor()

    def create(self, names, table="albums"):
        self.cursor.execute(f"CREATE TABLE {table} ({names})")
        self.conn.commit()
        
    def insert_data(self, data_mass, len_title, table="albums"): 
        len_title = "?,"*(len_title-1) + "?"
        self.cursor.executemany(f"INSERT INTO {table} VALUES ({len_title})", data_mass)
        self.conn.commit()
        
    def edit_data(self, title_last, last, title_new, new, table="albums"):
        self.cursor.execute(f"UPDATE {table} SET {title_new} = {new} WHERE {title_last} = {last}")
        self.conn.commit()  
        
    def delete_data(self, name, title_name, table="albums"):
        self.cursor.execute(f"DELETE FROM {table} WHERE {title_name} = {name}")
        
    def select_data(self, name, title, row_factor=False, table="albums"):
        self.cursor.execute(f"SELECT * FROM {table} WHERE {title}=?", [(name)])
        if row_factor:
            return self.cursor.fetchone()
        else:
            return self.cursor.fetchall()
        
    def select_data_with_sort(self, type_sort, name, title_name, table="albums"):
        a = []
        if name != None:
            for row in self.cursor.execute(f"SELECT {type_sort}, * FROM {table} ORDER BY {title_name}", [(name)]):
                a.append(row)
            return a
        else:
            for row in self.cursor.execute(f"SELECT {type_sort}, * FROM {table} ORDER BY {title_name}"):
                a.append(row)
            return a
        
    def search(self, type_search, name_search, table="albums"):
        self.cursor.execute(f"SELECT * FROM {table} WHERE {type_search} LIKE {name_search}")
        return self.cursor.fetchall()
    
    def get_all_data(self, table="albums"):
        self.cursor.execute(f"SELECT * FROM {table}")
        return self.cursor.fetchall()
    
    def get_cursor(self):
        return self.cursor
    
    def get_connect(self):
        return self.conn
