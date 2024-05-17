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
    persist_directory="./vector_db",
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


def rag(question):
    response = qa_chain({"question": question})
    print(response.get("answer"))

    return response.get("answer")




# question = input("Enter your question: ")
# rag(question)
