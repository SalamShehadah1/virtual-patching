from flask import Flask,request,render_template,redirect,url_for,session
from virtual_patch import apply_virtual_patch
import time

app=Flask(__name__)
app.secret_key="test123"
@app.route('/',methods=['GET','POST'])

def login():
    if request.method=='POST':
        username=request.form.get('username','')
        password=request.form.get('password','')

        if username=="admin" and password=="salam123":
           session.pop('attempts',None)
           session.pop('last_attempt',None)
           return render_template("home.html")
        
        else:
            session['attempts']=session.get('attempts',0) +1
            session['last_attempt']=time.time()
            session['error']="!!! Invalid Credentials"
            return redirect(url_for("login"))     
        
    else:
        error=session.pop('error',None)
        return render_template("login.html",error=error)
    
if __name__=='__main__':
    app.run(debug=True)