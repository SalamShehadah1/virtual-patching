from flask import request,session,redirect,url_for,flash
import time

max_attempts=3
block_time=30

def apply_virtual_patch(app):
    
    @app.before_request
    def rate_limit_login():

        if request.endpoint=='login' and request.method=='POST':
            now=time.time()
            attempts=session.get('attempts',1)
            last_attempt=session.get('last_attempt',0)

            if attempts>= max_attempts -1:

                if now-last_attempt<block_time:
                    flash("Too many failed attempts. Try again after "+ str(block_time) +" seconds")
                    return redirect(url_for('login'))
                else:
                    session.pop('attempts',None)
                    session.pop('last_attempts',None)
                    attempts=0
                    session['last_attempt']=now        
