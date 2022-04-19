from flask import Blueprint, redirect, render_template, request, send_from_directory
from App.models import Job, db
import json

job_views = Blueprint('job_views', __name__, template_folder='../templates')

@job_views.route('/jobs', methods=['GET'])
def index():
    jobs = Job.query.all()
    return render_template('jobs.html', jobs = jobs)



