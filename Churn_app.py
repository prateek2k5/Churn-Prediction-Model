import streamlit as st
import pickle
import numpy as np

#Load Model
with open('churn_model.pkl','rb') as f:
    model=pickle.load(f)

#Heading of the Webpage
st.title("Customer Churn Prediction")
#Subheading of the Webpage
st.write("Enter the Customer Details below : ")

#Using slider we are taking input from the users (min,max,mid)values
CreditScore=st.slider("Credit Score",0,1000,500)
Geography=st.slider("Geography (0-->France 1-->Germany 2-->Spain)",0,2,1)
Gender=st.slider("Gender (1-->Male , 0-->Female)",1.0,7.0,4.0)
Age=st.slider("Age",18,100,41)
Tenure=st.slider("Tenure",0,100,50)
Balance=st.slider("Balance")
NumOfProducts=st.slider("Num_Of_Products_Owned",0,100,50)
HasCrCard=st.slider("Has_Credit_Card (0-->No 1-->Yes)",0,1)
IsActiveMember=st.slider("Is_Active_Member (0-->No 1-->Yes)",0,1)
EstimatedSalary=st.slider("Estimated_Salary")


features=np.array([[CreditScore,Geography,Gender,Age,Tenure,Balance,NumOfProducts,HasCrCard,IsActiveMember,EstimatedSalary]])

if st.button("Predict"):
    prediction = model.predict(features)

    if prediction[0] == 1:
        st.error("⚠️ The customer is likely to churn.")
    else:
        st.success("✅ The customer is likely to stay.")
