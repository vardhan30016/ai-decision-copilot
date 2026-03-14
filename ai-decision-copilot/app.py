import streamlit as st
from data_processor import load_data
from decision_engine import analyze_data

st.set_page_config(
    page_title="AI Decision Copilot",
    layout="wide"
)

# Custom CSS
st.markdown("""
<style>
.main {
    background-color:#0f172a;
}

h1 {
color:white;
text-align:center;
}

.stFileUploader {
background-color:#1e293b;
padding:20px;
border-radius:10px;
}

.result-box {
background:#111827;
padding:20px;
border-radius:10px;
color:white;
}
</style>
""", unsafe_allow_html=True)

st.title("🚀 AI Decision Copilot")

st.write("Upload any dataset or document to get AI-powered insights")

uploaded_file = st.file_uploader(
    "Upload File",
    type=["csv","xlsx","pdf","txt"]
)

if uploaded_file:

    st.success("File uploaded successfully")

    data = load_data(uploaded_file)

    st.subheader("Preview")

    st.write(data)

    if st.button("Analyze with AI"):

        with st.spinner("AI analyzing data..."):

            result = analyze_data(data)

            st.markdown(
                f'<div class="result-box">{result}</div>',
                unsafe_allow_html=True
            )