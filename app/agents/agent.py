# agents/agent.py

class SimpleAgent:
    """
    A lightweight agent that decides whether to use:
    - RAG (vector database)
    - Direct LLM response
    """

    def __init__(self, vectorstore, llm):
        self.vectorstore = vectorstore
        self.llm = llm

    def decide(self, question):
        """
        Decide whether the question needs document retrieval or not.
        """

        router_prompt = f"""
You are a routing system.

Decide if the question needs DOCUMENT knowledge or GENERAL knowledge.

Return ONLY one word:
- "rag" → if the answer is likely inside the uploaded document
- "llm" → if it's a general question

Question:
{question}
"""

        result = self.llm.invoke(router_prompt).lower()

        if "rag" in result:
            return "rag"
        else:
            return "llm"

    def run(self, question, chat_history=""):
        """
        Execute the correct pipeline based on decision.
        """

        decision = self.decide(question)

        # =========================
        # CASE 1: RAG
        # =========================
        if decision == "rag":

            retriever = self.vectorstore.as_retriever()
            docs = retriever.get_relevant_documents(question)

            context = "\n\n".join([d.page_content for d in docs])

            prompt = f"""
Use ONLY the context to answer.

Context:
{context}

Chat History:
{chat_history}

Question:
{question}

Answer:
"""

            return self.llm.invoke(prompt)

        # =========================
        # CASE 2: LLM ONLY
        # =========================
        else:

            prompt = f"""
Answer the question normally.

Chat History:
{chat_history}

Question:
{question}

Answer:
"""

            return self.llm.invoke(prompt)