from django.db import models

# === Localidades (UF e Cidade) ===
class UF(models.Model):
    uf = models.CharField(max_length=2, unique=True)

    class Meta:
        verbose_name = 'Unidade Federativa'
        verbose_name_plural = 'Unidades Federativas'
        
    def __str__(self):
        return self.uf


class Cidade(models.Model):
    nome = models.CharField(max_length=100)
    uf = models.ForeignKey(UF, on_delete=models.CASCADE, verbose_name='Unidade Federativa')

    class Meta:
        verbose_name = 'Cidade'
        verbose_name_plural = 'Cidades'

    def __str__(self):
        return f'{self.nome} - {self.uf}'


# === Ocupações e Pessoas ===
class Ocupacao(models.Model):
    nome = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Ocupação'
        verbose_name_plural = 'Ocupações'

    def __str__(self):
        return self.nome


class Pessoa(models.Model):
    nome = models.CharField(max_length=100)
    nome_pai = models.CharField(max_length=100)
    nome_mae = models.CharField(max_length=100)
    cpf = models.CharField(max_length=11, unique=True)
    data_nascimento = models.DateField(null=True, blank=True, verbose_name='Data de Nascimento', default='2000-01-01')
    email = models.EmailField(unique=True, blank=True, null=True)
    cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE, verbose_name='Cidade')
    ocupacao = models.ForeignKey(Ocupacao, on_delete=models.CASCADE, verbose_name='Ocupação', null=True, blank=True)

    class Meta:
        abstract = True

    def __str__(self):
        return f'{self.nome} - {self.cidade} - {self.ocupacao}'


class Aluno(Pessoa):
    ra = models.CharField(max_length=10, unique=True, verbose_name='Registro Acadêmico', null=True, blank=True)


    class Meta:
        verbose_name = 'Aluno'
        verbose_name_plural = 'Alunos'

    def __str__(self):
        return f'{self.nome} - {self.ra}'


class Professor(Pessoa):
    pass

    class Meta:
        verbose_name = 'Professor'
        verbose_name_plural = 'Professores'


# === Instituições e Cursos ===
class Instituicao(models.Model):
    nome = models.CharField(max_length=100, unique=True)
    site = models.URLField(max_length=100, blank=True, null=True)
    telefone = models.CharField(max_length=15, blank=True, null=True)
    cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE, verbose_name='Cidade', blank=True, null=True)

    class Meta:
        verbose_name = 'Instituição'
        verbose_name_plural = 'Instituições'

    def __str__(self):
        return f'{self.nome} - {self.cidade}'


class Areas_Saber(models.Model):
    nome = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Área do Saber'
        verbose_name_plural = 'Áreas do Saber'

    def __str__(self):
        return self.nome


class Curso(models.Model):
    nome = models.CharField(max_length=100)
    instituicao = models.ForeignKey(Instituicao, on_delete=models.CASCADE, verbose_name='Instituição')
    carga_horaria_total = models.PositiveIntegerField()
    duracao_meses = models.PositiveSmallIntegerField()
    area_saber = models.ManyToManyField(Areas_Saber, verbose_name='Área do Saber')
    disciplinas = models.ManyToManyField('Disciplina', verbose_name='Disciplinas')

    class Meta:
        verbose_name = 'Curso'
        verbose_name_plural = 'Cursos'

    def __str__(self):
        return f'{self.nome} - {self.instituicao}'


# === Turnos, Disciplinas e Avaliações ===
class Turno(models.Model):
    nome = models.CharField(max_length=100)  # Ex.: Matutino, Vespertino, Noturno

    class Meta:
        verbose_name = 'Turno'
        verbose_name_plural = 'Turnos'

    def __str__(self):
        return self.nome


class Disciplina(models.Model):
    nome = models.CharField(max_length=100)
    area_saber = models.ForeignKey(Areas_Saber, on_delete=models.CASCADE, verbose_name='Área do Saber')
    estudantes = models.ManyToManyField(Aluno, through='Matricula', related_name='Disciplinas', verbose_name='Estudantes')

    class Meta:
        verbose_name = 'Disciplina'
        verbose_name_plural = 'Disciplinas'

    def __str__(self):
        return self.nome


class Tipo_Avaliacao(models.Model):
    nome = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Tipo de Avaliação'
        verbose_name_plural = 'Tipos de Avaliação'

    def __str__(self):
        return self.nome


class Avaliacao(models.Model):
    descricao = models.TextField( blank=True, null=True, verbose_name='Descrição', help_text='Descrição da avaliação')
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, verbose_name='Curso')
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE, verbose_name='Disciplina')
    estudante = models.ForeignKey(Aluno, on_delete=models.CASCADE, verbose_name='Estudante')
    nota = models.DecimalField(max_digits=3, decimal_places=2, blank=True, null=True, verbose_name='Nota')
    tipo_avaliacao = models.ForeignKey(Tipo_Avaliacao, on_delete=models.CASCADE, verbose_name='Tipo de Avaliação')

    class Meta:
        verbose_name = 'Avaliação'
        verbose_name_plural = 'Avaliações'

    def __str__(self):
        return f'{self.descricao} - {self.curso} - {self.disciplina} - {self.tipo_avaliacao}'


# === Matrículas, Frequências e Turmas ===
class Matricula(models.Model):
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE, verbose_name='Aluno', null=True, blank=True)
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE, verbose_name='Disciplina', related_name='matriculas')
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, verbose_name='Curso')
    instituicao = models.ForeignKey(Instituicao, on_delete=models.CASCADE, verbose_name='Instituição')
    data_inicio = models.DateField(blank=True, null=True, verbose_name='Data de Início', default='2000-01-01')
    data_previsao_termino = models.DateField(blank=True, null=True, verbose_name='Data Previsão de Término', default='2000-01-01')

    class Meta:
        verbose_name = 'Matrícula'
        verbose_name_plural = 'Matrículas'

    def __str__(self):
        return f'{self.aluno} - {self.disciplina} -  {self.curso}'


class Frequencia(models.Model):
    estudante = models.ForeignKey(Aluno, on_delete=models.CASCADE, verbose_name='Estudante', related_name='frequencias_estudante')
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, verbose_name='Curso')
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE, verbose_name='Disciplina')
    numero_faltas = models.PositiveSmallIntegerField()

    class Meta:
        verbose_name = 'Frequência'
        verbose_name_plural = 'Frequências'

    def __str__(self):
        return f'{self.estudante} - {self.curso} - {self.disciplina} - {self.numero_faltas}'


class Turma(models.Model):
    nome = models.CharField(max_length=100)
    turno = models.ForeignKey(Turno, on_delete=models.CASCADE, verbose_name='Turno')
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, verbose_name='Curso')
    alunos = models.ManyToManyField(Aluno, verbose_name='Alunos', blank=True)
    class Meta:
        verbose_name = 'Turma'
        verbose_name_plural = 'Turmas'

    def __str__(self):
        return self.nome


# === Ocorrências ===
class Ocorrencia(models.Model):
    descricao = models.TextField()
    data = models.DateField(verbose_name='Data', default='2000-01-01')
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, verbose_name='Curso')
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE, verbose_name='Disciplina')
    # pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE, verbose_name='Pessoa')

    class Meta:
        verbose_name = 'Ocorrência'
        verbose_name_plural = 'Ocorrências'

    def __str__(self):
        return f'{self.descricao} - {self.curso}'