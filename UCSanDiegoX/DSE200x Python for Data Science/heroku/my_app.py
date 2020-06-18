#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import streamlit as st
import pandas as pd
import pickle

# some errors without this two lines
import keras.backend.tensorflow_backend as tb
tb._SYMBOLIC_SCOPE.value = True

st.write("""
# Credit Card Fraud Detection deployed using streamlit
This app does credit card fraud detection but all the input features are mirrored/all-the-same for simplicity and we see that when all the features are close to zero. The transaction is determined as fraudulent as it makes no sense for all the features to be close to zero.
""")

st.sidebar.header('User Input Parameters')

def simple_neural_network():
    clf = Sequential()
    clf.add(Dense(units=16,input_dim = 29, activation = 'relu'))
    clf.add(Dense(units=24, activation = 'relu'))
    clf.add(Dropout(0.5))
    clf.add(Dense(units=20, activation = 'relu'))
    clf.add(Dense(units=24, activation = 'relu'))
    clf.add(Dense(units=1, activation = 'sigmoid'))
    
    clf.compile(optimizer='adam',loss='binary_crossentropy',metrics=['accuracy'])
      
    return clf

def user_input_features():
    V1 = st.sidebar.slider('All Features V1-V28, normAmount', 0.0, 1.0, 0.5)
    data = {'V1': V1,
           'V2': V1,
           'V3': V1,
           'V4': V1,
           'V5': V1,
           'V6': V1,
           'V7': V1,
           'V8': V1,
           'V9': V1,
           'V10': V1,
           'V11': V1,
           'V12': V1,
           'V13': V1,
           'V14': V1,
           'V15': V1,
           'V16': V1,
           'V17': V1,
           'V18': V1,
           'V19': V1,
           'V20': V1,
           'V21': V1,
           'V22': V1,
           'V23': V1,
           'V24': V1,
           'V25': V1,
           'V26': V1,
           'V27': V1,
           'V28': V1,
           'normAmount': V1
           }

    features= pd.DataFrame(data, index=[0])
    return features
df =  user_input_features()
st.subheader('User Input Parameters')
st.write(df)

filename = 'Neural_network_OS'
model = pickle.load(open(filename,'rb'))
pred = model.predict(df)
st.subheader('Prediction - 1 denotes frauduluent transaction, 0 denotes non-fraudulent transaction')
st.write(pred)
