import streamlit as st
from app.retrieval.qa import answer
from app.agents.gap_detector import find_conflicts

st.set_page_config(page_title="BA Copilot", layout="wide")
st.title("BA Copilot")
st.caption("Ask questions about your business documents and find contradictions between them.")

tab_ask, tab_conflicts = st.tabs(["Ask a question", "Find conflicts"])

with tab_ask:
    question = st.text_input("Your question", placeholder="What is the minimum credit score?")
    if st.button("Get answer") and question:
        with st.spinner("Searching documents..."):
            st.write(answer(question))

with tab_conflicts:
    if st.button("Find conflicts"):
        with st.spinner("Comparing documents..."):
            report = find_conflicts()
        st.success(f"Found {len(report.conflicts)} conflicts")
        st.table([
            {
                "Topic": c.topic,
                "Severity": c.severity.upper(),
                "Old / document A": f"{c.document_a}: {c.statement_a}",
                "New / document B": f"{c.document_b}: {c.statement_b}",
                "Ask the stakeholder": c.suggested_question,
            }
            for c in report.conflicts
        ])