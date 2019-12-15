from flask import Flask, render_template, request
app = Flask(__name__)

from core import register_user

@app.route('/')
def hello_world():
    return 'Hansel alarm button'

@app.route('/form/')
def form():
    return render_template('form.html')

@app.route('/register/', methods=['POST'])
def register():
    personal_token, share_token = register_user(request.form['name'],
                                                request.form['button_number'],
                                                request.form['contacts'])
    return render_template('token.html',
                           personal_token=personal_token,
                           share_token=share_token)

if __name__ == '__main__':
    app.run()

