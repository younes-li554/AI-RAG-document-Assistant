# prompts/prompt_builder.py

def build_prompt(context, chat_history, question):
    """
    Build a structured prompt for Conversational RAG system.

    This prompt combines:
    - Retrieved document context
    - Chat history (memory)
    - Current user question
    """

    prompt = f"""
You are a helpful AI assistant that answers questions based ONLY on the provided context.

If the answer is not found in the context, clearly say:
"I don't have enough information in the document."

---

📚 CONTEXT:
{context}

---

💬 CHAT HISTORY:
{chat_history}

---

❓ USER QUESTION:
{question}

---

🎯 INSTRUCTIONS:
- Use ONLY the provided context
- Use chat history to understand references (like "it", "this", etc.)
- Be accurate and concise
- Do not hallucinate or guess
- If unsure, say you don't know

ANSWER:
"""
    return prompt.strip()