
import streamlit as st
import os
import qrcode

st.title("QR-Code Generator")

webpage = input("webpage: ")

img = qrcode.make(f" Webpage: {webpage}")
img.save("qr.png", "PNG")

