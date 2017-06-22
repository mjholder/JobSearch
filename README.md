# JobSearch
To install directly from directory:
1. Go to jobsearch directory with setup.py in it
2. $ pip install -e .

Or install with an rpm package:
1. Go to jobsearch directory with setup.py in it
2. $ python setup.py bdist_rpm
3. $ yum install dist/jobsearch-x.x.x-1.xxxx.rpm

To run:
1. $ FLASK_APP=jobsearch
2. $ flask run
