from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hansel alarm button'

@app.route('/form/')
def hello(name=None):
    return render_template('form.html')

if __name__ == '__main__':
    app.run()
