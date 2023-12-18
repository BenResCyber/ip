import socket
import streamlit as st

hostname = socket.gethostname()
ip_address = socket.gethostbyname(hostname)

st.title("Your IP Address")
st.text(ip_address)
