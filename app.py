import streamlit as st
import pickle
import pandas as pd
import numpy as np
from streamlit_option_menu import option_menu

#creating a sidebar with different pages to navigate  
#with st.sidebar: #if you want a side bar 
selected = option_menu(
       menu_title = None ,#"Main Menu",
       options = ["Home","Model","About"],
       icons = ["house","robot","person"],
       menu_icon = "menu-button",
       default_index = 0,
       orientation = "horizontal",  #to make the menubar horizontal 
    )
    
if selected == "Home":
    #st.title('Home')
    with st.container():
        st.title('Energy Efficiency calculator')
        st.subheader('By Group 4 :wave:')
    
    with st.container():
        st.title('What is Energy Efficiency:information_source:')
        st.write(' problem ststement ')
        st.subheader('This is a sample Dataset:')
        df = pd.read_csv("energy_efficiency_data.csv")
        st.write(df)


if selected == "Model":
    #st.title('Model')
    st.title('Energy Efficiency')
    st.subheader('Enter the details')
 
    model = st.selectbox('choose a model',
      ('Decision tree classification', 'Random forest classification','Linear regression'))

    if model =='Decision tree classification':
       m = pickle.load(open('decisiontree.sav', 'rb'))
    elif model =='Random forest classification':
       m = pickle.load(open('randomforest.sav', 'rb'))
    else:
       m = pickle.load(open('linearregression.sav', 'rb'))


    def ef(input_data):
       na = np.asarray(input_data)
       d = na.reshape(1, -1)

       prediction = m.predict(d)
       print(prediction)


    def main():
       
     Relative_Compactness = st.text_input('Relative_Compactness')

     Surface_Area = st.text_input('Relative_Compactness') 
     Wall_Area = st.text_input('Wall_Area')
     Roof_Area = st.text_input('Roof_Area')
     Overall_Height = st.text_input('Overall_Height')
     Orientation = st.text_input('Orientation')
     Glazing_Area = st.text_input('Glazing_Area')
     Glazing_Area_Distribution= st.text_input('Glazing_Area_Distribution')

     cc = ''

     if st.button('Get Results'):
       cc = ef([Relative_Compactness, Surface_Area, Wall_Area, Roof_Area, Overall_Height, Orientation, Glazing_Area, Glazing_Area_Distribution, Heating_Load, Cooling_Load])

       st.success(cc)

    if __name__ == '__main__':
      main()

if selected == "About":
    #st.title('About')
    st.title('Hi, Group 4 here :smiley:')