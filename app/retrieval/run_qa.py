from app.retrieval.qa import answer

for q in [
    "What is the minimum credit score?",
    "Can self-employed people apply?",
    "What is the capital of France?",
]:
    print("Q:", q)
    print(answer(q))
    print()