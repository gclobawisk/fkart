from flask import Flask, request, render_template, redirect, jsonify

# CRIANDO O APP
app = Flask(__name__, static_folder = 'assets')


@app.route('/')
def index():
    arq = open("rankingPilotos.txt", encoding="utf-8")
    linhas = arq.readlines()
    array = []
    for linha in linhas:
        linha = linha.strip("\n")
        linha = linha.split("\t")
        array.append(linha)
    return render_template('index.html', array = array)

@app.route('/modelo2')
def modelo2():
    arq = open("rankingPilotos.txt", encoding="utf-8")
    linhas = arq.readlines()
    i = 1
    array = []
    for linha in linhas:
        linha = linha.strip("\n")
        linha = linha.split("\t")
        array.append(linha)
    return render_template('modelo2.html', array = array)

@app.route('/modelo3')
def modelo3():
    arq = open("rankingPilotos.txt", encoding="utf-8")
    linhas = arq.readlines()
    i = 1
    array = []
    for linha in linhas:
        linha = linha.strip("\n")
        linha = linha.split("\t")
        array.append(linha)
    return render_template('modelo3.html', array = array)

if __name__ == '__main__':
    app.run(port=5000, host='0.0.0.0', debug=True,
            threaded=True, use_reloader=True)