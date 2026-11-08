#GCE Deployment Instructions (Not working requires pre-payment)
#https://www.youtube.com/watch?v=O8rVd25tw7g&t=2722s

#Notes:
#Next week try making new gmail and using cap one bank account during GCE account creation
#Try googling alternative APIs to GCE, deploy with Render, IBM, or Cloudflare
#Try AWS again without Bootstrap

#Terminal
#pip install gunicorn
#cd MyApp
#pip freeze > requirements.txt

#Web
#https://github.com/
#Create new...
#New repository
#Repository name: Portfoloio_Website_GCE_http_Bootstrap

#Terminal (NOT WORKING! b/c GitHub no longer allows account passwords for command-line authentication, requiring a Personal Access Token (PAT) or SSH key instead.
#Try instead https://www.youtube.com/watch?v=u1Uwj9VqqxY, https://www.youtube.com/watch?v=m-NeesK2Mb0, https://www.youtube.com/watch?v=84caV_3RKgA&t=11
#Try instead https://oneuptime.com/blog/post/2026-01-24-git-unable-to-access-remote/view, https://www.geeksforgeeks.org/git/how-to-fix-git-authentication-failed-error/, https://oneuptime.com/blog/post/2026-01-24-git-unable-to-access-remote/view
#Try instead https://www.youtube.com/watch?v=dtZlEQc0J1w&t=3, https://www.youtube.com/watch?v=dtZlEQc0J1w&t=3, https://www.youtube.com/watch?v=u1Uwj9VqqxY, https://www.youtube.com/watch?v=SgxaQ463Prc
#git init
#git add .
#git commit -m "first commit"
#git branch -M main
#git remote add origin https://github.com/jeffreyfosterworkenvironment/Portfoloio_Website_GCE_http_Bootstrap.git
#git push -u origin main

#Web
#https://cloud.google.com/products/compute
#Try it in console
#Virtual machines -> VM instances
#Create instance
#Name: flask-instance

from flask import Flask, render_template, request, url_for, session, redirect
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import and_, or_
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, RadioField, SubmitField, SelectField
from wtforms import HiddenField
from wtforms.validators import DataRequired
from datetime import datetime

application = Flask(__name__)

application.config['SECRET_KEY'] = 'thequickbrownfrog'

import jinja2

bootstrap = Bootstrap(application)

class SearchButton_Form(FlaskForm):
    submit = SubmitField('Go To Search')

@application.route('/')
def index():
    form2 = SearchButton_Form()
    return render_template('index.html', form2=form2)


@application.route('/results')
def presults():
    return render_template('results.html')

@application.route('/results2')
def presults2():
    return render_template('results2.html')

@application.route('/results3')
def presults3():
    return render_template('results3.html')

if __name__ == "__main__":
    application.debug = True
    application.run()

