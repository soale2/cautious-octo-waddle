from django.shortcuts import render
from django.http import JsonResponse

def chatbot(request):
    return render(request, 'chatbot_app/chatbot.html')

def chatbot_api_view(request):
    if request.method == 'POST':
        query = request.POST.get('query')

        # Process the user query and generate a response
        response = 'This is a sample response.'

        return JsonResponse({'response': response})

    return JsonResponse({})