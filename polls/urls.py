from . import views
from django.urls import path

app_name = 'polls'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),  # GET
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),  # GET
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),  # GET
    path('<int:question_id>/vote/', views.vote, name='vote'),  # POST
]
