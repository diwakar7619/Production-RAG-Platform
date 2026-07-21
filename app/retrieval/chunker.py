from langchain_text_splitters import RecursiveCharacterTextSplitter

TEXT_SPLITTER = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50,
    length_function=len,
    separators=["\n\n", "\n", " ", ""],
)


def chunk_document(text: str) -> list[str]:
    return TEXT_SPLITTER.split_text(text)
