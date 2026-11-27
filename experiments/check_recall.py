from app.agents.gap_detector import find_conflicts

# Answer key: each planted conflict and the words that identify it
EXPECTED = {
    "age limit": ["60", "65"],
    "credit score": ["700", "650"],
    "self-employed": ["not eligible", "allowed"],
    "approval limit": ["5 lakh", "3 lakh"],
    "processing time": ["7 working", "5 working"],
    "documents": ["6 months", "3 months"],
}

report = find_conflicts()
found = 0
for name, keywords in EXPECTED.items():
    hit = any(
        all(k in (c.statement_a + " " + c.statement_b) for k in keywords)
        for c in report.conflicts
    )
    print(f"{'FOUND ' if hit else 'MISSED'} {name}")
    found += hit

print(f"\nRecall: {found} of {len(EXPECTED)} planted conflicts found")
print(f"Total reported: {len(report.conflicts)}")