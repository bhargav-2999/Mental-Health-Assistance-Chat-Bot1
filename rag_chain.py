



















# import os
# import logging
# from dotenv import load_dotenv
# from langchain.chains import RetrievalQA
# from langchain.prompts import PromptTemplate
# from langchain_chroma import Chroma
# from langchain_huggingface import HuggingFaceEmbeddings
# from langchain_groq import ChatGroq
# from langchain_core.messages import AIMessage
# from functools import lru_cache

# # Load environment variables
# load_dotenv()
# groq_api_key = os.getenv("GROQ_API_KEY")
# if not groq_api_key:
#     raise ValueError("🚫 GROQ_API_KEY is missing!")

# # Set up logging
# logging.basicConfig(
#     filename="rag_chain.log",
#     level=logging.INFO,
#     format="%(asctime)s %(levelname)s:%(message)s"
# )

# @lru_cache(maxsize=1)
# def get_resources():
#     """
#     Initialize and cache the LLM, retriever, and QA chain.
#     """
#     # LLM client
#     llm = ChatGroq(groq_api_key=groq_api_key, model_name="llama3-8b-8192")

#     # Embedding function and vector DB
#     embedding_fn = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
#     vectordb = Chroma(persist_directory="chroma_db", embedding_function=embedding_fn)
#     retriever = vectordb.as_retriever(search_kwargs={"k": 2})

#     # Prompt template for RAG
#     prompt_template = PromptTemplate(
#         input_variables=["context", "question"],
#         template="""
# You are a friendly, non-medical mental wellness assistant.
# Use the provided context to answer calmly and helpfully.

# Context:
# {context}

# Question:
# {question}

# Answer:
# """
#     )

#     # Build RetrievalQA chain
#     qa_chain = RetrievalQA.from_chain_type(
#         llm=llm,
#         retriever=retriever,
#         chain_type="stuff",
#         chain_type_kwargs={"prompt": prompt_template}
#     )

#     return llm, retriever, qa_chain

# # Retrieve cached resources
# _llm, _retriever, _qa_chain = get_resources()


# def summarize_history(messages: list[dict]) -> str:
#     """
#     Summarize chat history into three lines using the LLM.
#     """
#     if not messages:
#         return ""
#     text = "".join(
#         f"{'User' if m['role']=='user' else 'Assistant'}: {m['text']}\n" for m in messages
#     )
#     summary_prompt = f"Summarize this chat in 3 lines or less:\n\n{text}\nSummary:"
#     try:
#         res = _llm.invoke(summary_prompt)
#         return res.content.strip() if isinstance(res, AIMessage) else str(res).strip()
#     except Exception as e:
#         logging.warning(f"Failed to summarize history: {e}")
#         return ""


# def ask_bot(query: str, history: list[dict], previous: list[dict] = []) -> str:
#     """
#     Given a user query, chat history, and previous messages,
#     perform retrieval-augmented generation and return the answer.
#     """
#     try:
#         # Build recent context and summary
#         recent = "".join(
#             f"{'User' if m['role']=='user' else 'Assistant'}: {m['text']}\n" for m in history[-2:]
#         )
#         summary = summarize_history(previous)
#         full_context = (summary + "\n" + recent).strip() if summary else recent

#         # Truncate if too long
#         words = full_context.split()
#         if len(words) > 1000:
#             full_context = " ".join(words[:1000]) + "..."

#         # Retrieve relevant docs
#         try:
#             docs = _retriever.get_relevant_documents(full_context)
#         except Exception as e:
#             logging.warning(f"Retrieval error: {e}")
#             docs = []

#         # Prepare source tags
#         sources = sorted({doc.metadata.get("source") for doc in docs if doc.metadata.get("source")})
#         source_tag = f"\n\n[sources: {', '.join(sources)}]" if sources else ""

#         # Invoke QA chain
#         result = _qa_chain.invoke({"query": full_context})
#         answer = result.get("result", "").strip()
#         if not answer:
#             raise ValueError("Empty LLM response")
#         return answer + source_tag

#     except Exception as e:
#         logging.error(f"ask_bot error: {e}")
#         return "🧘 I’m still thinking about that. Could you rephrase?"


# if __name__ == "__main__":
#     while True:
#         user_q = input("Ask the bot (or type 'exit'): ")
#         if user_q.lower() == "exit":
#             break
#         print("Bot:", ask_bot(user_q, [], []))






import os
import logging
from dotenv import load_dotenv
from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate
from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_groq import ChatGroq
from langchain_core.messages import AIMessage
from functools import lru_cache

# Load environment variables
load_dotenv()
groq_api_key = os.getenv("GROQ_API_KEY")
if not groq_api_key:
    raise ValueError("🚫 GROQ_API_KEY is missing!")

# Set up logging
logging.basicConfig(
    filename="rag_chain.log",
    level=logging.INFO,
    format="%(asctime)s %(levelname)s:%(message)s"
)

@lru_cache(maxsize=1)
def get_resources():
    """
    Initialize and cache the LLM, retriever, and QA chain.
    """
    # LLM client
    llm = ChatGroq(groq_api_key=groq_api_key, model_name="llama3-8b-8192")

    # Embedding function and vector DB
    embedding_fn = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    vectordb = Chroma(persist_directory="chroma_db", embedding_function=embedding_fn)
    retriever = vectordb.as_retriever(search_kwargs={"k": 2})

    # Prompt template for RAG
    prompt_template = PromptTemplate(
        input_variables=["context", "question"],
        template="""
You are a friendly, non-medical mental wellness assistant.
Use the provided context to answer calmly and helpfully.

Context:
{context}

Question:
{question}

Answer:
"""
    )

    # Build RetrievalQA chain
    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=retriever,
        chain_type="stuff",
        chain_type_kwargs={"prompt": prompt_template}
    )

    return llm, retriever, qa_chain

# Retrieve cached resources
_llm, _retriever, _qa_chain = get_resources()


def summarize_history(messages: list[dict]) -> str:
    """
    Summarize chat history into three lines using the LLM.
    """
    if not messages:
        return ""
    text = "".join(
        f"{'User' if m['role']=='user' else 'Assistant'}: {m['text']}\n" 
        for m in messages
    )
    summary_prompt = f"Summarize this chat in 3 lines or less:\n\n{text}\nSummary:"
    try:
        res = _llm.invoke(summary_prompt)
        return res.content.strip() if isinstance(res, AIMessage) else str(res).strip()
    except Exception as e:
        logging.warning(f"Failed to summarize history: {e}")
        return ""


def ask_bot(query: str, history: list[dict], previous: list[dict] = []) -> str:
    """
    Given a user query, chat history, and previous messages,
    perform retrieval-augmented generation and return the answer.
    """
    try:
        # Build recent context and summary
        recent = "".join(
            f"{'User' if m['role']=='user' else 'Assistant'}: {m['text']}\n" 
            for m in history[-2:]
        )
        summary = summarize_history(previous)
        full_context = (summary + "\n" + recent).strip() if summary else recent

        # Truncate if too long
        words = full_context.split()
        if len(words) > 1000:
            full_context = " ".join(words[:1000]) + "..."

        # Retrieve relevant docs
        try:
            docs = _retriever.get_relevant_documents(full_context)
        except Exception as e:
            logging.warning(f"Retrieval error: {e}")
            docs = []

        # Prepare source tags
        sources = sorted({doc.metadata.get("source") for doc in docs if doc.metadata.get("source")})
        source_tag = f"\n\n[sources: {', '.join(sources)}]" if sources else ""

        # Invoke QA chain
        result = _qa_chain.invoke({"query": full_context})
        answer = result.get("result", "").strip()
        if not answer:
            raise ValueError("Empty LLM response")
        return answer + source_tag

    except Exception as e:
        logging.error(f"ask_bot error: {e}")
        # Empathy-first fallback for emotional distress
        distress_keywords = ["fed up", "hopeless", "worthless", "give up", "tired of", "can't go on"]
        if any(kw in query.lower() for kw in distress_keywords):
            empathy_prompt = (
                "You are an empathetic mental wellness companion. "
                f"The user is in distress: \"{query}\". "
                "First respond with genuine empathy and validation, then suggest one small step they can take right now."
            )
            try:
                resp = _llm.invoke(empathy_prompt)
                return (resp.content if hasattr(resp, "content") else str(resp)).strip()
            except Exception as e2:
                logging.warning(f"Empathy fallback failed: {e2}")
                return "🧘 I’m here for you. It sounds like you’re going through a lot. Would you like to share more about what’s on your mind?"
        # Standard fallback
        return "🧘 I’m still thinking about that. Could you rephrase?"


if __name__ == "__main__":
    while True:
        user_q = input("Ask the bot (or type 'exit'): ")
        if user_q.lower() == "exit":
            break
        print("Bot:", ask_bot(user_q, [], []))
