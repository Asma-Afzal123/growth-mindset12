#streamlit
import streamlit as st

st.set_page_config(page_title= "growth mindset project", project_icon="★")
st.title("Growth Mindset Challenge: Web App with Streamlit")

st.header("Welcome to Your Growth Journey!")
st.write("The Growth Mindset Challenge is an interactive web application built with Python and Streamlit. This app helps users develop a positive and resilient mindset by engaging them in daily challenges, self-reflection exercises, and motivational content.")

#quote section
st.header("Today's Growth Mindset Quote")
st.write("Success is not final,failure is not fatal:it is the courage to continue that counts. - Winston Churchill")
 
st.header("🔧What's your challenge Today?")
user_input = st.text_input("Describe a challenge you facing:")


#condition
if user_input:
    st.success(f"💪you re facing:{user_input}.keep pushing forward towords your goal!🚀")
else:
st.warning("Tell us about your challenge to get started!")

#reflexing
st.header("Reflect on Your Learning")
reflection = st.text_area("erite your reflections here:")

if reflection:
    st.success(f"✨Great Your reflection:{reflection}")

else:
    st.info("Reflection on past experience help your growth!Share your difficulties")

#acheivements

st.header("🏆Celebrate Your Wins!")
acheivement = st.text_input("share something you've recently accomplished:")

if acheivement:
    st.success(f"🎉Amazing you achieved:{acheivement}")
else:
    st.info("Big or small , every acheivement counts! share one now 😍")   


#footer
st.write("- - -")
st.write("🚀 Keep believing in yourself.Growth is a journey,not a destination! ✨")
st.write("** © Created by Asma Afzal**")
