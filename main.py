
#Import libraries
import streamlit as st
import numpy as np
import cv2
from rembg import remove
from  PIL import Image, ImageEnhance

from io import BytesIO
buf = BytesIO()

#Create two columns with different width
col1, col2 = st.columns( [0.8, 0.2])
with col1:               # To display the header text using css style
    st.markdown(""" <style> .font {
    font-size:35px ; font-family: 'Cooper Black'; color: #FF9633;} 
    </style> """, unsafe_allow_html=True)
    st.markdown('<p class="font">Upload your photo here...</p>', unsafe_allow_html=True)
    
#Add a header and expander in side bar
st.sidebar.markdown('<p class="font">Aplikasi Konversi Foto</p>', unsafe_allow_html=True)
with st.sidebar.expander("About the App"):
     st.write("""
        Konversi fotomu dengan beberapa filter di bawah  \n  \nCreated by Ricky - project Pengolahan Citra Digital
     """)
uploaded_file = st.file_uploader("", type=['jpg','png','jpeg'])


if uploaded_file is not None:
    image = Image.open(uploaded_file)
    
    col1, col2 = st.columns( [0.5, 0.5])
    with col1:
        st.markdown('<p style="text-align: center;">Before</p>',unsafe_allow_html=True)
        st.image(image,width=300)  

    with col2:     
        st.markdown('<p style="text-align: center;">After</p>',unsafe_allow_html=True)
        filter = st.sidebar.radio('Covert your photo to:', ['Original','Gray Image','Black and White', 'Delete Background', 'Pencil Sketch', 'Blur Effect'])
        if filter == 'Gray Image':
                converted_img = np.array(image.convert('RGB'))
                gray_scale = cv2.cvtColor(converted_img, cv2.COLOR_RGB2GRAY)
                st.image(gray_scale, width=300)
        elif filter == 'Black and White':
                converted_img = np.array(image.convert('RGB'))
                gray_scale = cv2.cvtColor(converted_img, cv2.COLOR_RGB2GRAY)
                slider = st.sidebar.slider('Adjust the intensity', 1, 255, 127, step=1)
                (thresh, blackAndWhiteImage) = cv2.threshold(gray_scale, slider, 255, cv2.THRESH_BINARY)
                st.image(blackAndWhiteImage, width=300)
        elif filter == 'Delete Background':
                converted_img = np.array(image.convert('RGB'))
                input_path = converted_img
                output_path = 'hasil.png'
                input = Image.open(uploaded_file)
                output = remove(input)
                converted_img = np.array(output.convert('RGB'))
                st.image(output, width=300)
                output.save('Hasil.jpg')
                output.save(buf, format="JPEG")
                byte_im = buf.getvalue()
                st.download_button(label="Download Images", data=byte_im, file_name='Hasil.jpg')
                
         
        elif filter == 'Pencil Sketch':
                converted_img = np.array(image.convert('RGB')) 
                gray_scale = cv2.cvtColor(converted_img, cv2.COLOR_RGB2GRAY)
                inv_gray = 255 - gray_scale
                slider = st.sidebar.slider('Adjust the intensity', 25, 255, 125, step=2)
                blur_image = cv2.GaussianBlur(inv_gray, (slider,slider), 0, 0)
                sketch = cv2.divide(gray_scale, 255 - blur_image, scale=256)
                st.image(sketch, width=300) 
                
        elif filter == 'Blur Effect':
                converted_img = np.array(image.convert('RGB'))
                slider = st.sidebar.slider('Adjust the intensity', 5, 81, 33, step=2)
                converted_img = cv2.cvtColor(converted_img, cv2.COLOR_RGB2BGR)
                blur_image = cv2.GaussianBlur(converted_img, (slider,slider), 0, 0)
                st.image(blur_image, channels='BGR', width=300) 
                image.save(buf, format="JPEG")
                byte_im = buf.getvalue()
        else: 
                st.image(image, width=300)
        
       
        

        

