import streamlit as st
from transformers import pipeline
import re

@st.cache_resource
def load_model():
    return pipeline("ner", model="d4data/biomedical-ner-all", aggregation_strategy="simple")

nlp = load_model()

st.title("CliniRead: Medical Resume Analyzer")

uploaded_file = st.file_uploader("Upload your medical resume (TXT only)", type=["txt"])

if uploaded_file is not None:
    text = uploaded_file.read().decode("utf-8")
    st.subheader("Resume Text")
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
