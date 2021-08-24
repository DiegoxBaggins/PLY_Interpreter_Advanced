from flask import Flask, render_template, url_for, redirect

app = Flask(__name__)


@app.route('/')
def slash():  # put application's code here
    return redirect(url_for('home'))


@app.route('/home')
def home():  # put application's code here
    return render_template('index.html')


@app.route('/analisis')
def analisis():  # put application's code here
    return render_template('analisis.html')


@app.route('/reports')
def reports():  # put application's code here
    return render_template('reports.html')


if __name__ == '__main__':
    app.run()
