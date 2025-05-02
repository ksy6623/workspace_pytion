import sqlite3
conn = sqlite3.connect("tb_coin_detail")
# conn = sqlite3.connect(":memory:") # 일회성 사용
sql = """
    CREATE TABLE tb_coin_detail(
            market VARCHAR2(20)
            ,price VARCHAR2(100)
            ,update_date VARCHAR2(100)
    )
"""
cur = conn.cursor()
cur.execute(sql) # 쿼리 실행
conn.close()