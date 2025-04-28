from django.http import JsonResponse
from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import json

@method_decorator(csrf_exempt, name='dispatch')
class MeuEndpointView(View):

    def get(self, request):
        return JsonResponse({'mensagem': 'Você fez uma requisição GET'})

    def post(self, request):
        dados = json.loads(request.body)
        nome = dados.get('nome', 'sem nome')
        return JsonResponse({'mensagem': f'Olá, {nome}! Você fez uma requisição POST'})
