from flask import Flask, request, jsonify
from flask_cors import CORS
from sklearn.ensemble import RandomForestClassifier
import joblib
import numpy as np  

#Inicializa o aplicativo Flask
app = Flask(__name__)
CORS(app) #Habilita o CORS para permitir solicitacoes de diferentes origens

#Carrega o modelo salvo
loaded_model = joblib.load('diabetes_model.joblib')

#Define uma rota para receber solicitações POST para fazer previsões
@app.route('/predict', methods=['POST'])
def predict(): #recebe dados do front, adiciona um atributo ficticio e realiza a predicao usando o modelo carregado
    try:
        data = request.json['data']
        print(f"Received data: {data}") #imprime no terminal os dados recebidos

        # Adiciona um atributo fictício (dummy attribute) com o valor zero
        data_with_dummy = np.append(data, 0)

        # Realiza a previsão com os dados modificados
        prediction = loaded_model.predict([data_with_dummy])[0]

        return jsonify({'prediction': (prediction)})

    except Exception as e:
        print(f"Error: {str(e)}")
        return jsonify({'error': str(e)})

#Inicia o servidor Flask se o script for executado diretamente
if __name__ == '__main__':
    app.run()
