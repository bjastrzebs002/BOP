from RequestHandler import RequestHandler
from PrepareData import PrepareData
from ModelBuilder import ModelBuilder
import argparse


def get_args():
    parser = argparse.ArgumentParser("Preparing data and building model")
    parser.add_argument('-f', '--filename', help="Filename for saved keras model - in /models/", type=str)
    parser.add_argument('-b', '--batch_size', help="Batch size for training model", type=int)
    parser.add_argument('-e', "--epochs", help="Number of epochs for training model", type=int)
    return parser.parse_args()


if __name__ == "__main__":
    args = get_args()
    pd = PrepareData(RequestHandler().get_data())
    model_builder = ModelBuilder(pd.prepare())
    model_builder.train_model(args.batch_size, args.epochs)
    model_builder.save_model(args.filename)
