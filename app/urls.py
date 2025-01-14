# academico/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('cursos/', views.CursosView.as_view(), name='cursos'),
    path('instituicoes/', views.InstituicoesView.as_view(), name='instituicoes'),
    path('turmas/', views.TurmasView.as_view(), name='turmas'),
    path('alunos/', views.AlunosView.as_view(), name='alunos'),
    path('professores/', views.ProfessoresView.as_view(), name='professores'),
    path('avaliacoes/', views.AvaliacoesView.as_view(), name='avaliacoes'),
    path('frequencias/', views.FrequenciasView.as_view(), name='frequencias'),
    path('ocorrencias/', views.OcorrenciasView.as_view(), name='ocorrencias'),
]
