from django.contrib import admin
from .models import *


# UF e CIDADE
class CidadeInline(admin.TabularInline):
    model = Cidade
    extra = 1

class UFAdmin(admin.ModelAdmin):
    inlines = [CidadeInline]
    list_display = ('uf',)
    search_fields = ('uf',)



#PESSOA E OCUPAÇÃO
class AlunoInline(admin.StackedInline):
    model = Aluno
    extra = 1

class ProfessorInline(admin.StackedInline):
    model = Professor
    extra = 1

class OcupacaoAdmin(admin.ModelAdmin):
    inlines = [AlunoInline, ProfessorInline]
    list_display = ('nome',)



# CURSO E INSTITUIÇÃO
class CursoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'carga_horaria_total', 'duracao_meses', 'instituicao')
    filter_horizontal = ('area_saber', 'disciplinas')

class CursoinLine(admin.TabularInline):
    model = Curso
    extra = 1
    fields = ('nome', 'carga_horaria_total', 'duracao_meses', 'area_saber')
    show_change_link = True

class InstituicaoAdmin(admin.ModelAdmin):
    inlines = [CursoinLine]
    list_display = ('nome', 'cidade')
    search_fields = ('nome', 'cidade')



# AREA DO SABER E CURSO
class Areas_SaberAdmin(admin.ModelAdmin):
    list_display = ('nome',)


# CURSO E DISCIPLINA


# DISCIPLINA E AVALIAÇÃO
class AvaliacaoAdmin(admin.ModelAdmin):
    list_display = ('descricao', 'estudante', 'disciplina', 'nota')
    list_filter = ('disciplina', 'estudante')
    search_fields = ('descricao',)

class AvaliacaoInline(admin.StackedInline):
    model = Avaliacao
    extra = 1

class DisciplinaAdmin(admin.ModelAdmin):
    inlines = [AvaliacaoInline]
    list_display = ('nome', 'area_saber')
    search_fields = ('nome',)



# TURMA E ALUNOS
class TurmaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'turno', 'curso')
    filter_horizontal = ('alunos',)
    search_fields = ('nome',)

class TurmainLine(admin.TabularInline):
    inlines = [AlunoInline]
    model = Turma
    extra = 1
    fields = ('nome', 'curso', 'turno')
    show_change_link = True

class AlunoInline(admin.TabularInline):
    model = Aluno
    extra = 1




# Estudantes, disciplinas, avaliações, frequência
class FrequenciaAdmin(admin.ModelAdmin):
    list_display = ('estudante', 'disciplina', 'numero_faltas')
    list_filter = ('disciplina', 'estudante')
    search_fields = ('estudante__nome', 'disciplina__nome')



admin.site.register(UF, UFAdmin)
admin.site.register(Cidade)
admin.site.register(Ocupacao, OcupacaoAdmin)
admin.site.register(Instituicao, InstituicaoAdmin)
admin.site.register(Areas_Saber, Areas_SaberAdmin)
admin.site.register(Curso, CursoAdmin)
admin.site.register(Turno)
admin.site.register(Disciplina, DisciplinaAdmin)
admin.site.register(Matricula)
admin.site.register(Tipo_Avaliacao)
admin.site.register(Avaliacao, AvaliacaoAdmin)
admin.site.register(Frequencia, FrequenciaAdmin)
admin.site.register(Turma, TurmaAdmin)
admin.site.register(Professor)
admin.site.register(Aluno)
admin.site.register(Ocorrencia)
