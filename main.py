from rembg import remove
from PIL import Image
from matplotlib import pyplot as plt
import streamlit

def main():
    input = Image.open(file)
    output_path = 'output.png'
    output = remove(input)
    plt.imshow(output_path)
    plt.show()
  
    
if __name__=="__main__":
   
    sidebar.subheader('Upload Image')
    file = sidebar.file_uploader(label='Pilih Gambar', type=('jpg'))
      
    if file is not None:
        sidebar.write('File Uploaded')
        try:
           main()
            
        except Exception as e:
            print(e)
           
 
   
   







                                                                                                   
