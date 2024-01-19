import streamlit as st
st.title('campusx')
col1,col2=st.columns(2)

with col1:
    st.image('D:\github_campusx\IMG_20210824_132021.jpg')
with col2:
    st.header('Campusx is an online learning platform, changing image')    
st.header('Courses')
st.subheader('DSMP')
st.subheader('ML')  
st.subheader('DSA')  
st.sidebar.title("Menu")
st.sidebar.markdown("""
-HOME
-MENU                    
-CAREER
-LOGIN
""")
st.sidebar.selectbox("Select one",["teacher","student"])
st.title("Hello teacher")