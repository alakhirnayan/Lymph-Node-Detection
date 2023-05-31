import pydicom 
import matplotlib.pyplot as plt 
import scipy.misc 
import pandas as pd
import numpy as np
import os 
import imageio
from skimage.transform import resize

def Dcm2jpg(file_path):
  #Get all picture names
  c = []
  names =  os.listdir(file_path)
  #Separate the file names in the folder from the. DCM following them
  for name in names:
    index = name.rfind('.')
    name = name[:index]
    c.append(name)
 
  for files in c :
    picture_path = "/home/al-akhir/Music/dcm_to_jpg/i/"+files+".dcm"
    out_path = "/home/al-akhir/Music/dcm_to_jpg/img/"+files+".jpg" 
    ds = pydicom.read_file(picture_path)
    img =  ds.pixel_array # extracting image information
    imageio.imwrite(out_path,img) 
  
  print('all is changed')
      
Dcm2jpg('/home/al-akhir/Music/dcm_to_jpg/i')

