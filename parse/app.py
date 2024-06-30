import nest_asyncio
import os
from llama_parse import LlamaParse
from llama_index.core import SimpleDirectoryReader
from dotenv import load_dotenv, find_dotenv

nest_asyncio.apply()

# Carga las variables de entorno desde un archivo .env
load_dotenv(find_dotenv(), override=True)

# Obtiene la API key de OpenAI desde las variables de entorno
llama_key = os.environ.get("LLAMA_CLOUD_API_KEY")

parser = LlamaParse(
    api_key= llama_key,
    result_type="text",  # "markdown" and "text" are available
    parsing_instruction=
    """
    - Elimina encabezados, numeracion y pies de pagina de cada pagina del PDF.
    - organiza tablas en lineas de texto.
    """,
    verbose=True,
)

file_extractor = {".pdf": parser}
documents = SimpleDirectoryReader(
    "./EPID", file_extractor=file_extractor
).load_data()

#print(documents[0].text)

filename = "output_tx.txt"
with open(filename, "w") as f:
    f.write(documents[0].text)