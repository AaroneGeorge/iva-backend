from langchain_community.embeddings.sentence_transformer import SentenceTransformerEmbeddings
from langchain_community.vectorstores import Chroma
from langchain.prompts import PromptTemplate
from langchain.chains import ConversationalRetrievalChain
from langchain_openai import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from decouple import config

embedding_function = SentenceTransformerEmbeddings(
    model_name="all-MiniLM-L6-v2"
)

vector_db = Chroma(
    persist_directory="../vector_db",
    collection_name="iva_train",
    embedding_function=embedding_function,
)


# create prompt
QA_prompt = PromptTemplate(
    template="""Use the following pieces of context to answer the user question.
chat_history: {chat_history}
Context: {text}
Question: {question}
Answer:""",
    input_variables=["text", "question", "chat_history"]
)

# create chat model
llm = ChatOpenAI(openai_api_key=config("OPEN_AI_KEY"), temperature=0)

# create memory
memory = ConversationBufferMemory(
    return_messages=True, memory_key="chat_history")

# create retriever chain
qa_chain = ConversationalRetrievalChain.from_llm(
    llm=llm,
    memory=memory,
    retriever=vector_db.as_retriever(
        search_kwargs={'fetch_k': 1, 'k': 1}, search_type='mmr'),
    chain_type="refine",
)

u_history = {}

def rag(question: str, uid: str) -> str:
    if uid not in u_history:
        u_history[uid] = []
    
    user_message = {"sender": "user", "content": question}
    u_history[uid].append(user_message)
    
    chat_history = [msg for msg_list in u_history.values() for msg in msg_list]
    
    response = qa_chain({"question": question, "chat_history": chat_history})
    
    assistant_message = {"sender": "assistant", "content": response.get("answer")}
    u_history[uid].append(assistant_message)
    
    return response.get("answer")

ans = rag("my ac is not working", "u123")
print(ans)
print(u_history)

ans = rag("what is your name", "u456")
print(ans)
print(u_history)

ans = rag("set me an alarm", "u123")
print(ans)
print(u_history)

ans = rag("what did i ask you before", "u123")
print(ans)
print(u_history)
