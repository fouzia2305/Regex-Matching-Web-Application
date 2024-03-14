from flask import Flask, request, render_template
import re
app=Flask(__name__)



@app.route('/')
def index():
    return render_template('home.html')
@app.route('/outcome',methods=['POST'])
def outcome():
    test_string=request.form['test_string']
    regex=request.form['regex']
    regex_matches=re.findall(regex,test_string)
    
    return render_template('home.html',regex_matches=regex_matches)
@app.route("/validate_email", methods=["POST"])
def validate_email():
    email=request.form['email']
    email_regex=r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    if re.match(email_regex,email):
        result="Valid email address"
    else:
        result="Invalid email address"
    return render_template('email_validation.html',result=result)


    

if __name__=='__main__':
    app.run(debug=True,host='0.0.0.0',port=5000)
    