# =============================================================================
# Придумал и разработал - MaMush (vk.com/maks.mushtriev2, t.me/Error_mak25)
# Гитхаб - github.com/Ma-Mush/LiteSQL
# PypI - pypi.org/project/litesql/
# =============================================================================

class lsql():
    import sqlite3
    conn = ''
    cursor = ''
    def connect(file_name):
        f = file_name[::-1]
        if f[:4] == 'db.':
            f = f[4:]
            file_name = f[::-1]
        global conn, cursor
        import sqlite3
        conn = sqlite3.connect(f"{file_name}.db")
        cursor = conn.cursor()
    def create(names, table="albums"):
        global conn, cursor
        cursor.execute(f"CREATE TABLE {table} ({names})")
        conn.commit()
    def insert_data(data_mass, len_title, table="albums"): 
        global conn, cursor
        titl = '?,' * (len_title - 1 )
        titl += '?'
        cursor.executemany(f"INSERT INTO {table} VALUES ({titl})", data_mass)
        conn.commit()
    def edit_data(title_last, last, title_new, new, table="albums"):
        global conn, cursor
        cursor.execute(f"UPDATE {table} SET {title_new} = '{new}' WHERE {title_last} = '{last}'")
        conn.commit()   
    def delete_data(name, title_name, table="albums"):
        global conn, cursor
        cursor.execute(f"DELETE FROM {table} WHERE {title_name} = '{name}'")
    def select_data(name, title, row_factor=False, table="albums"):
        global conn, cursor
        cursor.execute(f"SELECT * FROM {table} WHERE {title}=?", [(name)])
        if row_factor:
            return cursor.fetchone()
        else:
            return cursor.fetchall()
    def select_data_with_sort(type_sort, name, title_name, table="albums"):
        global conn, cursor
        a = []
        if name != None:
            for row in cursor.execute(f"SELECT {type_sort}, * FROM {table} ORDER BY {title_name}", [(name)]):
                a.append(row)
            return a
        else:
            for row in cursor.execute(f"SELECT {type_sort}, * FROM {table} ORDER BY {title_name}"):
                a.append(row)
            return a
    def search(type_search, name_search, table="albums"):
        global conn, cursor
        sql = f"SELECT * FROM {table} WHERE {type_search} LIKE '{name_search}'"
        cursor.execute(sql)
        return cursor.fetchall()