import streamlit as st
import psycopg2

st.write("Hello **world**!")

conn = psycopg2.connect(database="postgres", user="postgres", 
                        password="postgres", host="postgres", 
                        port="5432")