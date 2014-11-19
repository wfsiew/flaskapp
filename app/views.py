'''
Created on 19 Nov 2014

@author: wingfei.seiw
'''
from app import app

@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"