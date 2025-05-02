import numpy as np
import pickle
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, LSTM, Dense
from tensorflow.keras.callbacks import EarlyStopping, ModelCheckpoint
import os
# 데이터 로드
data_dir = "naver_data"
x_train = np.load(os.path.join(data_dir,'x_train.npy'))
y_train = np.load(os.path.join(data_dir,'y_train.npy'))
x_test = np.load(os.path.join(data_dir,'x_test.npy'))
y_test = np.load(os.path.join(data_dir,'y_test.npy'))

with open(os.path.join(data_dir,'tokenizer.pkl'),'rb') as f:
    tokenize = pickle.load(f)
with open(os.path.join(data_dir,'meta_info.txt'),encoding='utf-8') as f:
    meta = {line.split('=')[0]:
                line.strip().split('=')[1] for line in f}
    max_len = int(meta['max_len'])
    vocab_size = int(meta['vocab_size'])
    # 모델 생성
    print(max_len, vocab_size)
    model = Sequential()
    model.add(Embedding(input_dim=vocab_size, output_dim=100))
    model.add(LSTM(128))
    model.add(Dense(1,activation='sigmoid'))
    model.compile(optimizer='rmsprop',loss='binary_crossentropy',metrics=['acc'])
    es = EarlyStopping(monitor='val_loss',mode='min', verbose=1,patience=4)
    mc = ModelCheckpoint('best_lstm_model.h5',monitor='val_acc',mode='max',verbose=1,save_best_only=True)
    # 학습 전 입력 확인
    print(f"x_train.shape: {x_train.shape}") #(num_samples, max_len)
    print(f"y_train.shape: {y_train.shape}") #(num_samples, )
    # 학습
    model.fit(x_train, y_train, epochs=15, batch_size=64, validation_split=0.2, callbacks=[es,mc])
    # 테스트 평가
    print("text acc:",model.evaluate(x_test,y_test)[1])