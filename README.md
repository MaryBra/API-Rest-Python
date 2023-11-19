# API-Rest-Python

Esse código é um exemplo de uma aplicação web simples que utiliza um modelo de Machine Learning para fazer previsões sobre a ocorrencia de diabetes com base em dados fornecidos pelo usuario. A aplicação é construida usando o framework Flask para o backend e HTML com Bootstrap para o frontend. 

 

Importacao de bibliotecas para o funcionamento da API 

Flask: Framework web em Python. 

Request: permite acessar dados enviados com a solicitacao HTTP 

Jsonify: converte objetos Python em JSON. 

CORS: permite requisicoes entre dominios diferentes 

RandomForestClassifier do Scikit-Learn: implementa um classificador de floresta aleatória. 

Joblib(Recomendado pelo professor): usado para carregar o modelo treinado  

Numpy: Biblioteca para manipulação de arrays. 

 

Observações Gerais 

O modelo treinado ('diabetes_model.joblib') deve estar presente no mesmo diretorio que o script Flask 

A pagina HTML usa o jQuery e o Popper.js para o Bootstrap. 

Certifique-se de ter todas as dependencias instaladas usando pip install Flask, flask-cors, scikit-learn, joblib  e numpy 

Foi alocado também um arquivo .csv, uma tabela de um dataset parecido do Kaggle, que utilizamos os dados dela apenas para fazer testes. 

Execução do Código  

Execute o script Python (app.py) para iniciar o servidor Flask. 

Abra o arquivo HTML em um navegador 

Insira os dados no formato especificado e clique no botão "Predict" 

A previsão ou mensagens de erro serão exibidas na página. 
