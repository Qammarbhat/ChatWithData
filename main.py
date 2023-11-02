import streamlit as st
from functions_langchian import csv_reader

def main():
    st.set_page_config("Ask your CSV")
    st.header("Chat with your CSV by CQAI")

    user_csv = st.file_uploader("Upload your CSV file", type = "csv")

    if user_csv is not None:
        user_question = st.text_input("Ask a question about your CSV")
        st.write(f"Your question is : {user_question}")
        st.write("Answer:")
        st.write(csv_reader(user_csv, user_question))

if __name__ == "__main__":
    main()