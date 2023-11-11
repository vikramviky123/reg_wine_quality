from flask import Flask, render_template, request
import pandas as pd
import numpy as np
import pickle
from src.wine_reg.a_constants import *
from src.wine_reg.f_utils.common import load_pickle, read_yaml
from pathlib import Path


app = Flask(__name__)

candidates = {}


@app.route('/')
def index():
    return render_template('Intro.html')


@app.route('/data')
def data():
    return render_template('data.html')


@app.route('/eda/univariate')
def univariate():
    return render_template('univariate.html')


@app.route('/eda/bivariate')
def bivariate():
    return render_template('bivariate.html')


@app.route('/model/modelanalysis')
def modelanalysis():
    return render_template('modelanalysis.html')


def convert_to_float(value):
    return float(value) if value is not None and value != '' else None


@app.route('/model/modelplots')
def modelplots():
    return render_template('modelplots.html')


@app.route('/predict', methods=['GET', 'POST'])
def predict():
    try:

        # Retrieve the input data from the form
        fixed_acidity = request.form.get('fixed_acidity')
        volatile_acidity = request.form.get('volatile_acidity')
        citric_acid = request.form.get('citric_acid')
        residual_sugar = request.form.get('residual_sugar')
        chlorides = request.form.get('chlorides')
        free_sulfur_dioxide = request.form.get('free_sulfur_dioxide')
        total_sulfur_dioxide = request.form.get('total_sulfur_dioxide')
        density = request.form.get('density')
        pH = request.form.get('pH')
        sulphates = request.form.get('sulphates')
        alcohol = request.form.get('alcohol')

        # Load the saved list of models using pickle
        best_model_name = 'random_forest'
        pickle_file_path = Path(
            "artifacts/model_trainer/trained_models.joblib")
        loaded_models = load_pickle(pickle_file_path)

        rf_models = loaded_models[best_model_name]

        # Convert form data to float
        def convert_to_float(value):
            return float(value) if value is not None and value != '' else None

        fixed_acidity = convert_to_float(fixed_acidity)
        volatile_acidity = convert_to_float(volatile_acidity)
        citric_acid = convert_to_float(citric_acid)
        residual_sugar = convert_to_float(residual_sugar)
        chlorides = convert_to_float(chlorides)
        free_sulfur_dioxide = convert_to_float(free_sulfur_dioxide)
        total_sulfur_dioxide = convert_to_float(total_sulfur_dioxide)
        density = convert_to_float(density)
        pH = convert_to_float(pH)
        sulphates = convert_to_float(sulphates)
        alcohol = convert_to_float(alcohol)

        # Create a dictionary from the form data
        data = {
            'fixed_acidity': [fixed_acidity],
            'volatile_acidity': [volatile_acidity],
            'citric_acid': [citric_acid],
            'residual_sugar': [residual_sugar],
            'chlorides': [chlorides],
            'free_sulfur_dioxide': [free_sulfur_dioxide],
            'total_sulfur_dioxide': [total_sulfur_dioxide],
            'density': [density],
            'pH': [pH],
            'sulphates': [sulphates],
            'alcohol': [alcohol],
        }

        print(data)
        df = pd.DataFrame(data)
        print(df)

        preds = [model.predict(np.array(df)) for model in rf_models]
        print(preds)
        preds_mean = sum(preds) / len(preds)
        print(preds_mean)

        return render_template('predict.html', predicted_wine_quality=preds_mean)

    except Exception as e:
        return render_template('predict.html', error_message=str(e))


@app.route('/form')
def show_form():
    return render_template('predict.html', preds_final=None, error_message=None)


if __name__ == '__main__':
    app.run(debug=True)
