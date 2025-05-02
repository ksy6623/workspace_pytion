import pandas as pd
from week2.ex_db.DBManager import DBManager
from wordcloud import wordcloud, WordCloud
from konlpy.tag import Okt
from collections import Counter
sql = """
    SELECT *
    FROM stock_bbs
"""
db = DBManager()
conn = db.get_connection()
df = pd.read_sql(con=conn, sql=sql)
for i, v in df.iterrows():
    print(v['BBS_CONTENTS'])
    #1.명사 추출
    #2.단어 카운트 생성
    #3.워드클라우드 생성
    cloud = WordCloud(font_path="../../dataset/NanumGothicBold.ttf",width=800,height=400,background_color="white")
    gen = cloud.generate_from_frequencies(count)
    plt.figure(figsize=(10,5))
    plt.imshow(gen)
    plt.axis("off")
    plt.show()