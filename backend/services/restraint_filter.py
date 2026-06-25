from typing import List


class RestraintFilter:
    def __init__(self, restricted_terms: List[str] = None):
        self.restricted_terms = restricted_terms or []

    def is_allowed(self, text: str) -> bool:
        return not any(term.lower() in text.lower() for term in self.restricted_terms)
