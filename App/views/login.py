from flask import Blueprint, redirect, render_template, request, send_from_directory
from App.models import Job, db
import json

login_views = Blueprint('login_views', __name__, template_folder='../templates')

@login_views.route('/login')
def index():
  return render_template('login.html')


  
