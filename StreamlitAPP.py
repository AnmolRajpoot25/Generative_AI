import streamlit as st
import json
import pandas as pd
import traceback
import PyPDF2
import os
from src.mcqgenerator.utilis import read_file
from src.mcqgenerator.MCQGenerator import generate_evaluate_chain
from src.mcqgenerator.utilis import get_table_data
from langchain.callbacks import get_openai_callback


# =========================
# 🔹 UI CONFIG (ADDED)
# =========================
st.set_page_config(
    page_title="MCQ Generator",
    page_icon="📝",
    layout="centered"
)


# =========================
# 🔹 HEADER SECTION (ADDED)
# =========================
st.markdown(
    """
    <h1 style="text-align:center;">📝 MCQ Generator</h1>
    <p style="text-align:center; color:gray;">
    Generate Multiple Choice Questions using LangChain & LLMs
    </p>
    """,
    unsafe_allow_html=True
)

st.divider()


# =========================
# 🔹 LOAD RESPONSE JSON (UNCHANGED)
# =========================
with open('C:/Users/HP/PycharmProjects/Generative_AI/response.json', 'r') as file:
    RESPONSE_JSON = json.load(file)


# =========================
# 🔹 INPUT FORM SECTION (ENHANCED UI)
# =========================
with st.form("user_inputs"):

    st.subheader("📂 Upload Study Material")

    uploaded_file = st.file_uploader(
        "Upload a PDF or TXT file",
        type=["pdf", "txt"]
    )

    st.subheader("⚙️ MCQ Configuration")

    col1, col2 = st.columns(2)

    with col1:
        mcq_count = st.number_input(
            "Number of MCQs",
            min_value=3,
            max_value=50
        )

        subject = st.text_input(
            "Subject",
            max_chars=30
        )

    with col2:
        tone = st.text_input(
            "Complexity Level",
            max_chars=20,
            placeholder="Medium"
        )

    st.divider()

    button = st.form_submit_button("🚀 Create MCQs")


# =========================
# 🔹 BACKEND EXECUTION (UNCHANGED)
# =========================
if button and uploaded_file is not None and mcq_count and subject and tone:
    with st.spinner("Generating MCQs..."):
        try:
            text = read_file(uploaded_file)

            with get_openai_callback() as cb:
                response = generate_evaluate_chain(
                    {
                        "text": text,
                        "number": mcq_count,
                        "subject": subject,
                        "tone": tone,
                        "response_json": json.dumps(RESPONSE_JSON)
                    }
                )

        except Exception as e:
            traceback.print_exception(type(e), e, e.__traceback__)
            st.error("❌ Something went wrong")

        else:
            # =========================
            # 🔹 TOKEN INFO (ADDED – OPTIONAL UI)
            # =========================
            with st.expander("📊 Token Usage Details"):
                st.write(f"Total Tokens: {cb.total_tokens}")
                st.write(f"Prompt Tokens: {cb.prompt_tokens}")
                st.write(f"Completion Tokens: {cb.completion_tokens}")
                st.write(f"Total Cost: {cb.total_cost}")

            # =========================
            # 🔹 OUTPUT DISPLAY (ENHANCED)
            # =========================
            if isinstance(response, dict):
                quiz = response.get("quiz", None)

                if quiz is not None:
                    table_data = get_table_data(quiz)

                    if table_data is not None:
                        st.subheader("📘 Generated MCQs")

                        df = pd.DataFrame(table_data)
                        df.index = df.index + 1
                        st.table(df)

                        st.subheader("📝 Review / Explanation")
                        st.text_area(
                            label="",
                            value=response["review"],
                            height=150
                        )

                    else:
                        st.error("Error in the table data")
            else:
                st.write(response)


# =========================
# 🔹 FOOTER (ADDED)
# =========================
st.divider()
st.markdown(
    "<p style='text-align:center; color:gray;'>Built with ❤️ using Streamlit & LangChain</p>",
    unsafe_allow_html=True
)
