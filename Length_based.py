from langchain.text_splitter import CharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader('dl-curriculum.pdf')

docs = loader.load() # no of documents = no of pages in pdf

splitter = CharacterTextSplitter(
    chunk_size=200,
    chunk_overlap=0, #it means no overlap (default is 20) in more simple words it means no repeated text in chunks
    separator='' #it means no separator i.e. split by characters only
)

result = splitter.split_documents(docs)  #spli text is used to split the text into chunks while split_documents is used to split the documents into chunks

print(result[1].page_content) #print second chunk without metadata
print(result[0]) #print first chunk plus metadata