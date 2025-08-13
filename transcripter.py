from langchain_community.document_loaders import YoutubeLoader
from langchain_core.runnables import RunnableSequence
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain_community.vectorstores import FAISS
from langchain_mistralai.chat_models import ChatMistralAI
from langchain_mistralai import MistralAIEmbeddings

import faiss

import warnings

from dotenv import load_dotenv

warnings.filterwarnings("ignore")

# load the environment variables
load_dotenv()

# embedding model from Mistral
embeddings = MistralAIEmbeddings(model="mistral-embed")

def create_video_embeddings(url: str):
    if url!="":
        loader = YoutubeLoader.from_youtube_url(url)
        transcript = loader.load()
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=150)
        docs = text_splitter.split_documents(transcript)
        db = FAISS.from_documents(docs, embedding=embeddings)

        return db
    return None


def get_response_from_query(db: FAISS, query: str, k: int=4):
    if db is not None:
        docs = db.similarity_search(query, k=k)
        docs_page_content = "\n".join(doc.page_content for doc in docs)

        llm = ChatMistralAI(model_name="mistral-small-2506", temperature=0.8)

        prompt = PromptTemplate(
            input_variables=["question", "docs"],
            template="""
            You are a helpful YouTube assistant that answers questions about videos based on the video's transcripts.
            Answer the following question: {question} by searching the following video transcript:
            {docs}.
            Only use the video transcripts to answer the questions.
            If there is no question provided, summarize the video transcript.
            Your answers should be in a paragraph.
            If you don't know the answer, just say, "You don't know".
            """
        )

        #chain = LLMChain(llm=llm, prompt=prompt)
        chain = RunnableSequence(prompt | llm)

        response = chain.invoke({"question": query, "docs": docs_page_content})

        return response

    return None
