import os
import requests
from bs4 import BeautifulSoup
from langchain.docstore.document import Document
from langchain.text_splitter import RecursiveCharacterTextSplitter
import io
from PyPDF2 import PdfReader
import hashlib

# For html to txt

def content_compiler(urls):
    webpage_texts = ' '

    for url in urls:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        text = soup.get_text()
        webpage_texts += text

    content = Document(page_content=webpage_texts)
    return [content]

# For pdf to txt

CACHE_FOLDER = "pdf_cache"
os.makedirs(CACHE_FOLDER, exist_ok=True)

def download_pdf(file_id):
    cache_path = os.path.join(CACHE_FOLDER, f"{file_id}.pdf")

    if os.path.exists(cache_path):
        print(f"Using cached PDF for {file_id}")
        with open(cache_path, "rb") as f:
            return f.read()
            # return Document(page_content=f.read(), metadata={"source":f"{file_id}"})
    
    print(f"Downloading PDF: {file_id}")
    url = f'https://drive.google.com/uc?export=download&id={file_id}' # Files had to be downloaded into Gdrive as EDB website blocked by Incapsula
    response = requests.get(url)
    if response.status_code == 200:
        with open(cache_path, "wb") as f:
            f.write(response.content)
        return response.content
        # return response.content
        # return Document(page_content=response.content, metadata={"source":f"{file_id}"})
        # return [content]
    else:
        raise Exception(f"Failed to download: {file_id}")
    
def extract_text(pdf_bytes):
    reader = PdfReader(io.BytesIO(pdf_bytes))
    pdf_text = ''
    for page in reader.pages:
        pdf_text += page.extract_text() + '\n'
    return pdf_text

def compile_pdfs(file_ids):
    corpus_parts = []
    
    for i, file_id in enumerate(file_ids):
        print(f"Processing PDF {i+1}")
        pdf_bytes = download_pdf(file_id)
        text = extract_text(pdf_bytes)
        # corpus_parts.append(f"[PDF {i+1} - ID {file_id}]\n{text}")
        corpus_parts.append(Document(page_content=text, metadata={"source":file_id}))
    # full_corpus = "\n\n".join(corpus_parts)
    # return full_corpus
    return corpus_parts

# Splitters

def splitter(doc):
    text_splitter = RecursiveCharacterTextSplitter(
        separators=["\n\n", "\n", " ", ""], 
        chunk_size=800, 
        chunk_overlap=50,
        )
    chunks = text_splitter.split_documents(doc)
    return chunks

