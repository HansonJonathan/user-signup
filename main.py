from flask import Flask, request
import os
import jinja2

template_dir = os.path.join(os.path.dirname(__file__),'templates')

jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir))

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def index():
	template = jinja_env.get_template('home_page.html')
	return template.render()

@app.route("/", methods=['POST'])
def encrypt():
	form_username = request.form['username']
	form_password = request.form['password']
	form_verify_password = request.form['verifyPass']
	form_password = request.form['email']

	return 


app.run()