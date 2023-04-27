import streamlit as st
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split

df = pd.read_csv("Dataset.csv")
df=df.drop(['Unnamed: 6','Unnamed: 7','Unnamed: 8'], axis=1)
df = df.dropna()
 
# To reset the indices
df = df.reset_index(drop = True)
df.replace({'Area':{'Ankur':0,'Iscon':1,'Satellite':2,'Thaltej':3,'SG Highway':4,'Vastrapur':5,'Science City':6}},inplace=True)
df.replace({'Type':{'2D':0,'Mobile':1,'3D':2,'Square':3,'Digital':4,'Sqaure':3}},inplace=True)



st.title("Billboard Price Estimator")

X = df.drop('Price',axis=1)
y = df['Price']

X_train, X_test, y_train, y_test = train_test_split(X,y,test_size = 0.2, random_state=10)
rfr = RandomForestRegressor()
rfr.fit(X_train,y_train)


days = st.number_input("Enter number of Days: ")
height = st.number_input("Enter height: ")
width = st.number_input("Enter width: ")

Type = st.selectbox(
    'Type of Billboard',
    ('2D', '3D', 'Mobile','Square','Digital'))

if(Type=="2D"):
    t=0
if(Type=="Mobile"):
    t=1
if(Type=="3D"):
    t=2
if(Type=="Square"):
    t=3
if(Type=="Sqaure"):
    t=3
if(Type=="Digital"):
    t=4


Area = st.selectbox(
    'Area',
    ('Ankur', 'SG Highway', 'Vastrapur','Thaltej','Iscon','Satellite','Science City'))

if(Area=="Ankur"):
    a=0
if(Area=="Iscon"):
    a=1
if(Area=="Satellite"):
    a=2
if(Area=="Thaltej"):
    a=3
if(Area=="SG Highway"):
    a=4
if(Area=="Vastrapur"):
    a=5
if(Area=="Science City"):
    a=6

if st.button("Predict"):
    st.subheader("Predicted Price")
    st.text(rfr.predict([[days,height,width,t,a]]))
