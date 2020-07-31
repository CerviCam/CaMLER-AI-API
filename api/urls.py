from api.helper import path
from api import views

urls = [
    path('/predict', views.predict, methods=['POST'])
]