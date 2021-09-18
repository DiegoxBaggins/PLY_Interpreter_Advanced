import sys
import json
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
        resultado = procesoPrincipal(codigo)
        return render_template('analisis.html', text1=codigo, text2=resultado)
    else:
        return render_template('analisis.html', text1="escribe aqui tu codigo", text2="Output Console")


@app.route('/reports')
def reports():  # put application's code here
    with open('errors.json') as json_file:
        errores = json.load(json_file)
    with open('simbols.json') as json_file:
        simbols = json.load(json_file)
    return render_template('reports.html', errores=errores, simbols=simbols)


if __name__ == '__main__':
    app.run()


def procesoPrincipal(codigo):
    string = ""
    f = open("./output.txt", "w")
    f.write("")
    f.close()
    sys.setrecursionlimit(10 ** 4)
    newEnv = Entorno(None, "global")
    ast = parse(codigo)
    for instr in ast:
        instr.execute(newEnv)
    errores = newEnv.errors
    for error in errores:
        string += error[1] + " en linea: " + str(error[2]) + " en columna: " + str(error[3]) + "\n"
    f = open("./output.txt", "r")
    string += f.read()
    f.close()
    with open('errors.json', 'w') as outfile:
        json.dump(errores, outfile)
    variables = newEnv.simbols
    with open('simbols.json', 'w') as outfile:
        json.dump(variables, outfile)
    return string
