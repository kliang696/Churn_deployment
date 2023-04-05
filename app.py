# importing required libraries
#%%
import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
import xgboost
#%%

app = Flask(__name__) 

model = xgboost.Booster(model_file="xgb_model.bin")

@app.route('/')
def home():
    return render_template('myindex.html')

@app.route('/predict',methods=['POST'])
def predict():

    int_features = [int(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    dmatrix = xgboost.DMatrix(final_features)
    prediction = model.predict(dmatrix)
    
    if prediction <= 0.5:
        output = "No, This Customer won't Churn"
    elif prediction >= 0.5:
        output = "Yes, This Customer will Churn"
    else:
        outpur = 'ERROR!'
    return render_template('myindex.html', prediction_text='🤖🤖: "{}!"'.format(output))


if __name__ == "__main__":
    app.run(debug=True)