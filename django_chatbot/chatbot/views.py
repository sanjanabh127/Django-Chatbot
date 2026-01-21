from django.shortcuts import render
from django.http import JsonResponse
from django.conf import settings
from openai import OpenAI

# Initialize OpenAI client
client = OpenAI(api_key=settings.OPENAI_API_KEY)


def ask_openai(message):
    response = client.responses.create(
        model="gpt-4.1-mini",
        input=message
    )

    answer = response.output[0].content[0].text
    return answer


def chatbot(request):
    if request.method == "POST":
        message = request.POST.get("message")
        reply = ask_openai(message)
        return JsonResponse({
            "message": message,
            "response": reply
        })

    return render(request, "chatbot.html")
