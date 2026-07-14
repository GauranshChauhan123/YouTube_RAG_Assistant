from langchain_core.prompts import PromptTemplate

def prompt_template(query, relevant_docs):
    context = "\n\n".join(
        doc.page_content for doc in relevant_docs
    )
    template= PromptTemplate(
                 template='''You are a helpful assistant that answers questions based only on the provided context.

            Instructions:
             - Use the context to answer the question.
             - If the answer is not present in the context, say:
                   "I could not find the answer in the provided video content."
             - Be concise and accurate.
             

             Context:
             {context}

             Question:
             {query}

             Answer:
                  ''',
             input_variables=['context','query']
       
                    )
    return template.format(
         context=context,
         query=query
                 )
    
