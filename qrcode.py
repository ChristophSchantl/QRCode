import streamlit as st
import qrcode
from io import BytesIO
from PIL import Image

st.title("QR-Code Generator")

text = st.text_input("Text oder URL eingeben")

if st.button("QR-Code erstellen") and text:
    qr = qrcode.make(text)
    buf = BytesIO()
    qr.save(buf)
    buf.seek(0)
    img = Image.open(buf)
    st.image(img, caption="Dein QR-Code", use_column_width=True)
