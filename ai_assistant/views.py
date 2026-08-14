from django.shortcuts import render

# Create your views here.
import json

from django.http import JsonResponse
from django.views.decorators.http import require_POST

from .services import ask_gemini


@require_POST
def ask_ai(request):

    try:
        body = json.loads(request.body)

        question = body.get("question", "").strip()

        if not question:
            return JsonResponse(
                {
                    "success": False,
                    "error": "Please enter a question."
                },
                status=400
            )

        answer = ask_gemini(question)

        return JsonResponse(
            {
                "success": True,
                "answer": answer
            }
        )

    except Exception as e:

        return JsonResponse(
            {
                "success": False,
                "error": str(e)
            },
            status=500
        )