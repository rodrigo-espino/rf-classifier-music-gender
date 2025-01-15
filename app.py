from flask import Flask, request, jsonify
import pickle
import numpy as np

app = Flask(__name__)

# Load the trained model
filename = 'rf_model.pkl'
with open(filename, 'rb') as file:
    model = pickle.load(file)

# Define the classes (you'll need to replace these with your actual classes)
classes = np.array(['Banda', 'Mariachi', 'Mexicana Contemporánea', 'Norteño'])

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

if __name__ == '__main__':
    app.run(debug=True)