from flask import Flask, request, jsonify
from flask_cors import CORS
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_diabetes
import joblib
import numpy as np  

# Carrega o conjunto de dados de diabetes do scikit-learn
data = load_diabetes()
X_train, X_test, y_train, y_test = train_test_split(data.data, data.target, test_size=0.2, random_state=42)

# Inicializa o modelo RandomForest
model = RandomForestClassifier()

# Treina o modelo com os dados de treinamento
model.fit(X_train, y_train)
joblib.dump(model, 'diabetes_model.joblib')

#Inicializa o aplicativo Flask
app = Flask(__name__)
CORS(app) #Habilita o CORS para permitir solicitacoes de diferentes origens

#Carrega o modelo salvo
loaded_model = joblib.load('diabetes_model.joblib')

#Define uma rota para receber solicitaÃ§Ãµes POST para fazer previsÃµes
@app.route('/predict', methods=['POST'])
def predict(): #recebe dados do front, adiciona um atributo ficticio e realiza a predicao usando o modelo carregado
    try:
        data = request.json['data']
        print(f"Received data: {data}") #imprime no terminal os dados recebidos

        # Adiciona um atributo fictÃ­cio (dummy attribute) com o valor zero
        data_with_dummy = np.append(data, 0)

        # Realiza a previsÃ£o com os dados modificados
        prediction = loaded_model.predict([data_with_dummy])[0]

        return jsonify({'prediction': (prediction)})

    except Exception as e:
        print(f"Error: {str(e)}")
        return jsonify({'error': str(e)})

#Inicia o servidor Flask se o script for executado diretamente
if __name__ == '__main__':
    app.run()
