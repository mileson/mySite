from django.urls import path
from . import views


urlpatterns = [
    path('<int:question_id>', views.question, name='question'),

    path('<int:question_id>', views.result, name='result'),

    path('<int:question_id>', views.vote, name='vote'),
]
