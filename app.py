from flask import Flask, render_template, url_for, redirect, request
from Analyzer.Grammar import parse
from Symbol.Entorno import *

app = Flask(__name__)


@app.route('/')
def slash():  # put application's code here
    return redirect(url_for('home'))


@app.route('/home')
def home():  # put application's code here
    return render_template('index.html')


@app.route('/analisis',  methods=["POST", "GET"])
def analisis():  # put application's code here
    if request.method == "POST":
        dic = request.form
        codigo = dic["txt1"]
        print(codigo)
        f = open("./output.txt", "w")
        f.write("")
        f.close()
        newEnv = Entorno(None)
        ast = parse(codigo)
        for instr in ast:
            instr.execute(newEnv)
        f = open("./output.txt", "r")
        resultado = f.read()
        f.close()
        return render_template('analisis.html', text1=codigo, text2=resultado)
    else:
        return render_template('analisis.html', text1="escribe aqui tu codigo", text2="Output Console")


@app.route('/reports')
def reports():  # put application's code here
    return render_template('reports.html')


if __name__ == '__main__':
    app.run()
