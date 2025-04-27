







# # === index_data.py (formerly image_data.py) ===
# import os
# import requests
# from bs4 import BeautifulSoup
# import html2text
# from langchain_chroma import Chroma
# from langchain.docstore.document import Document
# from langchain_huggingface import HuggingFaceEmbeddings

# embedding_function = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
# db = Chroma(persist_directory="chroma_db", embedding_function=embedding_function)

# SCRAPE_LINKS = [
#     "https://www.mentalhealth.org.uk/explore-mental-health/publications/how-to-manage-and-reduce-stress",
#     "https://www.verywellmind.com/tips-to-reduce-stress-3145195",
#     "https://www.helpguide.org/articles/stress/stress-management.htm",
#     "https://www.nimh.nih.gov/health/topics/caring-for-your-mental-health",
#     "https://www.mind.org.uk/information-support/tips-for-everyday-living/",
#     "https://psychcentral.com/stress/how-to-calm-an-anxious-mind",
#     "https://www.betterhelp.com/advice/stress/10-effective-ways-to-manage-stress/",
#     "https://adaa.org/tips-manage-anxiety-and-stress",
#     "https://www.medicalnewstoday.com/articles/how-to-deal-with-stress",
#     "https://www.headspace.com/articles/stress",
#     "https://www.psycom.net/depression.central.html",
#     "https://www.psychologytoday.com/us/basics/depression",
#     "https://www.psychologytoday.com/us/basics/anxiety",
#     "https://www.webmd.com/depression/guide/depression-overview",
#     "https://www.mayoclinic.org/diseases-conditions/depression/in-depth/depression/art-20045943",
#     "https://www.mindful.org/what-is-mindfulness/",
#     "https://www.mentalhealth.gov/basics/what-is-mental-health",
#     "https://www.apa.org/topics/mental-health/",
#     "https://www.cdc.gov/mentalhealth/learn/index.htm",
#     "https://www.nami.org/About-Mental-Illness",
# ]

# def scrape_to_text(url):
#     try:
#         response = requests.get(url, timeout=10)
#         soup = BeautifulSoup(response.text, "html.parser")
#         for script in soup(["script", "style"]):
#             script.decompose()
#         html_content = soup.get_text()
#         markdown = html2text.html2text(html_content)
#         return markdown
#     except Exception as e:
#         print(f"❌ Failed to scrape {url}: {e}")
#         return ""

# def load_and_embed():
#     docs = []
#     for link in SCRAPE_LINKS:
#         content = scrape_to_text(link)
#         if content:
#             docs.append(Document(page_content=content, metadata={"source": link}))
#     if docs:
#         db.add_documents(docs)
#         print(f"✅ Embedded {len(docs)} articles.")
#     else:
#         print("⚠️ No documents were embedded. Check the links or scraping logic.")

# if __name__ == "__main__":
#     load_and_embed()   





# # === index_data.py ===
# import os
# import requests
# from bs4 import BeautifulSoup
# import html2text
# from langchain_chroma import Chroma
# from langchain.docstore.document import Document
# from langchain_huggingface import HuggingFaceEmbeddings
# import fitz  # PyMuPDF

# # Initialize embedding and Chroma DB
# embedding_function = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
# db = Chroma(persist_directory="chroma_db", embedding_function=embedding_function)

# # Web URLs and PDF files
# SCRAPE_LINKS = [
#     "https://www.mentalhealth.org.uk/explore-mental-health/publications/how-to-manage-and-reduce-stress",
#     "https://www.verywellmind.com/tips-to-reduce-stress-3145195",
#     "https://www.helpguide.org/articles/stress/stress-management.htm",
#     "https://www.nimh.nih.gov/health/topics/caring-for-your-mental-health",
#     "https://www.mind.org.uk/information-support/tips-for-everyday-living/",
#     "https://psychcentral.com/stress/how-to-calm-an-anxious-mind",
#     "https://www.betterhelp.com/advice/stress/10-effective-ways-to-manage-stress/",
#     "https://adaa.org/tips-manage-anxiety-and-stress",
#     "https://www.medicalnewstoday.com/articles/how-to-deal-with-stress",
#     "https://www.headspace.com/articles/stress",
#     "https://www.psycom.net/depression.central.html",
#     "https://www.psychologytoday.com/us/basics/depression",
#     "https://www.psychologytoday.com/us/basics/anxiety",
#     "https://www.webmd.com/depression/guide/depression-overview",
#     "https://www.mayoclinic.org/diseases-conditions/depression/in-depth/depression/art-20045943",
#     "https://www.mindful.org/what-is-mindfulness/",
#     "https://www.mentalhealth.gov/basics/what-is-mental-health",
#     "https://www.apa.org/topics/mental-health/",
#     "https://www.cdc.gov/mentalhealth/learn/index.htm",
#     "https://www.nami.org/About-Mental-Illness",
# ]

# PDF_FILES = [
#     r"C:\Users\bharg\OneDrive\Documents\CalmConnect\WellbeingMentalWellness2020-final.pdf"
# ]

# # Function to scrape web content and convert to markdown text
# def scrape_to_text(url):
#     try:
#         response = requests.get(url, timeout=10)
#         soup = BeautifulSoup(response.text, "html.parser")
#         for script in soup(["script", "style"]):
#             script.decompose()
#         html_content = soup.get_text()
#         markdown = html2text.html2text(html_content)
#         return markdown
#     except Exception as e:
#         print(f"❌ Failed to scrape {url}: {e}")
#         return ""

# # Function to extract PDF text using PyMuPDF
# def extract_text_from_pdf(pdf_path):
#     text = ""
#     try:
#         doc = fitz.open(pdf_path)
#         for page in doc:
#             text += page.get_text()
#     except Exception as e:
#         print(f"❌ Failed to extract text from {pdf_path}: {e}")
#     return text

# # Main processing logic
# def load_and_embed():
#     docs = []

#     # Scrape and convert web pages
#     for link in SCRAPE_LINKS:
#         content = scrape_to_text(link)
#         if content:
#             docs.append(Document(page_content=content, metadata={"source": link}))

#     # Extract from PDFs and save as .txt
#     for pdf_file in PDF_FILES:
#         if not os.path.isfile(pdf_file):
#             print(f"⚠️ PDF not found: {pdf_file}")
#             continue

#         content = extract_text_from_pdf(pdf_file)
#         if not content:
#             continue

#         # Save extracted text to .txt
#         txt_file = pdf_file.replace(".pdf", ".txt")
#         try:
#             with open(txt_file, "w", encoding="utf-8") as out:
#                 out.write(content)
#             print(f"📄 Saved extracted text to {txt_file}")
#         except Exception as e:
#             print(f"❌ Failed to write {txt_file}: {e}")

#         doc_name = os.path.splitext(os.path.basename(pdf_file))[0]

#         # Store in document list with metadata
#         docs.append(Document(
#             page_content=content,
#             metadata={
#                 "source": pdf_file,
#                 "doc_name": doc_name
#             }
#         ))

#     # Add all docs to vector DB
#     if docs:
#         db.add_documents(docs)
#         print(f"✅ Embedded {len(docs)} documents (web + PDFs).")
#     else:
#         print("⚠️ No documents were embedded. Check the links, PDFs, or scraping logic.")

# # Run
# if __name__ == "__main__":
#     load_and_embed()








# # === index_data.py ===
# import os
# import requests
# from bs4 import BeautifulSoup
# import html2text
# from langchain_chroma import Chroma
# from langchain.docstore.document import Document
# from langchain_huggingface import HuggingFaceEmbeddings
# from langchain.text_splitter import RecursiveCharacterTextSplitter
# import fitz  # PyMuPDF

# # Initialize embedding and Chroma DB
# embedding_function = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
# db = Chroma(persist_directory="chroma_db", embedding_function=embedding_function)

# # Web URLs and PDF files
# SCRAPE_LINKS = [
#     "https://www.mentalhealth.org.uk/explore-mental-health/publications/how-to-manage-and-reduce-stress",
#     "https://www.verywellmind.com/tips-to-reduce-stress-3145195",
#     "https://www.helpguide.org/articles/stress/stress-management.htm",
#     "https://www.nimh.nih.gov/health/topics/caring-for-your-mental-health",
#     "https://www.mind.org.uk/information-support/tips-for-everyday-living/",
#     "https://psychcentral.com/stress/how-to-calm-an-anxious-mind",
#     "https://www.betterhelp.com/advice/stress/10-effective-ways-to-manage-stress/",
#     "https://adaa.org/tips-manage-anxiety-and-stress",
#     "https://www.medicalnewstoday.com/articles/how-to-deal-with-stress",
#     "https://www.headspace.com/articles/stress",
#     "https://www.psycom.net/depression.central.html",
#     "https://www.psychologytoday.com/us/basics/depression",
#     "https://www.psychologytoday.com/us/basics/anxiety",
#     "https://www.webmd.com/depression/guide/depression-overview",
#     "https://www.mayoclinic.org/diseases-conditions/depression/in-depth/depression/art-20045943",
#     "https://www.mindful.org/what-is-mindfulness/",
#     "https://www.mentalhealth.gov/basics/what-is-mental-health",
#     "https://www.apa.org/topics/mental-health/",
#     "https://www.cdc.gov/mentalhealth/learn/index.htm",
#     "https://www.nami.org/About-Mental-Illness",
# ]

# PDF_FILES = [
#     r"C:\Users\bharg\OneDrive\Documents\CalmConnect\WellbeingMentalWellness2020-final.pdf",
#     r"C:\Users\bharg\OneDrive\Documents\CalmConnect\wellbeing-team-cbt-workshop-booklet-2016.pdf"
# ]

# # Function to scrape web content and convert to markdown text
# def scrape_to_text(url):
#     try:
#         response = requests.get(url, timeout=10)
#         soup = BeautifulSoup(response.text, "html.parser")
#         for script in soup(["script", "style"]):
#             script.decompose()
#         html_content = soup.get_text()
#         markdown = html2text.html2text(html_content)
#         return markdown
#     except Exception as e:
#         print(f"❌ Failed to scrape {url}: {e}")
#         return ""

# # Function to extract PDF text using PyMuPDF
# def extract_text_from_pdf(pdf_path):
#     text = ""
#     try:
#         doc = fitz.open(pdf_path)
#         for page in doc:
#             text += page.get_text()
#     except Exception as e:
#         print(f"❌ Failed to extract text from {pdf_path}: {e}")
#     return text

# # Main processing logic
# def load_and_embed():
#     docs = []

#     # Scrape and convert web pages
#     for link in SCRAPE_LINKS:
#         content = scrape_to_text(link)
#         if content:
#             docs.append(Document(page_content=content, metadata={"source": link}))

#     # Extract from PDFs and save as .txt
#     for pdf_file in PDF_FILES:
#         if not os.path.isfile(pdf_file):
#             print(f"⚠️ PDF not found: {pdf_file}")
#             continue

#         content = extract_text_from_pdf(pdf_file)
#         if not content:
#             continue

#         # Save extracted text to .txt
#         txt_file = pdf_file.replace(".pdf", ".txt")
#         try:
#             with open(txt_file, "w", encoding="utf-8") as out:
#                 out.write(content)
#             print(f"📄 Saved extracted text to {txt_file}")
#         except Exception as e:
#             print(f"❌ Failed to write {txt_file}: {e}")

#         doc_name = os.path.splitext(os.path.basename(pdf_file))[0]

#         # ✅ Chunking PDF text
#         splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
#         chunks = splitter.split_text(content)

#         for chunk in chunks:
#             docs.append(Document(
#                 page_content=chunk,
#                 metadata={
#                     "source": pdf_file,
#                     "doc_name": doc_name
#                 }
#             ))

#     # Add all docs to vector DB
#     if docs:
#         db.add_documents(docs)
#         print(f"✅ Embedded {len(docs)} documents (web + PDFs).")
#     else:
#         print("⚠️ No documents were embedded. Check the links, PDFs, or scraping logic.")

# # Run
# if __name__ == "__main__":
#     load_and_embed()

























import os
import json
import hashlib
import argparse
import logging
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed

import requests_cache
from tenacity import retry, stop_after_attempt, wait_exponential
from requests import head
from bs4 import BeautifulSoup
import html2text
from langchain_chroma import Chroma
from langchain.docstore.document import Document
from langchain_huggingface import HuggingFaceEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter

# ── Command-line args ────────────────────────────────────────────────────────
parser = argparse.ArgumentParser(description="Ingest web & PDF sources into Chroma.")
parser.add_argument("--links-file", type=str, help="File with list of URLs.")
parser.add_argument("--pdf-dir", type=str, help="Directory containing PDFs.")
parser.add_argument("--persist-dir", type=str, default="chroma_db", help="Chroma DB directory.")
parser.add_argument("--chunk-size", type=int, default=1000)
parser.add_argument("--chunk-overlap", type=int, default=200)
parser.add_argument("--max-workers", type=int, default=5)
parser.add_argument("--batch-size", type=int, default=50)
args = parser.parse_args()

# ── Logging ───────────────────────────────────────────────────────────────────
logging.basicConfig(
    filename="index_data.log", level=logging.INFO,
    format="%(asctime)s %(levelname)s: %(message)s"
)

# ── Sources ─────────────────────────────────────────────────────────────────
if args.links_file and Path(args.links_file).exists():
    SCRAPE_LINKS = [l.strip() for l in open(args.links_file) if l.strip()]
else:
    # SCRAPE_LINKS = [
    #     "https://www.mentalhealth.org.uk/explore-mental-health/publications/how-to-manage-and-reduce-stress",
    #     "https://www.verywellmind.com/tips-to-reduce-stress-3145195",
    #     "https://www.helpguide.org/articles/stress/stress-management.htm",
    #     "https://www.nimh.nih.gov/health/topics/caring-for-your-mental-health",
    #     "https://www.mind.org.uk/information-support/tips-for-everyday-living/",
    #     "https://psychcentral.com/stress/how-to-calm-an-anxious-mind",
    #     "https://www.betterhelp.com/advice/stress/10-effective-ways-to-manage-stress/",
    #     "https://adaa.org/tips-manage-anxiety-and-stress",
    #     "https://www.medicalnewstoday.com/articles/how-to-deal-with-stress",
    #     "https://www.headspace.com/articles/stress",
    #     "https://www.psycom.net/depression.central.html",
    #     "https://www.psychologytoday.com/us/basics/depression",
    #     "https://www.psychologytoday.com/us/basics/anxiety",
    #     "https://www.webmd.com/depression/guide/depression-overview",
    #     "https://www.mayoclinic.org/diseases-conditions/depression/in-depth/depression/art-20045943",
    #     "https://www.mindful.org/what-is-mindfulness/",
    #     "https://www.mentalhealth.gov/basics/what-is-mental-health",
    #     "https://www.apa.org/topics/mental-health/",
    #     "https://www.cdc.gov/mentalhealth/learn/index.htm",
    #     "https://www.nami.org/About-Mental-Illness",
    # ]

    SCRAPE_LINKS = [
    # Your existing links
    "https://www.mentalhealth.org.uk/explore-mental-health/publications/how-to-manage-and-reduce-stress",
    "https://www.verywellmind.com/tips-to-reduce-stress-3145195",
    "https://www.helpguide.org/articles/stress/stress-management.htm",
    "https://www.nimh.nih.gov/health/topics/caring-for-your-mental-health",
    "https://www.mind.org.uk/information-support/tips-for-everyday-living/",
    "https://psychcentral.com/stress/how-to-calm-an-anxious-mind",
    "https://www.betterhelp.com/advice/stress/10-effective-ways-to-manage-stress/",
    "https://adaa.org/tips-manage-anxiety-and-stress",
    "https://www.medicalnewstoday.com/articles/how-to-deal-with-stress",
    "https://www.headspace.com/articles/stress",
    "https://www.psycom.net/depression.central.html",
    "https://www.psychologytoday.com/us/basics/depression",
    "https://www.psychologytoday.com/us/basics/anxiety",
    "https://www.webmd.com/depression/guide/depression-overview",
    "https://www.mayoclinic.org/diseases-conditions/depression/in-depth/depression/art-20045943",
    "https://www.mindful.org/what-is-mindfulness/",
    "https://www.mentalhealth.gov/basics/what-is-mental-health",
    "https://www.apa.org/topics/mental-health/",
    "https://www.cdc.gov/mentalhealth/learn/index.htm",
    "https://www.nami.org/About-Mental-Illness",
    
    # Newly added emotional support links
    "https://www.helpguide.org/articles/grief/coping-with-grief-and-loss.htm",
    "https://www.verywellmind.com/how-to-practice-self-compassion-4164960",
    "https://www.betterup.com/blog/emotional-support",
    "https://psychcentral.com/lib/how-to-give-and-receive-emotional-support",
    "https://www.mind.org.uk/information-support/types-of-mental-health-problems/",
    "https://www.nami.org/Support-Education/Support-Groups",
    "https://www.mentalhealth.org.uk/explore-mental-health/a-z-topics/workplace-mental-health",
    "https://www.mayoclinic.org/healthy-lifestyle/adult-health/in-depth/mental-health/art-20046477",
    "https://www.healthline.com/health/building-a-support-system",
    "https://positivepsychology.com/emotional-support/",
]

PDF_FILES = []
if args.pdf_dir and Path(args.pdf_dir).exists():
    PDF_FILES = [str(p) for p in Path(args.pdf_dir).glob("*.pdf")]
else:
    PDF_FILES = [
        r"C:\Users\bharg\OneDrive\Documents\CalmConnect\WellbeingMentalWellness2020-final.pdf",
        r"C:\Users\bharg\OneDrive\Documents\CalmConnect\wellbeing-team-cbt-workshop-booklet-2016.pdf",
        r"C:\Users\bharg\OneDrive\Documents\CalmConnect\YogaForAnxietyandDepression-HarvardMedicalStudy.pdf",
        r"C:\Users\bharg\OneDrive\Documents\CalmConnect\Pilkington-2005-YogafordepressionTheresearchevidence.pdf",
        r"C:\Users\bharg\OneDrive\Documents\CalmConnect\UNICEF-MH-and-PS-Technical-Note-2019.pdf.pdf",
    ]

# ── HTTP cache + change detection ────────────────────────────────────────────
requests_cache.install_cache("webcache", expire_after=86400)
META_FILE = "source_meta.json"
meta = json.load(open(META_FILE)) if Path(META_FILE).exists() else {}

@retry(stop=stop_after_attempt(3), wait=wait_exponential(min=1, max=10))
def fetch_if_changed(url: str) -> str | None:
    """
    HEAD to check ETag/Last-Modified. Skip and return None on 403 or 405.
    """
    try:
        h = head(url, timeout=5)
        h.raise_for_status()
    except Exception as e:
        status = getattr(e.response, "status_code", None)
        if status in (403, 405):
            logging.warning(f"{status} for HEAD {url}: skipping")
            return None
        logging.warning(f"HEAD error {url}: {e}")
        raise

    from requests import Session
    session = Session()
    resp = session.get(url)
    try:
        resp.raise_for_status()
    except Exception as e:
        status = resp.status_code
        if status in (403, 405):
            logging.warning(f"{status} for GET {url}: skipping")
            return None
        logging.warning(f"GET error {url}: {e}")
        raise

    meta[url] = {
        "etag": h.headers.get("ETag") or h.headers.get("Last-Modified"),
        "hash": hashlib.md5(resp.content).hexdigest()
    }
    return resp.text

# ── Vector DB setup ─────────────────────────────────────────────────────────
embedding_fn = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
db = Chroma(persist_directory=args.persist_dir, embedding_function=embedding_fn)
splitter = RecursiveCharacterTextSplitter(chunk_size=args.chunk_size, chunk_overlap=args.chunk_overlap)

# ── Scrape & extract helpers ─────────────────────────────────────────────────
def scrape_to_text(url: str) -> str:
    html = fetch_if_changed(url)
    if not html:
        return ""
    soup = BeautifulSoup(html, "html.parser")
    for tag in soup(["script", "style"]):
        tag.decompose()
    return html2text.html2text(soup.get_text(separator=" "))

def extract_text_from_pdf(path: str) -> str:
    try:
        import fitz
        doc = fitz.open(path)
        return "\n".join(page.get_text() for page in doc)
    except Exception as e:
        logging.warning(f"PDF extract failed {path}: {e}")
        return ""

# ── Main ingestion & embedding ───────────────────────────────────────────────
def load_and_embed():
    docs = []

    # Parallel web scraping
    with ThreadPoolExecutor(max_workers=args.max_workers) as exe:
        futures = {exe.submit(scrape_to_text, u): u for u in SCRAPE_LINKS}
        for fut in as_completed(futures):
            u = futures[fut]
            content = fut.result()
            if content:
                docs.append(Document(page_content=content, metadata={"source": u}))
            else:
                logging.info(f"Skipped {u}")

    # PDF extraction + chunking
    for pdf in PDF_FILES:
        if not os.path.isfile(pdf):
            logging.warning(f"PDF not found: {pdf}")
            continue
        txt = extract_text_from_pdf(pdf)
        if not txt:
            continue
        Path(pdf).with_suffix(".txt").write_text(txt, encoding="utf-8")
        for chunk in splitter.split_text(txt):
            docs.append(Document(page_content=chunk, metadata={"source": pdf}))

    # Batch embedding
    for i in range(0, len(docs), args.batch_size):
        batch = docs[i : i + args.batch_size]
        db.add_documents(batch)
        logging.info(f"Embedded batch {i//args.batch_size +1} ({len(batch)} docs)")
    logging.info(f"Total embedded: {len(docs)} docs")

    # Save metadata
    with open(META_FILE, "w") as f:
        json.dump(meta, f, indent=2)

if __name__ == "__main__":
    load_and_embed()
