import streamlit as st
import os
import PyPDF2
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains import ConversationalRetrievalChain
from langchain.docstore.document import Document
import glob
from dotenv import load_dotenv

load_dotenv()

# Set up OpenAI API key
openai_api_key = os.getenv("OPENAI_API_KEY")
st.write("OpenAI API Key:", openai_api_key)

# Initialize session state for chat history and vector store
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []
if "vector_store" not in st.session_state:
    st.session_state.vector_store = None
if "conversation_chain" not in st.session_state:
    st.session_state.conversation_chain = None

# Function to read text from a PDF file
def read_pdf(file_path):
    try:
        with open(file_path, "rb") as file:
            pdf_reader = PyPDF2.PdfReader(file)
            text = ""
            for page in pdf_reader.pages:
                text += page.extract_text() or ""
            return text
    except Exception as e:
        st.error(f"Error reading PDF file: {e}")
        return None

# Function to read code files from portfolio folder
def read_portfolio_files(folder_path="portfolio"):
    documents = []
    if not os.path.exists(folder_path):
        st.error(f"Portfolio folder '{folder_path}' not found.")
        return documents
    for file_path in glob.glob(f"{folder_path}/**/*", recursive=True):
        if os.path.isfile(file_path):
            try:
                with open(file_path, "r", encoding="utf-8") as f:
                    content = f.read()
                    documents.append(Document(page_content=content, metadata={"source": file_path}))
            except Exception as e:
                st.warning(f"Could not read {file_path}: {e}")
    return documents

# Function to create vector store from resume and portfolio
def create_vector_store(resume_text, portfolio_docs):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    documents = [Document(page_content=resume_text, metadata={"source": "resume"})] + portfolio_docs
    chunks = text_splitter.split_documents(documents)
    embeddings = OpenAIEmbeddings(model="text-embedding-ada-002")
    vector_store = FAISS.from_documents(chunks, embeddings)
    return vector_store

# Streamlit app layout
st.title("Resume & Portfolio Chatbot")
st.write("Ask questions about your resume or portfolio.")

# Hardcoded resume file path
resume_file_path = "resume/Resume_Suyash.pdf"

# Button to index resume and portfolio
if st.button("Index Resume and Portfolio"):
    if not openai_api_key:
        st.error("Cannot proceed without a valid OpenAI API key.")
    elif os.path.exists(resume_file_path):
        with st.spinner("Indexing documents..."):
            # Read resume
            resume_text = read_pdf(resume_file_path)
            if resume_text:
                # Read portfolio files
                portfolio_docs = read_portfolio_files()
                
                # Create vector store
                try:
                    st.session_state.vector_store = create_vector_store(resume_text, portfolio_docs)
                    
                    # Initialize conversation chain
                    llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.3)
                    st.session_state.conversation_chain = ConversationalRetrievalChain.from_llm(
                        llm=llm,
                        retriever=st.session_state.vector_store.as_retriever(),
                        return_source_documents=True
                    )
                    st.success("Indexing complete! You can now ask questions.")
                except Exception as e:
                    st.error(f"Error creating vector store or conversation chain: {e}")
            else:
                st.error("Failed to read resume. Please check the file.")
    else:
        st.error(f"Resume file '{resume_file_path}' not found.")

# Chat interface
st.subheader("Chat with the Bot")
user_question = st.text_input("Ask a question about your resume or portfolio:")

if user_question and st.session_state.conversation_chain:
    with st.spinner("Generating response..."):
        try:
            response = st.session_state.conversation_chain({
                "question": user_question,
                "chat_history": st.session_state.chat_history
            })
            answer = response["answer"]
            st.session_state.chat_history.append((user_question, answer))
            
            # Display response
            st.write("**Bot:**", answer)
            
            # Display chat history
            st.subheader("Chat History")
            for i, (q, a) in enumerate(st.session_state.chat_history):
                st.write(f"**Q{i+1}:** {q}")
                st.write(f"**A{i+1}:** {a}")
                st.write("---")
        except Exception as e:
            st.error(f"Error generating response: {e}")
else:
    if user_question:
        st.warning("Please index your resume and portfolio first.")
