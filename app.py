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
    limit_bal = float(request.form['limit_bal'])
    sex = request.form(['sex'])
    age = int(request.form(['age']))
    education = request.form(['education'])
    marriage = request.form(['marriage'])
    pay = float(request.form(['payment_history']))
    bill_amt = float(request.form(['average_bill']))
    pay_amt1 = float(request.form(['jan_payment']))
    pay_amt2 = float(request.form(['feb_payment']))
    pay_amt3 = float(request.form(['march_payment']))
    pay_amt4 = float(request.form(['april_payment']))
    pay_amt5 = float(request.form(['may_payment']))
    pay_amt6 = float(request.form(['june_payment']))

    if sex == 'male':
        sex = 1
    else:
        sex = 2

    if education == 'uneducated':
        education = 0
    elif education == 'middle_school':
        education = 1
    elif education == 'high_school':
        education = 2
    elif education == 'ug':
        education = 3
    elif education == 'pg':
        education = 4
    elif education == 'phd':
        education = 5
    else:
        education = 6

    if marriage == 'unmarried':
        marriage = 0
    elif marriage == 'married':
        marriage = 1
    elif marriage == 'divorced':
        marriage = 2
    else:
        marriage = 3


    
    predict = model.predict([[limit_bal, sex, education, marriage, age
                , pay, bill_amt, pay_amt1, pay_amt2, pay_amt3, pay_amt4
                , pay_amt5, pay_amt6]])
    return render_template('home.html', prediction_text = 'Credit Card Default Status for account {} : {}'.format(acc_no, predict))


if __name__ =+ '__main__':
    app.run(debug = True)


