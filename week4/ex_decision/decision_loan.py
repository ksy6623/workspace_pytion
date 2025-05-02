# https://www.kaggle.com/datasets/altruistdelhite04/loan-prediction-problem-dataset?select=test_Y3wMUE5_7gLdaTN.csv
# Loan_ID: 대출 ID
# Gender: 성별
# Married: 결혼 여부
# Dependents: 부양가족 수
# Education: 학력 수준
# Self_Employed: 자영업 여부
# ApplicantIncome: 신청자의 소득
# CoapplicantIncome: 공동 신청자의 소득
# LoanAmount: 대출 금액
# Loan_Amount_Term: 대출 상환 기간
# Credit_History: 신용 이력
# Property_Area: 재산 위치
# Loan_Status: 대출 승인 여부 (Y: 승인, N: 불승인)
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.metrics import accuracy_score, classification_report
from sklearn.preprocessing import LabelEncoder
import matplotlib.pyplot as plt
import pandas as pd
import joblib

file_path = './data/train_loan_80.csv'
loan_data = pd.read_csv(file_path)
loan_data.head()
print(loan_data.info())
print(loan_data.describe())
loan_encoded = pd.get_dummies(loan_data,drop_first=True)
x = loan_encoded.drop(columns=['Loan_Status_Y'])
y = loan_encoded['Loan_Status_Y']

x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2)
model = DecisionTreeClassifier(criterion='gini',max_depth=5,random_state=42)
model.fit(x_train,y_train)
pred = model.predict(x_test)
joblib.dump(model,'loan_model.pkl')
joblib.dump(x.columns,'model_features.pkl')
acc = accuracy_score(y_test,pred)
report = classification_report(y_test, pred, target_names=['Denied','Approved'])
print(f"model acc:{acc:.2f}")
print(report)
plt.figure(figsize=(20,10))
plot_tree(model,feature_names=x.columns,class_names=['Denied','Approved'],filled=True,rounded=True,fontsize=10)
plt.show()