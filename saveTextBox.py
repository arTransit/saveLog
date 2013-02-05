"""
	saveTextBox.py	
"""

import flask
from flask import request
import os
import time

app = flask.Flask(__name__)



@app.route('/')
def index():
    """index(): generate index.html
    """
    return flask.render_template('index.html')


        
@app.route('/savelog', methods=['GET', 'POST'])
def savelog():
    filename =  "Logfile_" + time.strftime( '%Y%m%d-%H%M%S',time.localtime()) + ".txt"
    content = request.form['tdata']
    res = flask.Response(content,mimetype='Content-type: text/plain')
    res.headers['Content-disposition'] = 'attachment; filename=%s' % filename
    return res




if __name__ == '__main__':
    app.run(debug=True)

