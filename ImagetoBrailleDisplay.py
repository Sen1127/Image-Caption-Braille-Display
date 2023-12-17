from ImageCaptionModel_1 import img2text
from ImageCaptionModel_2 import predict_step
from arduino import connect2arduino
import argparse

def Img2arduino(fname, model):
    if model == 1:
        description = img2text(fname)
        print(description)
        connect2arduino(description)
    elif model == 2:
        descriptions = predict_step([f'{fname}.png'])
        for description in descriptions:
            print(description)
            connect2arduino(description)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Process a image file to a gcode file\nplease enter (1)img file name (2)model mode")
    parser.add_argument("string_param", type=str, help="image file name")
    parser.add_argument("int_param", type=int, help="model mode")

    args = parser.parse_args()
    Img2arduino(args.string_param, args.int_param)