from __future__ import print_function

import os
import StringIO
import flask

import tensorflow as tf
import numpy as np
import pandas as pd

from keras import backend as K
from keras.models import load_model
from sklearn.preprocessing import StandardScaler

from sklearn.preprocessing import LabelEncoder, OneHotEncoder

prefix = '/opt/ml/'
model_path = os.path.join(prefix, 'model')


# A singleton for holding the model.
class ScoringService(object):
    model = None

    @classmethod
    def get_model(cls):
        if cls.model is None:
            cls.model = load_model(os.path.join(model_path, 'lstm.h5'))
        return cls.model

    @classmethod
    def predict(cls, input):
        sess = K.get_session()
        with sess.graph.as_default():
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
    data = flask.request.data.decode('utf-8')
    l = map(int, data.split(","))
    a = np.array(l).reshape(1,1,len(l))
    predictions = ScoringService.predict(a)
    p_string = ",".join(map(str, predictions.tolist()[0][0]))
    return flask.Response(response=bytearray(p_string), status=200)