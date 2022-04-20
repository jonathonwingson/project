from flask import Blueprint, redirect, render_template, request, send_from_directory
from App.models import Job, db
import json

api_views = Blueprint('api_views', __name__, template_folder='../templates')

#@api_views.route('/', methods=['GET'])
#def get_api_docs():
#    return render_template('index.html')
    
 

def searchJob(search):
  return Job.query.filter(Job.Name.like('%'+search+'%'))

@api_views.route('/')
def search():
  search = request.args.get('search')
  job=None
  if search:
    job=searchJob(search)
    return render_template('index.html', job=job)
  return render_template('index.html')
  
  
  


@api_views.route('/login')
def index():
  return render_template('login.html')