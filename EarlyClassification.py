import pickle
import pandas as pd
import numpy as np
import streamlit as st
import time
import matplotlib.pyplot as plt

df = pd.read_csv('DataSets\Early Classification of Diabetes.csv')

cols = (df.columns[0]).split(';')


def ecpred():
    model = pickle.load(
        open('models\Early_Classification_of_Diabetes.pkl', 'rb'))

    st.title('Early Classification of Diabetes')
    criteria = []

    name = st.text_input('Name')
    age = st.text_input('Age')
    try:
        age = (int(float(age)))
    except:
        st.warning('Expecting a Number')
    criteria.append(age)
    gender = st.radio('Gender', ('M', 'F'))

    if gender == 'M':
        criteria.append(1)
    else:
        criteria.append(0)

    st.text('Select Symoptems')

    for col in cols[2:-1]:
        cb = st.checkbox(f'{col}'.capitalize())
        criteria.append(int(cb))

    if st.button('Predict'):
        try:
            x = np.array(criteria, ndmin=2, dtype=float)
            res = (model.predict(x)[0])

            if res:
                st.info(
                    'Your Symoptems indicates Towards Having Diabetes Soon...'.upper())
            else:
                st.info(
                    'No Symoptems indicating Towards Having Diabetes \U0001f600'.upper())

        except:
            st.warning('Inputs Required!')


ecpred()
