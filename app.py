## frontend/app.py
import streamlit as st

st.set_page_config(page_title="Carolina Bandwidth Dashboard")
st.title("📊 Carolina Bandwidth Dashboard")

st.success("Backend connection live. Monitoring started.")

st.text_input("Input Text for GPT")
st.file_uploader("Upload Audio for Whisper")

st.markdown("---")
st.write("Job Queue Status: TODO")amlit or Gradio entry point
