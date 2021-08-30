import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "api.settings")
from django.apps import AppConfig
from django.conf import settings
import pickle


class SoundpredictorConfig(AppConfig):
    # sound predictor ML model config
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'soundpredictor'
    # ML model has been copied to the below folder
    path = os.path.join(settings.MODELS, 'models.p')
    with open(path, 'rb') as pickled:
        data = pickle.load(pickled)
        regressor = data['regressor']
        vectorize = data['vectorize'] 
