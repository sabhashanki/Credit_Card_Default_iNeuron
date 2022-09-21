from flask import Flask, request, render_template
import pickle
import numpy as np
import requests

app = Flask(__name__)

model = pickle.load(open('credit_default.pkl','rb'))

@app.route('/', method = ['GET'])
def home():
    return render_template('home.html')

@app.route('/predict', method = ['POST'])
def predict():
    acc_no = request.form(['acc_no'])
    limit_bal = int(request.form['limit_bal'])
    sex = request.form(['sex'])
    age = request.form(['age'])
    education = request.form(['education'])
    marriage = request.form(['marriage'])
    pay = request.form(['repayment_status'])
    bill_amt = request.form(['average_bill'])
    pay_amt1 = request.form(['jan_payment'])
    pay_amt2 = request.form(['feb_payment'])
    pay_amt3 = request.form(['march_payment'])
    pay_amt4 = request.form(['april_payment'])
    pay_amt5 = request.form(['may_payment'])
    pay_amt6 = request.form(['june_payment'])
    predict = model.predict([[limit_bal, sex, education, marriage, age
                , pay, bill_amt, pay_amt1, pay_amt2, pay_amt3, pay_amt4
                , pay_amt5, pay_amt6]])
    return render_template('home.html', prediction_text = 'Credit Card Default Status : {}'.format(predict))


if __name__ =+ '__main__':
    app.run(debug = True)


