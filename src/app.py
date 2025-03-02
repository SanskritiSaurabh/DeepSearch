import streamlit as st
from workflow import app  # Import from workflow.py instead of main.py
from utils.config import get_config

config = get_config()

st.set_page_config(page_title="KaironAI", layout="wide")
st.title("🔍 KaironAI Research Agent")

query = st.text_input("Enter your research question:", placeholder="What is...?")

if st.button("Generate Report"):
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Research Process")
        with st.status("Processing query...", expanded=True) as status:
            try:
                st.write("🔎 Gathering information...")
                result = app.invoke({"query": query})
                
                status.update(label="Research complete!", state="complete")
                st.subheader("Raw Research Data")
                st.json(result["research_data"])
                
            except ValueError as e:
                status.update(label="Configuration error!", state="error")
                st.error(f"Configuration error: {str(e)}")
            except Exception as e:
                status.update(label="System failure!", state="error")
                st.error(f"System failure: {str(e)}")
    
    with col2:
        st.subheader("Final Report")
        if "final_answer" in result:
            st.markdown(result["final_answer"])
        else:
            st.warning("No answer generated")