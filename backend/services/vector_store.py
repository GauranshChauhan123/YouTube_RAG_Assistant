from backend.utils.embedding_model import get_embedding_model
from langchain_chroma import Chroma


#generate embeddings and create vector store
def create_vector_store(chunks,video_id):
    try:
       embedding_function = get_embedding_model()
       vector_store = Chroma.from_documents(
       documents=chunks,
        embedding=embedding_function,
        collection_name=video_id,
        persist_directory="chroma_db"
       )

       return vector_store
    except Exception as e:
        print('error while creating vector store', e)
