from rembg import remove
from PIL import Image
from matplotlib import pyplot as plt
import streamlit as st

def tampil(img):
    plt.imshow(img)
    plt.show()
    st.plt.show()
  
    
if __name__=="__main__":
   
    st.sidebar.subheader('Upload Image')
    img = st.sidebar.file_uploader(label='Pilih Gambar', type=('jpg'))
      
    if img is not None:
        st.sidebar.write('File Uploaded')
        try:
           tampil(img)
            
        except Exception as e:
            print(e)
           
 
   
   







                                                                                                   
