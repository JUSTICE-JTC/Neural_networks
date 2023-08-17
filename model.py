import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline

def load_data(file_path):
    """Load data from a CSV file and return a DataFrame."""
    data = pd.read_csv(file_path)
    return data

def preprocess_data(data):
    """Preprocess data and return feature matrix X and target y."""
    X = data['Birthplace'] + ' ' + data['MilitaryUnit']
    y = data['Name']
    return X, y

def build_model(X, y):
    """Build and train a text classification model."""
    model = make_pipeline(CountVectorizer(), MultinomialNB())
    model.fit(X, y)
    return model

def predict_name(model, input_text):
    """Predict the name based on the input text using the trained model."""
    predicted_name = model.predict([input_text])
    return predicted_name[0]

def main():
    # Load the data
    data_file = 'data.csv'
    data = load_data(data_file)
    
    # Preprocess the data
    X, y = preprocess_data(data)
    
    # Build and train the model
    model = build_model(X, y)
    
    # Sample input text
    input_text = "Chicago 3rd Infantry Division"
    
    # Predict the name
    predicted_name = predict_name(model, input_text)
    print("Predicted Name:", predicted_name)

if __name__ == '__main__':
    main()
