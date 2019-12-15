from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hansel alarm button'

@app.route('/form/')
def form():
    return render_template('form.html')

@app.route('/token/')
def token():
    return render_template('token.html')


if __name__ == '__main__':
    app.run()
