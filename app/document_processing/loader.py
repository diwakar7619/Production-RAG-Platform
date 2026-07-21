import pymupdf
import docx


def load_document(file_path: str) -> str:
    if file_path.endswith(".pdf"):
        return _load_pdf(file_path)
    elif file_path.endswith(".txt"):
        return _load_txt(file_path)
    elif file_path.endswith(".docx"):
        return _load_docx(file_path)
    else:
        raise ValueError(
            f"Unsupported file format: {file_path}\nSupported formats are: .pdf, .txt, .docx"
        )


def _load_pdf(file_path: str) -> str:
    with pymupdf.open(file_path) as doc:
        text = []
        for page in doc:
            text.append(page.get_text())
    return "\n".join(text)


def _load_txt(file_path: str) -> str:
    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()


def _load_docx(file_path: str) -> str:
    doc = docx.Document(file_path)
    text = []
    for para in doc.paragraphs:
        text.append(para.text)
    return "\n".join(text)
