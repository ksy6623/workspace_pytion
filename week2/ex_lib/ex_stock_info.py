import pandas as pd
from week2.ex_db.DBManager import DBManager
from week2.ex_db.sqlite04 import market

# 엑셀 읽어오기

krx_df = pd.read_excel("krx.xlsx", engine='openpyxl')
print(krx_df.head())
for i , row in krx_df.iterrows():
    code = row['Code']
    nm = row['Name']
    market = row['Market']
    vol = row['Volume']
    print(f"{i}:{row['Name']}-{row['Code']}-{row['Market']}-{row['Volume']}")
    db.insert(SQL['info_insert'],[code, nm, market, vol])
    # DB에 저장! tb_krx
print("종료")