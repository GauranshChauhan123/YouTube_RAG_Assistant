from langchain_chroma import Chroma
from utils import get_embedding_model


def retrieve_related_info(query: str, video_id: str, k: int = 5):
    """Perform semantic search on the persisted vector store and return the most relevant chunks."""
    try:
        embedding_function= get_embedding_model()
        vector_store = Chroma(
            collection_name=video_id,
            embedding_function=embedding_function,
            persist_directory="chroma_db"
        )

        relevant_docs = vector_store.max_marginal_relevance_search(
                                            query=query,
                                            k=k,
                                            fetch_k=20
                                                                 )
        
        return relevant_docs
    except Exception as e:
        print("error during semantic retrieval:", e)
        return []
