import streamlit as st
st.set_page_config(page_title="QR-Code Generator", page_icon="🔳")

import qrcode
from io import BytesIO
from PIL import Image

st.title("🔳 QR-Code Generator für Webseiten")

# Eingabefeld für Text oder URL
webpage = st.text_input("Gib die Webseite oder den Text ein:", placeholder="https://example.com")

# Button zur Generierung
if st.button("QR-Code erstellen") and webpage:
    # QR-Code erzeugen
    qr = qrcode.make(webpage)

    # Bild im Arbeitsspeicher speichern
    buffer = BytesIO()
    qr.save(buffer, format="PNG")
    buffer.seek(0)
    img = Image.open(buffer)

    # Bild anzeigen
    st.image(img, caption="Dein QR-Code", use_column_width=False)

    # Download-Link
    st.download_button(
        label="📥 QR-Code herunterladen",
        data=buffer,
        file_name="qrcode.png",
        mime="image/png"
    )
