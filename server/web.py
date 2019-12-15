from flask import Flask, render_template, request
app = Flask(__name__)
import os

import core
import bot

@app.route('/')
def hello_world():
    return render_template('landing.html')

@app.route('/form/')
def form():
    return render_template('form.html')

@app.route('/register/', methods=['POST'])
def register():
    personal_token, share_token = core.register_user(request.form['name'],
                                                     request.form['button_number'],
                                                     request.form['contacts'])
    return render_template('token.html',
                           personal_token=personal_token,
                           share_token=share_token)

@app.route('/alarm/', methods=['POST'])
def alarm():
    try:
        ud = core.get_user_by_number(request.json['number'])
    except IndexError:
        return '', 400
    bot.send_message_from_alarm(ud['subscribers'], ud['name'])
    return '', 200


if __name__ == '__main__':
    if 'hansel_dev' in os.environ:
        app.run()
    else:
        app.run(host='0.0.0.0', port=80)

