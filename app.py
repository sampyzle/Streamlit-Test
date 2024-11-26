import streamlit as st

st.title('Streamlit Class')

st.subheader("This is a practce Deployment")

st.checkbox('I am a Male')

st.radio("select a gender", ['Male','Female'])

st.selectbox('Pick a weapon', ['Gun','knife'])

st.multiselect('Pick a weapon', ['Gun','knife'])

st.button('Click Me👍')

st.text_input("Enter your Name", placeholder= 'eg: Cesar Sampaio')

st.text_area('Tell me about yourself', "eg I am a ....")

st.text_input('Enter your Password:',type= 'password')

st.slider('Pick a range', 1, 5)


st.number_input('Enter your weight:')

































st.title('Streamlit Class')

st.header("Sampaio")

st.subheader('My surname is Ceasar')

st.write('I love Python')

st.divider()

st.text('This is nice')

st.markdown('### This is a markdown')

st.success('What a success!')

st.warning('Stop there')

st.info('Plum Weapons')

st.error('Try again!')

st.exception(ZeroDivisionError('Try to divide by zero'))

st.image('filename.png')