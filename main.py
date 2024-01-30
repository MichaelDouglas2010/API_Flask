#Apos instalar a biblioteca Flask importo o Flask para o programa, Importo make response que formata como uma resposta e jsonify que formata em json , request 
from flask import Flask, make_response, jsonify, request
from flask.globals import request
# Importando do banco de dados a lista de carros
from bd import Carros

# Declaro uma variavel Flask e atribuo o nome default que for utilizado (instancio)
app = Flask(__name__)
#Configura o Json em ordem normal não por ordem alfabetica
app.config['JSON SORTS KEYS'] = False

#Marcação da função com um decorreitor para demostrar ao flask como rota 
#Função chama lista de carros
@app.route('/carros', methods =['GET'])
def get_carros():
    return make_response(
        jsonify(
            Mensagem = 'Lista de Carros',
            dados = Carros
            )
    ) 

# Decorreitor função para postar dados no banco de dados
#Função que manda os dados no formato Json
@app.route('/carros', methods = ['POST'])
def create_carro():
    carro = request.json
    Carros.append(carro)
    return make_response(
        jsonify(carro)
    )
@app.route('/texto')
def index():
    return '<h1>Bem vindo</h1>'

# Inicia o servidor quando não assignamos uma porta ele abre na Porta 5000 como padrão
if __name__ == '__main__':
    app.run(host = 'localhost', port = 8088, debug = True)




