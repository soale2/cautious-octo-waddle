import nltk
from difflib import SequenceMatcher

nltk.download('punkt')

def get_best_match(query, questions):
    best_match = None
    max_similarity = 0

    for qna in questions:
        similarity = SequenceMatcher(None, qna['question'].lower(), query.lower()).ratio()
        if similarity > max_similarity:
            max_similarity = similarity
            best_match = qna

    return best_match
