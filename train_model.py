from sklearn.ensemble import RandomForestClassifier
import joblib

def train_model(X_train, y_train):
    # Define, compila e treina o modelo
    model = RandomForestClassifier()
    model.fit(X_train, y_train)

    # Salva o modelo treinado
    joblib.dump(model, 'diabetes_model.joblib')

