from django.shortcuts import render
from .apps import SoundpredictorConfig
from django.http import JsonResponse
from rest_framework.views import APIView


class call_model(APIView):
    def get(self, request):
        if request.method == 'GET':
            sound = request.GET.get('sound')
            # sklearn prediction model 
            vector = SoundpredictorConfig.vectorize.transform([sound])
            prediction = SoundpredictorConfig.regressor.predict(vector)[0]
            response = {'data': prediction}
            return JsonResponse(response)
    
