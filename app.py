import streamlit as st
from transformers import pipeline

# Load model NER sekali saja
@st.cache_resource
def load_model():
    return pipeline(
        "ner",
        model="Ishan0612/biobert-ner-disease-ncbi",
        tokenizer="Ishan0612/biobert-ner-disease-ncbi",
        aggregation_strategy="simple"
    )

nlp = load_model()

st.set_page_config(page_title="CliniRead - Medical Resume Assistant", layout="wide")

# Header
st.title("Understand Your Medical Resume Like Never Before")
st.markdown("""
CliniRead transforms complex medical records into clear, personalized health insights for you and your caregivers.
""")

# File uploader
uploaded_file = st.file_uploader(
    "Upload Your Medical Resume (PDF, DOC, TXT)",
    type=["pdf", "doc", "docx", "txt"],
    help="Drag and drop file here. Limit 200MB per file."
)

if uploaded_file:
    st.success(f"File **{uploaded_file.name}** berhasil diupload.")
    st.info("Parsing file dan ekstraksi teks bisa dikembangkan lebih lanjut nanti.")

# Separator
st.markdown("---")

# Input teks manual untuk NER testing
st.subheader("Masukkan teks medis untuk analisis NER")
text_input = st.text_area(
    "Masukkan teks medis di sini:",
    value="The patient has signs of diabetes mellitus and chronic obstructive pulmonary disease."
)

if st.button("Proses NER"):
    if not text_input.strip():
        st.warning("Mohon masukkan teks terlebih dahulu.")
    else:
        results = nlp(text_input)
        if results:
            st.subheader("Entity yang terdeteksi:")
            for entity in results:
                st.write(f"{entity['word']} — ({entity['entity_group']}) [score: {entity['score']:.2f}]")
        else:
            st.info("Tidak ada entity yang terdeteksi.")

# Footer
st.markdown("---")
st.markdown("© 2023 CliniRead. All rights reserved. HIPAA compliant secure upload and storage.")













'''

import streamlit as st
from transformers import pipeline

@st.cache_resource
def load_model():
    return pipeline(
        "ner",
        model="Ishan0612/biobert-ner-disease-ncbi",
        tokenizer="Ishan0612/biobert-ner-disease-ncbi",
        aggregation_strategy="simple"
    )

nlp = load_model()

st.title("BioBERT Disease NER")

# Load konten HTML dari file fe.html di repo
with open("fe.html", "r") as f:
    html_content = f.read()

st.markdown(html_content, unsafe_allow_html=True)

# Input teks dari user via Streamlit widget
text_input = st.text_area("Masukkan teks medis:")

if text_input:
    results = nlp(text_input)
    st.subheader("Entity yang terdeteksi:")
    for entity in results:
        st.write(f"{entity['word']} — ({entity['entity_group']})")

        '''
'''
import streamlit as st
from transformers import pipeline

# Load NER pipeline sekali saja
@st.cache_resource
def load_model():
    return pipeline(
        "ner",
        model="Ishan0612/biobert-ner-disease-ncbi",
        tokenizer="Ishan0612/biobert-ner-disease-ncbi",
        aggregation_strategy="simple"
    )

nlp = load_model()

st.title("Named Entity Recognition (NER) for Medical Text")

text = st.text_area("Masukkan teks medis di sini:", 
                    "The patient has signs of diabetes mellitus and chronic obstructive pulmonary disease.")

if st.button("Proses NER"):
    results = nlp(text)
    if results:
        st.write("Hasil NER:")
        for entity in results:
            st.write(f"**{entity['word']}** - ({entity['entity_group']}) [score: {entity['score']:.2f}]")
    else:
        st.write("Tidak ada entity yang terdeteksi.")

'''




