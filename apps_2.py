import streamlit as st
from transformers import pipeline
import pdfplumber
from pdf2image import convert_from_bytes
import pytesseract
import re

@st.cache_resource
def load_model():
    return pipeline("ner", model="d4data/biomedical-ner-all", aggregation_strategy="simple")

nlp = load_model()

st.title("CliniRead with PDF OCR")

uploaded_file = st.file_uploader("Upload your medical resume (PDF)", type=["pdf"])

def extract_text_from_pdf(file_bytes):
    # Try extracting text from PDF (text-based)
    with pdfplumber.open(file_bytes) as pdf:
        full_text = ""
        for page in pdf.pages:
            full_text += page.extract_text() or ""
    if full_text.strip():
        return full_text
    # If empty, do OCR
    images = convert_from_bytes(file_bytes.read())
    text = ""
    for image in images:
        text += pytesseract.image_to_string(image)
    return text

if uploaded_file:
    text = extract_text_from_pdf(uploaded_file)
    st.subheader("Extracted Text")
    st.write(text)
    
    if st.button("Analyze"):
        entities = nlp(text)
        
        obat = [e['word'] for e in entities if e['entity_group'].lower() in ['drug', 'medication']]
        penyakit = [e['word'] for e in entities if e['entity_group'].lower() in ['disease', 'diagnosis', 'condition']]
        
        jadwal = re.findall(r'(kontrol|follow[- ]?up|check[- ]?up).*?(\d{1,2} \w+ \d{4}|\d{1,2}/\d{1,2}/\d{2,4})', text, flags=re.IGNORECASE)
        jadwal = [f"{m[0]} pada {m[1]}" for m in jadwal]
        
        instruksi = [line for line in text.split('\n') if any(k in line.lower() for k in ['jaga', 'hindari', 'sarankan', 'pantau', 'perhatikan'])]
        
        st.subheader("Summary")
        
        st.markdown("**Diagnosed Conditions:**")
        if penyakit:
            for p in set(penyakit):
                st.write("-", p)
        else:
            st.write("Tidak terdeteksi kondisi medis.")
        
        st.markdown("**Medications:**")
        if obat:
            for o in set(obat):
                st.write("-", o)
        else:
            st.write("Tidak terdeteksi obat.")
        
        st.markdown("**Follow-up Schedule:**")
        if jadwal:
            for j in jadwal:
                st.write("-", j)
        else:
            st.write("Tidak ditemukan jadwal kontrol/follow-up.")
        
        st.markdown("**Instructions / Advice:**")
        if instruksi:
            for i in instruksi:
                st.write("-", i)
        else:
            st.write("Tidak ditemukan instruksi khusus.")
