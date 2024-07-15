import pymysql

def init_DB(DB):
    conn = pymysql.connect(
        host='localhost',
        user="mysql",
        passwd="jiaotongno1",
        db=DB)
    cursor = conn.cursor()
    return conn, cursor