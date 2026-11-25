# ba-copilot# BA Copilot

An AI assistant for business analysts. It answers questions about policy and
requirements documents with citations to the source file, and (in progress)
detects contradictions between old and new documents.

## Problem
When a process changes, rules end up spread across old policies and new BRDs.
Contradictions are often found late, during testing. BA Copilot finds answers
and conflicts quickly, with sources.

## How it works
Document -> chunks -> embeddings -> Chroma -> retrieval -> LLM -> cited answer

## Status
- [x] Document loading and chunking
- [x] Embeddings and vector search (Chroma)
- [x] Question answering with citations
- [x] FastAPI endpoint
- [ ] Contradiction detector
- [ ] Evaluation set
- [ ] Streamlit UI and AWS deployment

## Run it
pip install -r requirements.txt
Add OPENAI_API_KEY to a .env file
python -m app.retrieval.run_qa