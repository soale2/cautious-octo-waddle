import os
import json
from django.shortcuts import render
from django.http import JsonResponse
from difflib import SequenceMatcher

KNOWLEDGE_BASE_PATH = os.path.join(os.path.dirname(__file__), 'knowledge_base.json')

def chatbot(request):
    return render(request, 'chatbot_app/chatbot.html')

def load_knowledge_base():
    with open(KNOWLEDGE_BASE_PATH, 'r') as file:
        knowledge_base = json.load(file)
    return knowledge_base

def get_best_match(query, questions):
    best_match = None
    max_similarity = 0

    for qna in questions:
        similarity = SequenceMatcher(None, qna['question'].lower(), query.lower()).ratio()
        if similarity > max_similarity:
            max_similarity = similarity
            best_match = qna

    return best_match

def chatbot_api_view(request):
    knowledge_base = load_knowledge_base()

    if request.method == 'POST':
        data = json.loads(request.body)
        query = data.get('query')

        # Search for the best matching question across all topics
        best_match = None
        max_similarity = 0

        for topic, questions in knowledge_base.items():
            match = get_best_match(query, questions)
            if match:
                similarity = SequenceMatcher(None, match['question'].lower(), query.lower()).ratio()
                if similarity > max_similarity:
                    max_similarity = similarity
                    best_match = match

        if best_match:
            answer = best_match['answer']
            return JsonResponse({'response': answer})

        # No answer found for the question
        response_message = f"No answer found for the question '{query}'"
        return JsonResponse({'response': response_message})

    return JsonResponse({})
