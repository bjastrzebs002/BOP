from RequestHandler import RequestHandler
from PrepareData import PrepareData
from ModelBuilder import ModelBuilder
import logging


def generate_model(c1, c2):
    rh = RequestHandler(c1, c2)
    pd = PrepareData(c2)
    mb = ModelBuilder(pd.prepare(rh.get_data()))
    mb.train_model()
    mb.save_model("model_{}_{}".format(c1, c2))
    logging.info("Model trained and saved for {}/{}".format(c1, c2))


if __name__ == "__main__":
    cur_1 = ["CAD", "EUR", "USD", "CHF", "PLN", "SEK", "GBP"]
    cur_2 = ["CAD", "EUR", "USD", "CHF", "PLN", "SEK", "GBP"]
    for curr_s in cur_1:
        for curr_f in cur_2:
            if curr_s != curr_f:
                generate_model(curr_s, curr_f)
