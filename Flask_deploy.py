import streamlit as st
from joblib import dump, load
import numpy as np

log_model = load('Multi_class_log_model.joblib')

def classify(sepal_length, sepal_width, petal_length, petal_width):
    inputs=np.array([[sepal_length, sepal_width, petal_length, petal_width]]).reshape(1, -1)
    prediction=log_model.predict(inputs)
    pred = '{}'.format(prediction)
    return(pred)


    
def main():
    st.title("Major Project")
    html_temp = """
    <div style="background-color:teal ;padding:10px">
    <h2 style="color:white;text-align:center;">Iris Classification</h2>
    </div>
    """
    
    

    picture = st.camera_input("Take a picture")

    if picture:
        st.image(picture)
   
     
if __name__=='__main__':
    main()
