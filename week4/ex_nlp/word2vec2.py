from gensim.models import Word2Vec


model = Word2Vec.load('news.model')
while True:
    text = input("검색단어")
    print(model.wv.most_similar(positive=[text]))