from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.views import View
from django.contrib import messages
from django import forms

class IndexView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'index.html')
    
class CursosView(View):
    def get(self, request, *args, **kwargs):
        cursos = Curso.objects.all()
        return render(request, 'curso.html', {'cursos': cursos})

class InstituicoesView(View):
    def get(self, request, *args, **kwargs):
        instituicoes = Instituicao.objects.all()
        return render(request, 'instituicoes.html', {'instituicoes': instituicoes})
    
class TurmasView(View):
    def get(self, request, *args, **kwargs):
        turmas = Turma.objects.all()
        return render(request, 'turmas.html', {'turmas': turmas})

class AlunosView(View):
    def get(self, request, *args, **kwargs):
        alunos = Aluno.objects.all()
        return render(request, 'alunos.html', {'alunos': alunos})

class ProfessoresView(View):
    def get(self, request, *args, **kwargs):
        professores = Professor.objects.all()
        return render(request, 'professores.html', {'professores': professores})
    
class AvaliacoesView(View):
    def get(self, request, *args, **kwargs):
        avaliacoes = Avaliacao.objects.all()
        return render(request, 'avaliacoes.html', {'avaliacoes': avaliacoes})
    
class FrequenciasView(View):
    def get(self, request, *args, **kwargs):
        frequencias = Frequencia.objects.all()
        return render(request, 'frequencias.html', {'frequencias': frequencias})

class OcorrenciasView(View):
    def get(self, request, *args, **kwargs):
        ocorrencias = Ocorrencia.objects.all()
        return render(request, 'ocorrencias.html', {'ocorrencias': ocorrencias})
    
class AlunoForm(forms.ModelForm):
    class Meta:
        model = Aluno
        fields = ['nome', 'nome_pai', 'nome_mae', 'cpf', 'data_nascimento', 'email', 'cidade', 'ocupacao']

class AlunoCreateView(View):
    def get(self, request, *args, **kwargs):
        form = AlunoForm()
        return render(request, 'aluno_form.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = AlunoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('alunos')
        return render(request, 'aluno_form.html', {'form': form})


