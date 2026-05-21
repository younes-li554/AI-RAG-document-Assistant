from app.utils.document_loader import load_document

def test_load():
    docs = load_document("sample.txt", "sample.txt")
    assert len(docs) > 0