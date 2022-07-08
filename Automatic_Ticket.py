

import streamlit as st
import requests

import pandas as pd
import pickle

from streamlit_lottie import st_lottie
from streamlit_lottie import st_lottie_spinner


def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()
def load_lottiefile(filepath:str):
    with open(fielpath,'r') as f:
        return json.load(f)
k=load_lottieurl('https://assets8.lottiefiles.com/private_files/lf30_oincl3bl.json')  
bank=load_lottieurl('https://assets4.lottiefiles.com/packages/lf20_nMLiIw.json')  
prepaid=load_lottieurl('https://assets2.lottiefiles.com/packages/lf20_yopo5lmk.json')
Dispute=load_lottieurl('https://assets4.lottiefiles.com/packages/lf20_llckxtas.json')
mortgage=load_lottieurl('https://assets3.lottiefiles.com/packages/lf20_h20vn7sp.json')
other=load_lottieurl('https://assets2.lottiefiles.com/packages/lf20_6ofxdidn.json')
img=load_lottieurl('https://assets3.lottiefiles.com/packages/lf20_w51pcehl.json')
st.title('Automatic Ticket Classification')
from PIL import Image
st_lottie(k,speed=2)


text=st.text_area('Complaint')

st.sidebar.title('Ticket will classify in five Categories')
with st.sidebar:
    st_lottie(img)
    st.header('1 Credit card / Prepaid card')
    st.header('2 Bank account services')
    st.header('3 Theft/Dispute reporting')
    st.header('4 Mortgages/loans')
    st.header('5 Others ')


loaded_model = pickle.load(open('model.pkl', 'rb'))
cv=loaded_model['countvect']
tfidf=loaded_model['tifid']
mo=loaded_model['model']


if st.button('Classify'):
    
    
    if [text][0]=='':
        st.title('Please type a complaint')
    else:   
        c=cv.transform([text])
        X=tfidf.transform(c)
        output=mo.predict(X)
        st.title('Complaint is related to')
        if output[0]==1:
            st.header('Credit card or prepaid card')
            st_lottie(prepaid,width=400,height=500)
        elif output[0]==0:
            st.header('Bank Account services')
            st_lottie(bank,width=400,height=500)
        elif output[0]==4:
            st.header('Mortgage/Loan')
            st_lottie(mortgage,width=400,height=500)
        elif output[0]==3:
            st.header('Theft/Dispute Reporting')
            st_lottie(Dispute,width=400,height=500)
        else:
            st.header('Other')   
            st_lottie(other,width=400,height=500)
    
   
    
else:
    st.title('Please type a complaint')
    
