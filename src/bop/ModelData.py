from sklearn.model_selection import train_test_split
import numpy as np
import logging

logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)


class ModelData:
    def __init__(self, prepared_data):
        logging.info("Preparing data for model..")
        input_data, output_data = prepared_data
        self.x_train, self.x_test, self.y_train, self.y_test = self.generate_train_test(input_data, output_data)

    def get_train(self):
        return self.x_train, self.y_train

    def get_test(self):
        return self.x_test, self.y_test

    @staticmethod
    def generate_train_test(x, y):
        x = [np.float32(a).reshape(100, 1) for a in x]
        x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)
        x_train = np.asarray(x_train).reshape(-1, 1, 100)
        y_train = np.asarray(y_train).reshape(-1, 1, 1)
        x_test = np.asarray(x_test).reshape(-1, 1, 100)
        y_test = np.asarray(y_test).reshape(-1, 1, 1)
        return x_train, x_test, y_train, y_test

    @staticmethod
    def data_for_prediction(data):
        return np.float32(data).reshape(-1, 1, 100)


