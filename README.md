🎬 YouTube Assistant using LangChain + Mistral
An AI-powered YouTube assistant that answers questions about videos by extracting, chunking, embedding, and analyzing their transcripts.
Built with LangChain, MistralAI, and FAISS for fast, accurate retrieval and response generation.

🚀 Features
📜 Automatic transcript extraction from YouTube videos

✂ Smart text chunking & embedding with MistralAIEmbeddings

📂 Stores vectors in FAISS for lightning-fast searches

🔍 Retrieves relevant chunks using semantic similarity

🤖 Generates natural language answers with ChatMistralAI

🛠 Modular design for easy RAG pipeline extensions

🧠 How It Works
Transcript Extraction
Uses YoutubeLoader from LangChain Community to fetch transcript data.

Chunking & Embedding
Splits text using RecursiveCharacterTextSplitter, then embeds it with MistralAIEmbeddings.

Vector Store
Saves embeddings in a FAISS vector store for fast similarity search.

RAG-Style Querying
Searches for relevant transcript chunks and injects them into a custom prompt.

LLM Response Generation
Generates context-aware answers using ChatMistralAI.

🛠 Tech Stack
Component	Tool/Library
Language Model	MistralAI (ChatMistralAI)
Framework	LangChain
Embeddings	MistralAIEmbeddings
Vector DB	FAISS
Transcripts	YoutubeLoader
Prompting	PromptTemplate + RunnableSequence
Env Vars	python-dotenv

📦 Installation
Clone the repository
git clone https://github.com/your-username/Youtube-Assistant.git
cd Youtube-Assistant














