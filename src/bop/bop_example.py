from Bop import Bop


if __name__ == "__main__":
    bop = Bop('PLN', "USD")
    pred = bop.predict_tomorrow_option()
    print("{}% for higher,  {}% for lower".format(round(pred*100, 3), round((100 - pred*100), 3)))

