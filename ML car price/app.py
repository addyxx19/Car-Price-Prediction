import pandas as pd
import numpy as np
import pickle as pk
import streamlit as st

model=pk.load (open('model.pkl','rb'))

st.header('Car Price Prediction ML Model')
cd= pd.read_csv('Cardetails.csv')
def getbn(car_name):
    car_name= car_name.split(' ')[0]
    return car_name.strip() 
cd['name']= cd['name'].apply(getbn)

name=st.selectbox('Select Car Brand', cd['name'].unique())
year=st.slider('Car Manufacture Year', 1994,2024)
km_driven=st.slider('Number of kms driven', 11,200000)
fuel=st.selectbox('Fuel Type', cd['fuel'].unique())
seller_type=st.selectbox('Seller Type', cd['seller_type'].unique())
transmission=st.selectbox('Transmission Type', cd['transmission'].unique())
owner= st.selectbox('Seller Type', cd['owner'].unique())
mileage=st.slider('Car Mileage', 10,40)
engine=st.slider('Engine CC', 700,5000)
max_power=st.slider('Max Power', 11,200)
seats=st.slider('Number of Seats ', 5,10)


if st.button("Predict"):
    inputdm= pd.DataFrame(
    [[name,year,km_driven,fuel,seller_type,transmission,owner,mileage,engine,max_power,seats]],
    columns=['name','year','km_driven','fuel','seller_type','transmission','owner','mileage','engine','max_power','seats'])
    inputdm['owner'].replace(['First Owner', 'Second Owner', 'Third Owner',
       'Fourth & Above Owner', 'Test Drive Car'],[1,2,3,4,5], inplace=True)
    inputdm['fuel'].replace(['Diesel', 'Petrol', 'LPG', 'CNG'],[1,2,3,4], inplace=True)
    inputdm['seller_type'].replace(['Individual', 'Dealer', 'Trustmark Dealer'],[1,2,3], inplace=True)
    inputdm['transmission'].replace(['Manual', 'Automatic'],[1,2], inplace=True)
    inputdm['name'].replace(['Maruti' ,'Skoda', 'Honda', 'Hyundai', 'Toyota' ,'Ford', 'Renault' ,'Mahindra',
      'Tata', 'Chevrolet', 'Datsun' ,'Jeep', 'Mercedes-Benz', 'Mitsubishi', 'Audi',
      'Volkswagen' ,'BMW', 'Nissan', 'Lexus', 'Jaguar' ,'Land' ,'MG' ,'Volvo', 'Daewoo',
      'Kia', 'Fiat', 'Force' ,'Ambassador' ,'Ashok', 'Isuzu', 'Opel'],
                   [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31],
                   inplace=True)
    

    car_price= model.predict(inputdm)
    st.markdown('Car Price is going to be'+str(car_price[0]))    
