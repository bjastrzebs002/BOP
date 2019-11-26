from RequestHandler import RequestHandler
from PrepareData import PrepareData
from ModelData import ModelData
from keras.models import load_model
import os


class Bop:
    def __init__(self, base, currency):
        self.base = base
        self.currency = currency
        self.request_handler = RequestHandler(self.base, self.currency)
        self.prepare_data = PrepareData(currency)
        self.single_prediction_data = ModelData.data_for_prediction(self.prepare_data.single_dict_prepare(
                                                                self.request_handler.get_100daysback_data()))

    def predict_tomorrow_option(self):
        if "model_{}_{}.h5".format(self.currency, self.base) in os.listdir('models'):
            model = load_model('models/model_{}_{}.h5'.format(self.currency, self.base))
            prediction = model.predict(self.single_prediction_data).reshape(-1)[0]
        else:
            model = load_model('models/model_{}_{}.h5'.format(self.base, self.currency))
            prediction = 1 - model.predict(self.single_prediction_data).reshape(-1)[0]
        return prediction

