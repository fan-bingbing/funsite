from django.urls import path

from . import views

urlpatterns = [
    # /manual/
    path('', views.index, name='index'),
    # /manual/5/
    path('<int:action_id>/', views.detail, name='detail'),

]
