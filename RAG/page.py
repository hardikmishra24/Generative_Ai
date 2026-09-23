from langchain_community.document_loaders import WebBaseLoader

url = "https://jecrcfoundation.com/"

data = WebBaseLoader(url)  # Creates an object of WebBaseLoader class named data and provides the URL to WebBaseLoader class.
docs = data.load()  # Loads the document from the URL specified in data and returns a list of Document objects containing page content and metadata.

print(docs[0].page_content)  # Prints the page content of the first document in the list.