import streamlit
streamlit.title('My parents New Healthy Diner')
streamlit.header('Breakfast Menu')
streamlit.text('🥣Omega 3 & Blueberry Oatmeal')
streamlit.text(' 🥗 kale,Spinach & Rocket Smoothi')
streamlit.text(' 🐔 Hard Boiled Free Range Egg')
streamlit.header('🥑🍞 Avacodo Toast')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝')
import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
# Display the table on the page.
streamlit.dataframe(my_fruit_list)
