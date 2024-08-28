from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User

class DiretorCurso(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True, unique=True)
    nome = models.CharField(max_length=255)
    segundo_nome = models.CharField(max_length=255)
    apelido = models.CharField(max_length=255)
    data_de_nascimento = models.DateField()
    identificacao = models.CharField(max_length=20, unique=True)
    nuit = models.CharField(max_length=20, unique=True)
    endereco = models.CharField(max_length=255)
    contacto = models.CharField(max_length=15)
    email = models.EmailField()

    def __str__(self):
        return self.nome


class Curso(models.Model):
    id = models.BigAutoField(primary_key=True)
    codigo = models.CharField(max_length=20, unique=True)
    nome = models.CharField(max_length=100)
    descricao = models.TextField(max_length=2000, null=True, blank=True)
    diretor = models.ForeignKey(DiretorCurso, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.nome


class SemestreLectivo(models.Model):
    id = models.BigAutoField(primary_key=True)
    semestre = models.IntegerField()
    curso = models.ForeignKey(Curso, related_name='semestres', on_delete=models.CASCADE)

    def __str__(self):
        return f'Semestre {self.semestre} do Curso {self.curso.nome}'




class Docente(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True, unique=True)
    nome = models.CharField(max_length=225)
    apelido = models.CharField(max_length=225)
    data_de_nascimento = models.DateField()
    identificacao = models.CharField(max_length=20, unique=True)
    data_de_emissao = models.DateField()
    data_de_validade = models.DateField()
    nuit = models.CharField(max_length=20, unique=True)
    endereco = models.CharField(max_length=255)
    contacto = models.CharField(max_length=15)
    email = models.EmailField()
    formacao = models.TextField(null=True, blank=True)

    def __str__(self):
        return f'{self.nome} {self.apelido}'
    
class Disciplina(models.Model):
    id = models.BigAutoField(primary_key=True)
    codigo = models.CharField(max_length=20, unique=True)
    nome = models.CharField(max_length=100)
    carga_horaria = models.IntegerField()
    descricao = models.TextField()
    semestre = models.ForeignKey(SemestreLectivo, related_name='disciplinas', on_delete=models.CASCADE)
    docente_responsavel = models.ForeignKey(Docente, related_name='disciplinas', on_delete=models.CASCADE)

    def __str__(self):
        return self.nome
    

class DocenteDisciplina(models.Model):
    docente = models.ForeignKey(Docente, on_delete=models.CASCADE)
    disciplina = models.ManyToManyField(Disciplina)

    def __str__(self):
        disciplinas = ', '.join([d.nome for d in self.disciplina.all()])
        return f'{self.docente.nome} leciona {disciplinas}'
    



class Estudante(models.Model):
    GENERO_CHOICES = [
        ('M', 'Masculino'),
        ('F', 'Feminino'),
    ]
    id = models.BigAutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True, unique=True)
    nome = models.CharField(max_length=100)
    segundo_nome = models.CharField(max_length=225)
    apelido = models.CharField(max_length=225)
    data_de_nascimento = models.DateField()
    genero = models.CharField(max_length=1, choices=GENERO_CHOICES)
    nacionalidade = models.CharField(max_length=100)
    numero_de_bi = models.CharField(max_length=20, unique=True)
    data_de_emissao = models.DateField()
    data_de_validade = models.DateField()
    nuit = models.CharField(max_length=20, unique=True)
    endereco = models.CharField(max_length=255)
    contacto = models.CharField(max_length=15)
    email = models.EmailField()
    nome_do_pai = models.CharField(max_length=600)
    nome_da_mae = models.CharField(max_length=600)
    escola_anterior = models.CharField(max_length=400)
    ano_conclusao = models.DateField()

    def __str__(self):
        return f'{self.nome} {self.apelido}'
    
class EstudanteDisciplina(models.Model):
    estudante = models.ForeignKey(Estudante, on_delete=models.CASCADE)
    disciplinas = models.ManyToManyField(Disciplina)

    def __str__(self):
        disciplinas_nomes = ', '.join([disciplina.nome for disciplina in self.disciplinas.all()])
        return f'{self.estudante.nome} estuda {disciplinas_nomes}'
    
class EstudanteCurso(models.Model):
    estudante = models.ForeignKey(Estudante, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('estudante', 'curso')
        verbose_name = 'Estudante Curso'
        verbose_name_plural = 'Estudantes Cursos'

    def __str__(self):
        return f'{self.estudante.nome} - {self.curso.nome}'


class Pagamento(models.Model):
    TIPO_PAGAMENTO_CHOICES = [
        ('matricula', 'Matrícula'),
        ('mensalidade', 'Mensalidade'),
    ]
    
    MES_REFERENTE_CHOICES = [
        ('janeiro', 'Janeiro'),
        ('fevereiro', 'Fevereiro'),
        ('marco', 'Março'),
        ('abril', 'Abril'),
        ('maio', 'Maio'),
        ('junho', 'Junho'),
        ('julho', 'Julho'),
        ('agosto', 'Agosto'),
        ('setembro', 'Setembro'),
        ('outubro', 'Outubro'),
        ('novembro', 'Novembro'),
        ('dezembro', 'Dezembro'),
    ]

    METODO_PAGAMENTO_CHOICES = [
        ('numerario', 'Numerário'),
        ('m-pesa', 'M-Pesa'),
        ('e-mola', 'E-Mola'),
        ('bim', 'BIM'),
    ]

    id = models.BigAutoField(primary_key=True)
    estudante = models.ForeignKey(Estudante, on_delete=models.CASCADE, related_name='pagamentos')
    tipo_pagamento = models.CharField(max_length=20, choices=TIPO_PAGAMENTO_CHOICES)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    data_pagamento = models.DateField(auto_now_add=True)
    metodo_pagamento = models.CharField(max_length=20, choices=METODO_PAGAMENTO_CHOICES)
    mes_referente = models.CharField(max_length=10, choices=MES_REFERENTE_CHOICES)

    def __str__(self):
        return f'{self.get_tipo_pagamento_display()} - {self.estudante.nome} {self.estudante.apelido}'



from django.db import models

class Avaliacao(models.Model):
    estudante = models.ForeignKey('Estudante', on_delete=models.CASCADE)
    disciplina = models.ForeignKey('Disciplina', on_delete=models.CASCADE)
    nota1 = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    percent_nota1 = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)  # Percentagem para nota1
    nota2 = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    percent_nota2 = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)  # Percentagem para nota2
    nota3 = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    percent_nota3 = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)  # Percentagem para nota3
    nota4 = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    percent_nota4 = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)  # Percentagem para nota4
    data_avaliacao = models.DateField(auto_now_add=True)

    def clean(self):
        super().clean()
        percent_values = [self.percent_nota1, self.percent_nota2, self.percent_nota3, self.percent_nota4]
        percent_values = [p for p in percent_values if p is not None]
        if sum(percent_values) != 100:
            raise ValidationError('A soma das percentagens das notas deve ser igual a 100%.')

    def __str__(self):
        return (
            f'{self.estudante.nome} tem notas {self.nota1}, {self.nota2}, {self.nota3}, {self.nota4}, '
            f'com percentagens {self.percent_nota1}%, {self.percent_nota2}%, {self.percent_nota3}%, {self.percent_nota4}%, '
            f'em {self.disciplina.nome}'
        )


class Exames(models.Model):
    estudante = models.ForeignKey(Estudante, on_delete=models.CASCADE)
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE)
    exame = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    exame_recorrencia = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    data_avaliacao = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.estudante.nome}, exame {self.exame}, recorrência {self.exame_recorrencia} em {self.disciplina.nome}'


class Funcionario(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True, unique=True)
    nome = models.CharField(max_length=225)
    apelido = models.CharField(max_length=225)
    data_de_nascimento = models.DateField()
    identificacao = models.CharField(max_length=20, unique=True)
    nuit = models.CharField(max_length=20, unique=True)
    endereco = models.CharField(max_length=255)
    contacto = models.CharField(max_length=15)
    email = models.EmailField()

    def __str__(self):
        return self.nome


class Acionista(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True, unique=True)
    nome = models.CharField(max_length=255)
    segundo_nome = models.CharField(max_length=255)
    apelido = models.CharField(max_length=255)
    data_de_nascimento = models.DateField()
    identificacao = models.CharField(max_length=20, unique=True)
    nuit = models.CharField(max_length=20, unique=True)
    endereco = models.CharField(max_length=255)
    contacto = models.CharField(max_length=15)
    email = models.EmailField()

    def __str__(self):
        return self.nome
"""
from django.db import models
from django.contrib.auth.models import User

class DiretorCurso(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True, unique=True)
    nome = models.CharField(max_length=255)
    segundo_nome = models.CharField(max_length=255)
    apelido = models.CharField(max_length=255)
    data_de_nascimento = models.DateField()
    identificacao = models.CharField(max_length=20, unique=True)
    nuit = models.CharField(max_length=20, unique=True)
    endereco = models.CharField(max_length=255)
    contacto = models.CharField(max_length=15)
    email = models.EmailField()

    def __str__(self):
        return self.nome


class Curso(models.Model):
    id = models.BigAutoField(primary_key=True)
    codigo = models.CharField(max_length=20, unique=True)
    nome = models.CharField(max_length=100)
    descricao = models.TextField(max_length=2000, null=True, blank=True)
    diretor = models.ForeignKey(DiretorCurso, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.nome


class SemestreLectivo(models.Model):
    id = models.BigAutoField(primary_key=True)
    semestre = models.IntegerField()
    curso = models.ForeignKey(Curso, related_name='semestres', on_delete=models.CASCADE)

    def __str__(self):
        return f'Semestre {self.semestre} do Curso {self.curso.nome}'




class Docente(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True, unique=True)
    nome = models.CharField(max_length=225)
    apelido = models.CharField(max_length=225)
    data_de_nascimento = models.DateField()
    identificacao = models.CharField(max_length=20, unique=True)
    data_de_emissao = models.DateField()
    data_de_validade = models.DateField()
    nuit = models.CharField(max_length=20, unique=True)
    endereco = models.CharField(max_length=255)
    contacto = models.CharField(max_length=15)
    email = models.EmailField()
    formacao = models.TextField(null=True, blank=True)

    def __str__(self):
        return f'{self.nome} {self.apelido}'
    
class Disciplina(models.Model):
    id = models.BigAutoField(primary_key=True)
    codigo = models.CharField(max_length=20, unique=True)
    nome = models.CharField(max_length=100)
    carga_horaria = models.IntegerField()
    descricao = models.TextField()
    semestre = models.ForeignKey(SemestreLectivo, related_name='disciplinas', on_delete=models.CASCADE)
    docente_responsavel = models.ForeignKey(Docente, related_name='disciplinas', on_delete=models.CASCADE)

    def __str__(self):
        return self.nome
    

class DocenteDisciplina(models.Model):
    docente = models.ForeignKey(Docente, on_delete=models.CASCADE)
    disciplina = models.ManyToManyField(Disciplina)

    def __str__(self):
        disciplinas = ', '.join([d.nome for d in self.disciplina.all()])
        return f'{self.docente.nome} leciona {disciplinas}'
    



class Estudante(models.Model):
    GENERO_CHOICES = [
        ('M', 'Masculino'),
        ('F', 'Feminino'),
    ]
    id = models.BigAutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True, unique=True)
    nome = models.CharField(max_length=100)
    segundo_nome = models.CharField(max_length=225)
    apelido = models.CharField(max_length=225)
    data_de_nascimento = models.DateField()
    genero = models.CharField(max_length=1, choices=GENERO_CHOICES)
    nacionalidade = models.CharField(max_length=100)
    numero_de_bi = models.CharField(max_length=20, unique=True)
    data_de_emissao = models.DateField()
    data_de_validade = models.DateField()
    nuit = models.CharField(max_length=20, unique=True)
    endereco = models.CharField(max_length=255)
    contacto = models.CharField(max_length=15)
    email = models.EmailField()
    nome_do_pai = models.CharField(max_length=600)
    nome_da_mae = models.CharField(max_length=600)
    escola_anterior = models.CharField(max_length=400)
    ano_conclusao = models.DateField()

    def __str__(self):
        return f'{self.nome} {self.apelido}'
    
class EstudanteDisciplina(models.Model):
    estudante = models.ForeignKey(Estudante, on_delete=models.CASCADE)
    disciplinas = models.ManyToManyField(Disciplina)

    def __str__(self):
        disciplinas_nomes = ', '.join([disciplina.nome for disciplina in self.disciplinas.all()])
        return f'{self.estudante.nome} estuda {disciplinas_nomes}'
    
class EstudanteCurso(models.Model):
    estudante = models.ForeignKey(Estudante, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('estudante', 'curso')
        verbose_name = 'Estudante Curso'
        verbose_name_plural = 'Estudantes Cursos'

    def __str__(self):
        return f'{self.estudante.nome} - {self.curso.nome}'


class Pagamento(models.Model):
    TIPO_PAGAMENTO_CHOICES = [
        ('matricula', 'Matrícula'),
        ('mensalidade', 'Mensalidade'),
    ]
    
    MES_REFERENTE_CHOICES = [
        ('janeiro', 'Janeiro'),
        ('fevereiro', 'Fevereiro'),
        ('marco', 'Março'),
        ('abril', 'Abril'),
        ('maio', 'Maio'),
        ('junho', 'Junho'),
        ('julho', 'Julho'),
        ('agosto', 'Agosto'),
        ('setembro', 'Setembro'),
        ('outubro', 'Outubro'),
        ('novembro', 'Novembro'),
        ('dezembro', 'Dezembro'),
    ]

    METODO_PAGAMENTO_CHOICES = [
        ('numerario', 'Numerário'),
        ('m-pesa', 'M-Pesa'),
        ('e-mola', 'E-Mola'),
        ('bim', 'BIM'),
    ]

    id = models.BigAutoField(primary_key=True)
    estudante = models.ForeignKey(Estudante, on_delete=models.CASCADE, related_name='pagamentos')
    tipo_pagamento = models.CharField(max_length=20, choices=TIPO_PAGAMENTO_CHOICES)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    data_pagamento = models.DateField(auto_now_add=True)
    metodo_pagamento = models.CharField(max_length=20, choices=METODO_PAGAMENTO_CHOICES)
    mes_referente = models.CharField(max_length=10, choices=MES_REFERENTE_CHOICES)

    def __str__(self):
        return f'{self.get_tipo_pagamento_display()} - {self.estudante.nome} {self.estudante.apelido}'



class Avaliacao(models.Model):
    estudante = models.ForeignKey(Estudante, on_delete=models.CASCADE)
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE)
    nota1 = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    nota2 = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    nota3 = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    nota4 = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    data_avaliacao = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.estudante.nome} tem notas {self.nota1}, {self.nota2}, {self.nota3}, {self.nota4}, em {self.disciplina.nome}'
    

class Exames(models.Model):
    estudante = models.ForeignKey(Estudante, on_delete=models.CASCADE)
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE)
    exame = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    exame_recorrencia = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    data_avaliacao = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.estudante.nome}, exame {self.exame}, recorrência {self.exame_recorrencia} em {self.disciplina.nome}'


class Funcionario(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True, unique=True)
    nome = models.CharField(max_length=225)
    apelido = models.CharField(max_length=225)
    data_de_nascimento = models.DateField()
    identificacao = models.CharField(max_length=20, unique=True)
    nuit = models.CharField(max_length=20, unique=True)
    endereco = models.CharField(max_length=255)
    contacto = models.CharField(max_length=15)
    email = models.EmailField()

    def __str__(self):
        return self.nome


class Acionista(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True, unique=True)
    nome = models.CharField(max_length=255)
    segundo_nome = models.CharField(max_length=255)
    apelido = models.CharField(max_length=255)
    data_de_nascimento = models.DateField()
    identificacao = models.CharField(max_length=20, unique=True)
    nuit = models.CharField(max_length=20, unique=True)
    endereco = models.CharField(max_length=255)
    contacto = models.CharField(max_length=15)
    email = models.EmailField()

    def __str__(self):
        return self.nome

"""