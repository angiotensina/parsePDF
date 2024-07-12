
# bring in deps
from llama_parse import LlamaParse
from llama_index.core import SimpleDirectoryReader
from llama_index.core import (
    VectorStoreIndex,
    SimpleDirectoryReader,
    StorageContext, 
    ServiceContext
)
import os
from dotenv import load_dotenv, find_dotenv

# Carga las variables de entorno desde un archivo .env
load_dotenv(find_dotenv(), override=True)

# Obtiene la API key de OpenAI desde las variables de entorno
api_key_openAI = os.environ.get("OPENAI_API_KEY")

# set up parser
parser = LlamaParse(
    result_type="markdown"  # "markdown" and "text" are available
)

# use SimpleDirectoryReader to parse our file
file_extractor = {".pdf": parser}
documents = SimpleDirectoryReader(input_files=['./PDF/still.pdf'], file_extractor=file_extractor).load_data()

#print(documents)


# one extra dep
from llama_index.core import VectorStoreIndex

from llama_index.embeddings.openai import OpenAIEmbedding
from llama_index.llms.openai import OpenAI
from llama_index.core import Settings


MODEL_NAME = "gpt-4o"
EMBEDDING_MODEL = "text-embedding-3-large"

Settings.llm = OpenAI(model=MODEL_NAME, api_key=api_key_openAI)
Settings.embed_model = OpenAIEmbedding(model=EMBEDDING_MODEL, api_key=api_key_openAI)

# create an index from the parsed markdown
index = VectorStoreIndex.from_documents(documents, settings=Settings)

# create a query engine for the index
query_engine = index.as_query_engine()

# query the engine
query = "Que es la enfermedad de still"
response = query_engine.query(query)
print(response)


