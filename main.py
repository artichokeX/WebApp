import requests
import streamlit as st 
from streamlit_lottie import st_lottie
import json


#configurations
st.set_page_config(page_title="Kurts Webpage", page_icon=":wave:", layout="wide")

def heads():
    with st.container():
        st.subheader("Welcome, User! :wave:")
        st.title("Cyber Security Analsyt | Aspiring Python Developer")
        st.write("With over 5 years of Security Experience, i am looking to enhance security workloads using Python automation, as well as enhancing research capabilities.")
        st.write("[My Github](https://www.github.com/artichokeX)")
heads()

#get lottie
def loadlotti(url):
    
    r = requests.get(url)
    if r.status_code == 200:
        return r.json()
    else:
        print(f"Error {r.status_code}")

#animation file
animation = loadlotti("https://lottie.host/484a6017-6547-4bc5-ab11-74d247af9a3b/SJIBRVbMC5.json")


#lists of random data
with st.container():
    st.divider()
    left,right = st.columns(2)
    
    with left:
        st.header("What I Do")
        st.write('##')
        st.write("""
                 
                 On My Github i have various projects, mainly for FUBAR (google it) and learning.
                 My Goals in life are:
                 - Become a well versed SOC Analyst
                 - Understand Machine Learning and automation within Security
                 - Become a better gamer.
                 """)
        
    with right:
        st_lottie(animation, height=300, key="security")
       
with st.container():
    st.divider()
    left,right = st.columns(2)
    
    with left:
        number = st.slider('Squared')
        st.write(number, 'Squarded is', number * number)
    
    with right:
        name = st.text_input('Your name', key='Name')
        
        if name:
            st.write(f'Hello {name}!')
            

# some JSON:
x =  '{ "name":"John", "age":30, "city":"New York"}'
y =  '{ "name":"Jane", "age":30, "city":"Columbus"}'

def jsonData(b, query):
    try:
        data = json.loads(b)
        return data.get(query, "Query not found")
    except json.JSONDecodeError:
        return "Invalid JSON input"
         
with st.container():
    st.divider()
    left,right = st.columns(2)
        
    with left:
        st.write(jsonData(x, "age"))
    with right:
        st.write(jsonData(y, "city"))