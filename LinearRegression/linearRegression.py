from flask import Flask, request, render_template
import pickle
import numpy as np

app = Flask(__name__)

# Load trained model
with open("boston_housing.pkl", "rb") as file:
    model = pickle.load(file)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get Features from form
        CRIM = float(request.form['CRIM'])
        ZN = float(request.form['ZN'])
        INDUS = float(request.form['INDUS'])
        CHAS = float(request.form['CHAS'])
        NOX = float(request.form['NOX'])
        RM = float(request.form['RM'])
        AGE = float(request.form['AGE'])
        DIS = float(request.form['DIS'])
        RAD = float(request.form['RAD'])
        TAX = float(request.form['TAX'])
        PTRATIO = float(request.form['PTRATIO'])
        B = float(request.form['B'])
        LSTAT = float(request.form['LSTAT'])            
        prediction = model.predict([[CRIM, ZN, INDUS, CHAS, NOX, RM, AGE, DIS, RAD, TAX, PTRATIO, B, LSTAT]])  # Predict house price

        return render_template('index.html',
                               prediction_text=f'Predicted House Price: ${prediction[0]:.2f}')
    except Exception as e:
        return render_template('index.html', prediction_text=f'Error: {str(e)}')

if __name__ == "__main__":
    app.run(debug=True)