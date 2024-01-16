from ImageCaptionModel_1 import img2text
from ImageCaptionModel_2 import predict_step
from arduino import connect2arduino
import argparse

def Img2arduino(str):
    connect2arduino(str)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Process a image file to a gcode file\nplease enter (1)img file name (2)model mode")
    parser.add_argument("string_param", type=str, help="name")

    args = parser.parse_args()
    Img2arduino(args.string_param)