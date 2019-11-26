from ModelData import ModelData
from keras.models import Sequential
from keras.layers import LSTM, Dense, Dropout, TimeDistributed
import logging

logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)


class ModelBuilder:

    def __init__(self, prepared_data):
        self.model_data = ModelData(prepared_data)
        self.model = self.get_model()

    @staticmethod
    def get_model():
        logging.info("Creating model..")
        model = Sequential()
        model.add(LSTM(500, input_shape=(1, 100,), return_sequences=True))
        model.add(LSTM(250, return_sequences=True))
        model.add(LSTM(100, return_sequences=True))
        model.add(Dropout(0.5))
        model.add(TimeDistributed(Dense(1, activation="sigmoid")))

        model.compile(optimizer="adam", loss="mean_squared_error", metrics=['accuracy'])
        return model

    def train_model(self, batch_size=16, epochs=20):
        logging.info("Training model..")
        self.model.fit(self.model_data.get_train()[0], self.model_data.get_train()[1],
                       batch_size=batch_size, epochs=epochs,
                       validation_data=self.model_data.get_test())

    def save_model(self, filename):
        self.model.save("models/{}.h5".format(filename))
        logging.info("Model saved to models/{}.h5".format(filename))

    def get_trained_model(self):
        return self.model
