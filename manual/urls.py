from django.urls import path

from . import views

app_name = 'manual'
urlpatterns = [
    # /manual/
    path('', views.index, name='index'),
    # /manual/5/
    path('<int:action_id>/', views.detail, name='detail'),
    # /manual/5/
    path('<int:equipment_id>/vote', views.vote, name='vote'),

]
