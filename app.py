from flask import Flask, request, render_template
import requests
import pickle

app = Flask(__name__)

model = pickle.load(open('credit_default.pkl','rb'))

@app.route('/', methods = ['GET'])
def home():
    return render_template('home.html')

@app.route('/predict', methods = ['POST'])
def predict():

    acc_no = request.form['acc_no']
    limit_bal = float(request.form['limit_bal'])
    sex = request.form['sex']
    age = int(request.form['age'])
    education = request.form['education']
    marriage = request.form['marriage']
    pay = request.form['payment_history']
    bill_amt = float(request.form['average_bill'])
    pay_amt1 = float(request.form['jan_payment'])
    pay_amt2 = float(request.form['feb_payment'])
    pay_amt3 = float(request.form['march_payment'])
    pay_amt4 = float(request.form['april_payment'])
    pay_amt5 = float(request.form['may_payment'])
    pay_amt6 = float(request.form['june_payment'])

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

    if pay == 'on_time':
        pay = 0
    elif pay == 'advance_one':
        pay = -1
    elif pay == 'advance_two':
        pay = -2
    elif pay == 'delay_one':
        pay = 1
    elif pay == 'delay_two':
        pay = 2
    elif pay == 'delay_three':
        pay = 3
    elif pay == 'delay_four':
        pay = 4
    elif pay == 'delay_five':
        pay = 5
    elif pay == 'delay_six':
        pay = 6
    else:
        pay = 7

    
    predict = model.predict([[limit_bal, sex, education, marriage, age
                , pay, bill_amt, pay_amt1, pay_amt2, pay_amt3, pay_amt4
                , pay_amt5, pay_amt6]])
    if predict == 0:
        output = 'Not Default'
    else:
        output = 'Default'
    return render_template('home.html', prediction_text = 'Credit Card Default Status for account {} : {}'.format(acc_no, output))


if __name__ == '__main__':
    app.run(debug = True)


