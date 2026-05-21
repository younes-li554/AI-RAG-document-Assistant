from collections import deque

class MemoryManager:
    def __init__(self, max_history=10):
        """
        max_history: maximum number of stored messages (user + assistant)
        """
        self.history = deque(maxlen=max_history)

    def add_message(self, role, message):
        """
        Add a message to memory.

        Args:
            role (str): 'user' or 'assistant'
            message (str): message content
        """
        self.history.append({
            "role": role,
            "message": message
        })

    def get_history(self):
        """
        Return full chat history as a list.
        """
        return list(self.history)

    def format_history(self):
        """
        Convert chat history into a string format for prompts.
        """
        formatted = ""

        for msg in self.history:
            if msg["role"] == "user":
                formatted += f"User: {msg['message']}\n"
            else:
                formatted += f"Assistant: {msg['message']}\n"

        return formatted.strip()

    def clear(self):
        """
        Clear all stored memory.
        """
        self.history.clear()