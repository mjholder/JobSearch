from flask import Flask, render_template, request, redirect
import json

app = Flask(__name__)

try:
    conf = open('jobsearch/statics/config.json')
    hostname = json.load(conf)['hostname']
except:
    hostname = 'pcp2.ccr.buffalo.edu:8080'

@app.route('/')
def main():
    return render_template('index.html', title='Home', host=hostname)

@app.route('/search', methods=['GET'])
def input():
    cluster = request.args['cluster']
    job = request.args['jobid']
    url = "http://" + hostname + "/supremm_rest/loader.html?resource_id=" + cluster + "&jobid=" + job
    print url
    return redirect(302, url)
