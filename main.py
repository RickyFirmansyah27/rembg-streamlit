from rembg import remove
from PIL import Image
from matplotlib import pyplot as plt
import streamlit as st
import os



def BGbred():
    old_name = file.name
    new_name = "rm.jpg"
    os.rename(old_name, new_name)
    image = Image.open('rm.jpg')
    output = remove_background(image, color='red')
    st.image(image)
  
  
    
if __name__=="__main__":
   
    st.sidebar.subheader('Upload Image')
    file = st.sidebar.file_uploader(label='Pilih Gambar', type=('jpg'))
      
    if file is not None:
        st.sidebar.write('File Uploaded')
        st.write('Program API REMBG')
        BGbred()
            
 
           
 
   
   







                                                                                                   
