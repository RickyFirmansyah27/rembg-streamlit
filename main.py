from rembg import remove
from PIL import Image
from matplotlib import pyplot as plt
import streamlit as st
import os



def BGbred():
    output = rembg.remove_background(file.name, color='red')
    st.image(image)
  
  
    
if __name__=="__main__":
   
    st.sidebar.subheader('Upload Image')
    file = st.sidebar.file_uploader(label='Pilih Gambar', type=('jpg'))
      
    if file is not None:
        st.sidebar.write('File Uploaded')
        st.write('Program API REMBG')
        BGbred()
            
 
           
 
   
   







                                                                                                   
