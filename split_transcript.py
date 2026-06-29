from langchain_text_splitters import RecursiveCharacterTextSplitter

def split_transcript(transcript):
    try:
       
       splitter= RecursiveCharacterTextSplitter(chunk_size=1000,chunk_overlap=200)       
       documents=splitter.create_documents([transcript])
       
       return documents
    
    except Exception as e:
        print('error :',e)
