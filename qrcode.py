import streamlit as st
import qrcode
from io import BytesIO
from PIL import Image

st.set_page_config(page_title="QR-Code Generator", page_icon="🔳")
st.title("🔳 QR-Code Generator für Webseiten")

# Texteingabe vom Nutzer
webpage = st.text_input("Gib die Webseite oder den Text ein:", placeholder="https://example.com")

if st.button("QR-Code erstellen") and webpage:
    # QR-Code erzeugen
    qr = qrcode.make(webpage)

    # Zwischenspeicher anlegen (nicht speichern!)
    buffer = BytesIO()
    qr.save(buffer, format="PNG")
    buffer.seek(0)
    img = Image.open(buffer)

    # QR-Code anzeigen
    st.image(img, caption="Dein QR-Code", use_column_width=False)
