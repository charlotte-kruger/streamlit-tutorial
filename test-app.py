import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.header('this is the intro to streamlit')

our_data=pd.DataFrame({
    'Alex':[1,2,3,4,5],
    'Char':[55,45,35,25,15],
    'Third': [10,20,30,40,50]
})

st.write(our_data)

st.table(our_data)

st.dataframe(our_data.style.highlight_max(axis=0))

st.line_chart(our_data)

our_figure = plt.figure(figsize=(10,6))
plt.plot(our_data['Alex'])
st.pyplot(our_figure)

st.markdown('# Widgets')
x=st.slider('the value of x')

st.write('the value of', x, 'squared is', x**2)


st.markdown('## Use a select box to use your plot')

plot_choice = st.selectbox("which dataset would you like to plot?", ('Alex', 'Char', 'Third'))
selected_fig = plt.figure()
plt.plot(our_data[plot_choice])
st.pyplot(selected_fig)