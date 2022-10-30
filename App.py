import streamlit as st
from joblib import dump, load
import numpy as np
import pandas as pd


def main():
       
    st.title("Major Project")
    html_temp = """
    <div style="background-color:teal ;padding:20px">
    </div>
    
    """
    
    picture = st.camera_input("Take a picture")

    if picture:
        st.image(picture)


    
    
if __name__=='__main__':
    main()