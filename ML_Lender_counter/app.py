import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)

# Load the trained Support Vector Machine (SVM) model
with open('model.pkl', 'rb') as file:
    model = pickle.load(file)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    lender_count = int(request.form['lender_count'])
    repayment_term = int(request.form['repayment_term'])
    sector = request.form['sector']
    location_country_code = request.form['location_country_code']

    # Convert sector and location_country_code to one-hot encoded format
    sectors = ['Arts', 'Clothing', 'Construction', 'Education', 'Food', 'Health', 'Housing', 'Manufacturing', 'Personal Use', 'Retail', 'Services', 'Transportation', 'Wholesale']
    location_country_codes = ['BI', 'BJ', 'BW', 'CD', 'CG', 'CI', 'CM', 'EG', 'GH', 'KE', 'LR', 'LS', 'MG', 'ML', 'MR', 'MW', 'MZ', 'NG', 'RW', 'SL', 'SN', 'SO', 'SS', 'TG', 'TZ', 'UG', 'ZA', 'ZM', 'ZW']

    sector_values = [1 if sector == s else 0 for s in sectors]
    location_country_code_values = [1 if location_country_code == loc else 0 for loc in location_country_codes]

    # Combine the features into a single array with default values for missing features
    features = [lender_count, repayment_term] + sector_values + location_country_code_values + [0, 0]

    final_features = [np.array(features)]

    # Make the prediction using the model
    prediction = model.predict(final_features)
    output = round(prediction[0], 2)

    return render_template('index.html', prediction_text='Predicted Loan Amount: ${}'.format(output))

if __name__ == "__main__":
    app.run(debug=True)
