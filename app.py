import streamlit as st
import pickle 
import numpy as np

loaded_model = pickle.load(open('churn.pkl', 'rb'))
sc = pickle.load(open('sc.pkl', 'rb'))

st.title('CHURN PREDICTION')
Age=st.number_input("Enter Age")

Gender = st.selectbox("Gender", ("Male", "Female"))
if Gender == "Male":
    Gender = 0
else:
    Gender = 1
    
Subscription_Length_Months=st.number_input("Enter Subscription Length Months")
Monthly_Bill=st.number_input("Enter Monthly Bill")
Total_Usage_GB=st.number_input("Enter Total Usage GB")
if st.button('Test Results'):
    model = loaded_model.predict(sc.transform([[Age, Gender,Subscription_Length_Months,Monthly_Bill, Total_Usage_GB]]))

    if model == 0:
        st.write("NO")

    else:
        st.write("YES")

