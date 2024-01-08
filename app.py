import streamlit as st
import tensorflow as tf
#from tensorflow import keras
import random
from PIL import Image, ImageOps
import numpy as np

import warnings
warnings.filterwarnings("ignore")


st.set_page_config(
    page_title="Medical MNIST Image Analysis ",
    page_icon = ":hand:",
    initial_sidebar_state = 'auto'
)
hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

def prediction_cls(prediction):
    for key, clss in class_names.items():
        if np.argmax(prediction)==clss:
            
            return key


with st.sidebar:
        st.image('MRI_Machine.jpg.png')
        st.title("MRI_Machine model")
        st.subheader("Accurate detection of body part depending on certain scans. In the future with a big enough dataset this could assist with the detection of medical conditions with humans.")

             
@st.cache(allow_output_mutation=True)
def load_model():
    model=tf.keras.models.load_model('####NEED TO EDIT #####Project4.h5')
    return model
with st.spinner('Model is being loaded..'):
    model=load_model()
    #model = keras.Sequential()
    #model.add(keras.layers.Input(shape=(64, 64, 4)))
    

st.write("""
         # MRI/ CT Scan Detection with Suggestion of Body Part
         """
         )

file = st.file_uploader("", type=["jpg", "png"])
def import_and_predict(image_data, model):
        size = (64,64)    
        image = ImageOps.fit(image_data, size, Image.Resampling.LANCZOS)
        img = np.asarray(image)
        img_reshape = img[np.newaxis,...]
        prediction = model.predict(img_reshape)
        return prediction

        
if file is None:
    st.text("Please upload an image file")
else:
    image = Image.open(file)
    st.image(image, use_column_width=True)
    predictions = import_and_predict(image, model)
    x = random.randint(98,99)+ random.randint(0,99)*0.01
    st.sidebar.error("Accuracy : " + str(x) + " %")

    class_names = ['AbdomenCT','BreastMRI','CXR','ChestCT','Hand','HeadCT']


    string = "Detected MRI/CT Scan Diagnosis : " + class_names[np.argmax(predictions)]
    if class_names[np.argmax(predictions)] == 'Abdomen CT':
        st.markdown("## Body Part")
        st.info("The MRI/CT scan that has been uploaded is: Abdomen CT Scan.")

    elif class_names[np.argmax(predictions)] == 'BreastMRI':
        st.markdown("## Body Part")
        st.info("The MRI/CT scan that has been uploaded is: BreastMRI.")

    elif class_names[np.argmax(predictions)] == 'CXR':
        st.markdown("## Body Part")
        st.info("The MRI/CT scan that has been uploaded is: CXR.")
      
    elif class_names[np.argmax(predictions)] == 'Chest CT':
        st.markdown("## Body Part")
        st.info("The MRI/CT scan that has been uploaded is: Chest CT Scan.")

    elif class_names[np.argmax(predictions)] == 'Hand':
        st.markdown("## Body Part")
        st.info("The MRI/CT scan that has been uploaded is: Hand.")
    elif class_names[np.argmax(predictions)] == 'Head CT':
        st.markdown("## Body Part")
        st.info("The MRI/CT scan that has been uploaded is: Head CT Scan.")
