from __future__ import print_function

import os
import StringIO
import flask

import tensorflow as tf
import numpy as np
import pandas as pd

from sklearn.preprocessing import StandardScaler

from sklearn.preprocessing import LabelEncoder, OneHotEncoder

import StringIO
import pickle

prefix = '/opt/ml/'
model_path = os.path.join(prefix, 'model')

# A singleton for holding the model.
class ScoringService(object):
    model = None

    @classmethod
    def get_model(cls):
        if cls.model is None:
            cls.model = pickle.load(open(os.path.join(model_path, 'kmeans.sav'), 'rb'))
        return cls.model

    @classmethod
    def predict(cls, input):
        clf = cls.get_model()
        return clf.predict(input)


app = flask.Flask(__name__)

@app.route('/ping', methods=['GET'])
def ping():
    health = ScoringService.get_model() is not None
    status = 200 if health else 404
    return flask.Response(
        response='\n',
        status=status,
        mimetype='application/json')


@app.route('/invocations', methods=['POST'])
def transformation():
    df = None

    if flask.request.content_type == 'text/csv':
        csv_string = flask.request.data.decode('utf-8')
        s = StringIO.StringIO(csv_string)
        df = pd.read_csv(s)

    else:
        return flask.Response(
            response='This predictor only supports CSV data',
            status=415,
            mimetype='text/plain')

    predictions = ScoringService.predict(df.values)

    out = StringIO.StringIO()
    out_df = pd.DataFrame(predictions)
    result_df = pd.concat([df, out_df], axis=1, sort=False)
    result_df.to_csv(out, header=False, index=False)
    result = out.getvalue()

    return flask.Response(response=result, status=200, mimetype='text/csv')
