from app.agents.gap_detector import find_conflicts
from app.retrieval.vectorstore import get_all_chunks

source_text = {}
for chunk in get_all_chunks():
    source_text[chunk["source"]] = source_text.get(chunk["source"], "") + "\n" + chunk["text"]

report = find_conflicts()
bad = 0
for c in report.conflicts:
    ok_a = c.statement_a in source_text.get(c.document_a, "")
    ok_b = c.statement_b in source_text.get(c.document_b, "")
    if not (ok_a and ok_b):
        bad += 1
        print("NOT FOUND IN SOURCE:", c.topic)

print(f"{len(report.conflicts) - bad} of {len(report.conflicts)} conflicts have verbatim quotes")