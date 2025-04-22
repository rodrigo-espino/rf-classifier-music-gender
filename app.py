from flask import Flask, request, jsonify
import pickle
from flask_cors import CORS
import numpy as np

app = Flask(__name__)
CORS(app)

# Load the trained model
filename = 'rf_model.pkl'
with open(filename, 'rb') as file:
    model = pickle.load(file)

# Define the classes (you'll need to replace these with your actual classes)
classes = np.array(['Banda', 'Bolero', 'Duranguense', 'Mariachi',
                    'Mexicana Contemporánea', 'Norteño', 'Rock', 'Tropical'])

##
@app.route('/predict', methods=['POST'])
def predict():
    print("l")
    try:
        data = request.get_json()
        print(data)
        input_data = np.array(data['input']).reshape(1,-1) 
        print(input_data)
        prediction = model.predict(input_data)
        predicted_class = classes[prediction][0]
        return jsonify({'prediction': predicted_class})
    except Exception as e:
        return jsonify({'error': str(e)})

@app.route('/ok', methods=['GET'])
def return_okey():
    return jsonify({'msg':'Ok'})

if __name__ == '__main__':
    app.run(debug=True)
