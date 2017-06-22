from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def main():
    return 'Welcome!'

@app.route('/Home_Page')
def index():
    user = {'error': ''}
    return render_template('index.html', title='Home', user=user)

@app.route('/Home_Page', methods=['POST'])
def input():
    cluster = request.form['cluster']
    job = request.form['jobid']
    url = "http://pcp2.ccr.buffalo.edu:8080/supremm_rest/loader.html?resource_id=" + cluster + "&jobid=" + job
    if job.isdigit():
        print("Redirecting to " + url)
        return redirect(url, code = 302)
    else:
        user = {'error': "Error: Job id's only contain integers"}
        return render_template('index.html', title='Home', user=user)

