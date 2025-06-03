
import streamlit as st
from transformers import pipeline

# Load model once
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

# --- Header ---
st.title("Understand Your Medical Resume Like Never Before")
st.write(
    "CliniRead transforms complex medical records into clear, personalized health insights for you and your caregivers."
)

# --- File uploader ---
uploaded_file = st.file_uploader(
    "Upload Your Medical Resume (PDF, DOC, TXT)", 
    type=["pdf", "doc", "docx", "txt"],
    help="Drag & drop your file here or click to browse files"
)

if uploaded_file:
    # (Nanti di sini kamu bisa parsing file, extract teks, dll)
    st.success("File uploaded successfully!")
    
    # Contoh sementara: extract teks dari file txt saja (untuk demo)
    if uploaded_file.type == "text/plain":
        content = uploaded_file.read().decode("utf-8")
        st.text_area("Isi dokumen:", content, height=300)
        
        # Run NER untuk demo
        if st.button("Analyze Medical Entities"):
            results = nlp(content)
            st.subheader("Detected Medical Entities:")
            for entity in results:
                st.write(f"- **{entity['word']}** ({entity['entity_group']})")

# --- Sidebar dengan info fitur ---
st.sidebar.header("Your Complete Health Companion")
st.sidebar.write("""
- Medication Breakdown: Clear explanations of prescribed meds  
- Lab Results Explained: Visual charts and normal ranges  
- Follow-up Timeline: Recommended appointments and reminders  
- Condition Summary: Diagnosis overview in plain language  
- Caregiver Access: Share securely with family  
- Interactive Q&A: Chat with AI medical assistant  
""")

# --- Footer ---
st.markdown("---")
st.markdown(
    """
    © 2023 CliniRead. All rights reserved.  
    HIPAA compliant secure upload and storage.
    """
)












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




