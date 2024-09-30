import streamlit as st
import pickle

# load model
model = pickle.load(open('sentiment_analysis.pkl', 'rb'))

# create title
st.title('Sentiment Analysis Model')

review = st.text_input('Enter your review')

submit = st.button('Predict')

if submit:
    prediction = model.predict([review])
    if prediction[0] == 'negative':
        st.success('Positive Review')
    else:
        st.warning('Negative Review')
