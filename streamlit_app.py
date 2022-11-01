import streamlit
import pandas
import requests
import snowflake.connector 
from urllib.error import URLError

streamlit.header("The fruit Load list contains:")
def get_fruityvice_data(this_fruit_choice):
 With my_cnx.cursor() as mu_cur:
 my_cur.execute("select * from fruit_load_list")
 return my_cur.fetchall()

if streamlit.button('Get Fruit Load List')
my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_data_rows = get_fruit_load_list()
streamlit.datafram(my_data_rows)



    
 
