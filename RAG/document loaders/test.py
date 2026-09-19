from langchain_community.document_loaders import TextLoader

data = TextLoader(r"C:\Users\hardi\OneDrive\Desktop\Gen_Ai\RAG\document loaders\dotnet-applied-ai-summary.txt")
# the r string at the starting of the file path is used to indicate that it is a raw string. 
# Which tells Python to treat backslashes as literal characters and not as escape characters. 
docs = data.load()

print(docs[0]) # This shows the first document in the list of documents. 
# Document is a kind of list which contains two things : metadata and page content.  