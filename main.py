from rembg import remove
from PIL import Image
from matplotlib import pyplot as plt
import streamlit as st

def remBG():
    output = remove(file)
    plt.imshow(output)
    plt.show()

def BGblue():
    image = Image.open(file)
    output = remove_background(image, color='red')
    plt.imshow(output)
    plt.show()

def BGbred():
    
    output = remove_background(file, color='red')
    plt.imshow(output)
    plt.show()
  
    
if __name__=="__main__":
   
    st.sidebar.subheader('Upload Image')
    file = st.sidebar.file_uploader(label='Pilih Gambar', type=('jpg'))
      
    if file is not None:
        st.sidebar.write('File Uploaded')
        try:
           remBG()
            
        except Exception as e:
            print(e)
           
 
   
   







                                                                                                   
