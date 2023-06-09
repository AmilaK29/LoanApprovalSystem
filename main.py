from flask import Flask,render_template,request

server = Flask(__name__)

@server.route("/mydetails",methods = ["GET","POST"])
def pageFun():

    form_data = request.form

    loan_id = form_data['loan_id']
    gender = form_data['gender']
    married = form_data['married']
    dependents = form_data['dependents']
    education = form_data['education']
    self_employed = form_data['self_employed']
    applicant_income = form_data['applicant_income']
    coapplicant_income = form_data['coapplicant_income']
    loan_amount = form_data['loan_amount']
    loan_amount_term = form_data['loan_amount_term']
    credit_history = form_data['credit_history']
    property_area = form_data['property_area']

    property_area = float(property_area)
    loan_amount = float(loan_amount)

    val = property_area * loan_amount

    print(property_area,loan_amount)
    print(int(val))

  
    return render_template('mydetails.html')



@server.route("/approval",methods = ["GET","POST"])
def loan_approval():

    form_data = request.form
    mail = form_data['email']
    passd = form_data['password']

    print(mail,passd)    
    return render_template('completion.html')

def decode_strings():
    return

server.run(debug=True)

