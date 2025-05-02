import sqlite3
conn = sqlite3.connect("mydb.db")
# 1.array or tuple 순서로
sql = """
            INSERT INTO tb_coin VALUES(?, ?, ?)
"""
#2. dict 키로 맵핑
sql2 = """
            INSERT INTO tb_coin VALUES(:marlet, :kr, :en)
"""
data = {
    "market" : "DOGE", "kr":"도지코인","en":"dogecoin"
}
cur = conn.cursor()
# cur.execute(sql, ['TEST','TEST','TEST']) # 쿼리 실행
cur.execute(sql2,data)
conn.commit()
conn.close()
