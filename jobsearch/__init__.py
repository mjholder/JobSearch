from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('index.html', title='Home')

@app.route('/search', methods=['GET'])
def input():
    cluster = request.args['cluster']
    job = request.args['jobid']
    url = "http://pcp2.ccr.buffalo.edu:8080/supremm_rest/loader.html?resource_id=" + cluster + "&jobid=" + job
    print url
    return redirect(302, url)
