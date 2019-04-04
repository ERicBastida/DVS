# Here we have to import library of
# from pynq import Overlay
# https://pynq.readthedocs.io/en/v2.0/overlay_design_methodology/overlay_tutorial.html

from .models import *
import time
class FileProcessor:

    def work(self,number_function,path_file_1, path_file_2):

        print("Files to process :  ", path_file_1, "  ,  ", path_file_2 , ". With function : ", number_function)

        # YOURS IMPLEMENTED FUNCTION FROM FPGA
        #           * * *

        # new_file_name = #You must put the path of new file here, to be illustrate in the web page

        # if(number_function == "1"):
        #     file_name ='media/images/MultiVidOut.mp4'
        # elif (number_function == "2"):
        #     file_name= 'media/images/PillOut.mp4'
        # else:
        #     file_name = 'media/images/IntestineOut.mp4'

        file_name = 'media/images/processed_file.mp4'
        return file_name

