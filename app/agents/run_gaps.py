from app.agents.gap_detector import find_conflicts

report = find_conflicts()
print(f"Found {len(report.conflicts)} conflicts\n")
for i, c in enumerate(report.conflicts, 1):
    print(f"{i}. {c.topic} [{c.severity.upper()}]")
    print(f"   {c.document_a}: {c.statement_a}")
    print(f"   {c.document_b}: {c.statement_b}")
    print(f"   Ask: {c.suggested_question}\n")