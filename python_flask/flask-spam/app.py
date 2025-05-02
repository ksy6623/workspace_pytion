from flask import Flask, request, render_template
import pickle

from python_flask.flask_coffee.app import predict
from week2.ex_lib.ex_google_translate import message, result

app = Flask(__name__)
with open("spam_model.pkl","rb") as f:
    model = pickle.load(f)
with open("vectiorizer.pkl","rb") as f:
    vectiorizer = pickle.load(f)

@app.route("/",methods=["GET","POST"])
def index():
    prediction = None
    if request.method == 'POST':
        message = request.form['message']
        vec = vectiorizer.transform([message]) # 적용할때는 fit_tranform, 사용할때는 transform
        result = model.predict(vec)[0]
        prediction = '스팸 입니다!' if result == 1 else '정상입니다.'
    return render_template("index.html",prediction="")

if __name__ == '__main__':
    app.run(debug=True)