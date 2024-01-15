from django.shortcuts import render
from django.http import JsonResponse
import openai

def generate_ideas(request):
    if request.method == 'POST':
        user_input = request.POST.get('user_input', '')

        openai.api_key = "Chave_OPENAI_API_KEY"

        prompt = f"Gere conceitos inovadores de startups com base em: {user_input}"

        response = openai.Completion.create(
            model='gpt-3.5-turbo',
            prompt=prompt,
            max_tokens=1000,
        )
        generated_text = response['choices'][0]['text']

        return JsonResponse({'generate_ideas': generated_text})
    elif request.method == 'GET':
        return render(request, 'ideas_generator/index.html')
    else:
        return JsonResponse({'error': 'Método não permitido'}, status=405)
