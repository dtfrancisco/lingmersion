from flask import g

def fetch_one_row_closed(sql, properties):
    cur = g.conn.cursor()
    cur.execute(sql)
    row = cur.fetchone()
    cur.close()
    return row

def fetch_one_row_unclosed(sql, properties):
    cur = g.conn.cursor()
    cur.execute(sql)
    row = cur.fetchone()
    return row

def fetch_rows_as_dict(sql, properties):
    cur = g.conn.cursor()
    cur.execute(sql)
    row = cur.fetchone()
    dict_rows = convert_data_for_frontend(row, cur, properties)
    cur.close()
    return dict_rows

def fetch_rows(sql, properties):
    cur = g.conn.cursor()
    cur.execute(sql)
    rows = cur.fetchall()
    cur.close()
    return rows

def add_or_update_row(sql, data):
    cur = g.conn.cursor()
    cur.execute(sql, data)
    g.conn.commit()
    cur.close()

def convert_data_for_frontend(row, cur, properties):
    dict_rows = []

    while row is not None:
        if len(properties) == len(row): 
            dict_row = {properties[i] : row[i] for i, _ in enumerate(row)} 

        dict_rows.append(dict_row)

        row= cur.fetchone()

    return dict_rows
