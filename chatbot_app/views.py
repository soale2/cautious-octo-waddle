from . import config
import requests
import json
from django.shortcuts import render
from django.http import JsonResponse

CLIENT_ID = config.CLIENT_ID
CLIENT_SECRET = config.CLIENT_SECRET
API_KEY = config.API_KEY


def chatbot(request):
    return render(request, 'chatbot_app/chatbot.html')

def chatbot_api_view(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        query = data.get('query')

        # Make API request to Stack Exchange API
        url = 'https://api.stackexchange.com/2.3/questions'
        params = {
            'site': 'stackoverflow',
            'intitle': query,
            'order': 'desc',
            'sort': 'votes',
            'pagesize': 1,
            'filter': '!-*f(6rc.(XcPdJ_'
        }
        response = requests.get(url, params=params)

        # Process the API response and generate a response message
        if response.status_code == 200:
            data = response.json()
            items = data.get('items', [])
            if items:
                question = items[0].get('title')
                answer_id = items[0].get('accepted_answer_id')
                if answer_id:
                    answer_url = f'https://api.stackexchange.com/2.3/answers/{answer_id}'
                    answer_params = {
                        'site': 'stackoverflow',
                        'filter': '!9_bDE(fI5',
                        'key': API_KEY
                    }
                    answer_response = requests.get(answer_url, params=answer_params)
                    if answer_response.status_code == 200:
                        answer_data = answer_response.json()
                        answers = answer_data.get('items', [])
                        if answers:
                            answer = answers[0].get('body_markdown')
                            response_message = f"The top answer related to the question '{question}' is:\n\n{answer}"
                        else:
                            response_message = f"No answer found for the question '{question}'"
                    else:
                        response_message = 'Error occurred while retrieving the answer.'
                else:
                    response_message = f"No accepted answer found for the question '{question}'"
            else:
                response_message = f"No question found related to '{query}'"
        else:
            response_message = 'Error occurred while making the API request.'

        return JsonResponse({'response': response_message})

    return JsonResponse({})