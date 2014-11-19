'''
Created on 19 Nov 2014

@author: wingfei.seiw
'''
from flask import Flask

app = Flask(__name__)
app.config.from_object('config')

from app import views