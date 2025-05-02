import joblib
import pandas as pd
import numpy as np
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

model = joblib.load('loan_model.pkl')
model_features = joblib.load('model_features.pkl')

test_data = pd.read_csv('./data/test_loan_20.csv')
print(test_data.head())
test_encoded = pd.get_dummies(test_data, drop_first=True)
x = test_encoded.drop(columns=['Loan_Status_Y'])
test_pred = model.predict(x)
test_data['loan_pred'] = np.where(test_pred == 1, 'Approved','Denied')

test_data.to_csv('./data/result.csv', index=False)

y = test_encoded['Loan_Status_Y']
acc = accuracy_score(y, test_pred)
report = classification_report(y, test_pred, target_names=['Denied','Approved'])
print(f"acc:{acc:.2f}")
print(report)
print("혼동 행령 confusion_matrix")
print(confusion_matrix(y,test_pred))