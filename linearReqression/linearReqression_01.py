import pandas as pd
from sklearn.linear_model import LinearRegression
import pickle

# 파일에서 모델 로드
with open('manhattan_model.pk1', 'rd') as f:
    model = pickle.loads(f)

print(model.coef_)
print(model.intercept_)
data = [[2,2,1749,4,15,10,0,0,0,1,0,0,0]]
column = ['bedrooms', 'bathrooms', 'size_sqft',
       'min_to_subway', 'floor', 'building_age_yrs', 'no_fee', 'has_roofdeck',
       'has_washer_dryer', 'has_doorman', 'has_elevator', 'has_dishwasher',
       'has_patio', 'has_gym']
sample = pd.DataFrame(data, columns=column)
y_pred = model.predict(sample)
print("예측값:",y_pred)
