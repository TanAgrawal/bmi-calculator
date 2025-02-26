import streamlit as st

st.title("Welcome to BMI Calculator")

weight=st.number_input("Enter your weigth(in kgs)")

h_format=st.radio("Select your height format: ", ("cms","meters","feet"))

BMI_Value=0

if(h_format=="cms"):
    height=st.number_input("Centimeters")

    try:
        BMI_Value=weight/((height/100)**2)
    except:
        st.text("Enter some value of height")

elif(h_format=="meters"):
    height=st.number_input("Meters")

    try:
        BMI_Value=weight/(height**2)
    except:
        st.text("Enter some value of height")

else:
    height=st.number_input("Feet")

    try:
        BMI_Value = weight /(((height/3.28)) ** 2)
    except:
        st.text("Enter some value of height")

if(st.button("Calculate BMI")):
    st.text("Your BMI Index is {}".format(BMI_Value))

if(BMI_Value<16):
    st.error("Extremely Underweight")
elif(BMI_Value>=16 and BMI_Value<18.5):
    st.warning("Underweight")
elif(BMI_Value>=18.5 and BMI_Value<25):
    st.success("Healthy")
elif(BMI_Value>=25 and BMI_Value<30):
    st.warning("Overweight")
elif(BMI_Value>=30):
    st.error("Extremely Overweight")