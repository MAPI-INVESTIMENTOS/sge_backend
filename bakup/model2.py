from django.db import models
from django.contrib.auth.models import User
from datetime import date

class Curso(models.Model):
    id_curso = models.BigAutoField(primary_key=True)
    codigo_do_curso = models.CharField(max_length=20, unique=True)
    nome_do_curso = models.CharField(max_length=100)
    descricao = models.TextField(max_length=2000, null=True, blank=True)

    def __str__(self):
        return self.nome_do_curso

class SemestreLectivo(models.Model):
    id_semestre = models.BigAutoField(primary_key=True)
    semestre_lec = models.IntegerField()
    curso = models.ForeignKey(Curso, related_name='semestres', on_delete=models.CASCADE)

    def __str__(self):
        return f'Semestre {self.semestre_lec} do Curso {self.curso.nome_do_curso}'

class Disciplina(models.Model):
    id_disciplina = models.BigAutoField(primary_key=True)
    codigo_da_disciplina = models.CharField(max_length=20, unique=True)
    nome_da_disciplina = models.CharField(max_length=100)
    carga_hora = models.IntegerField()
    descricao_disciplina = models.TextField()
    semestre = models.ForeignKey(SemestreLectivo, related_name='disciplinas', on_delete=models.CASCADE)

    def __str__(self):
        return self.nome_da_disciplina




class Docente(models.Model):
    id_docente = models.BigAutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True,unique=True)
    nome_do_docente = models.CharField(max_length=225)
    apelido_do_docente = models.CharField(max_length=225)
    data_de_nascimento = models.DateField()
    identificacao = models.CharField(max_length=20, unique=True)
    data_de_emissao = models.DateField()
    data_de_validade = models.DateField()
    nuit = models.CharField(max_length=20, unique=True)
    endereco_do_docente = models.CharField(max_length=255)
    contacto = models.CharField(max_length=15)
    email = models.EmailField()
    formacao = models.TextField(null=True, blank=True)

    def __str__(self):
        return f'{self.nome_do_docente} {self.apelido_do_docente}'


class Estudante(models.Model):
    id_estudante = models.BigAutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE,null=True, unique=True)
    nome_do_estudante = models.CharField(max_length=100)
    segundo_nome = models.CharField(max_length=225)
    apelido_do_estudante = models.CharField(max_length=225)
    data_de_nascimento = models.DateField()
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
        return f'{self.nome_do_estudante} {self.apelido_do_estudante}'
    

class Funcionario(models.Model):
    id_funcionario = models.BigAutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True,unique=True)
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
    id_acionista = models.BigAutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True,unique=True)
    nome_acionista = models.CharField(max_length=255)
    segundo_nome_acionista = models.CharField(max_length=255)
    apelido_acionista = models.CharField(max_length=255)
    data_de_nascimento = models.DateField()
    identificacao = models.CharField(max_length=20, unique=True)
    nuit = models.CharField(max_length=20, unique=True)
    endereco = models.CharField(max_length=255)
    contacto = models.CharField(max_length=15)
    email = models.EmailField()

    def __str__(self):
        return self.nome_acionista





########################################################

from django.db import models
from django.contrib.auth.models import User
from datetime import date

class Docente(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True,unique=True)
    nome_do_docente = models.CharField(max_length=225)
    apelido_do_docente = models.CharField(max_length=225)
    data_de_nascimento = models.DateField()
    identificacao = models.CharField(max_length=20, unique=True)
    data_de_emissao = models.DateField()
    data_de_validade = models.DateField()
    nuit = models.CharField(max_length=20, unique=True)
    endereco_do_docente = models.CharField(max_length=255)
    contacto = models.CharField(max_length=15)
    email = models.EmailField()
    formacao = models.TextField(null=True, blank=True)

    def __str__(self):
        return f'{self.nome_do_docente} {self.apelido_do_docente}'

class SemestreLectivo(models.Model):
    nome_do_semestre = models.CharField(max_length=15)
    curso = models.ForeignKey('Curso', on_delete=models.CASCADE, related_name='semestres',null=True)

    def __str__(self):
        return self.nome_do_semestre

class Curso(models.Model):
    codigo_do_curso = models.CharField(max_length=20, unique=True)
    nome_do_curso = models.CharField(max_length=100)
    duracao_semestres = models.IntegerField()
    diretor_do_curso = models.ForeignKey(Docente, on_delete=models.CASCADE, null=True, blank=True)
    descricao = models.TextField(max_length=2000, null=True, blank=True)

    def __str__(self):
        return self.nome_do_curso

class Disciplina(models.Model):
    codigo_da_disciplina = models.CharField(max_length=20, unique=True)
    nome_da_disciplina = models.CharField(max_length=100)
    carga_hora = models.IntegerField()
    descricao_disciplina = models.TextField()
   # curso = models.ForeignKey(Curso, on_delete=models.CASCADE, related_name='disciplinas')
    semestre = models.ForeignKey(SemestreLectivo, on_delete=models.CASCADE, related_name='disciplinas')
    docente_responsavel = models.ForeignKey(Docente, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.nome_da_disciplina

class Teste(models.Model):
    estudante = models.ForeignKey('Estudante', on_delete=models.CASCADE, related_name='testes',unique=	True)
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE, related_name='testes')
    teste1 = models.FloatField(null=True, blank=True)
    teste2 = models.FloatField(null=True, blank=True)
    teste3 = models.FloatField(null=True, blank=True)
    teste4 = models.FloatField(null=True, blank=True)

    def calcular_media(self):
        notas = [self.teste1, self.teste2, self.teste3, self.teste4]
        notas = [nota for nota in notas if nota is not None]
        if notas:
            media = sum(notas) / len(notas)
            if media < 10:
                return media
            elif 10 <= media <= 13:
                return media
            elif 14 <= media <= 20:
                return media
        return self.media

    def __str__(self):
        return f'Testes {self.estudante.nome_do_estudante} {self.disciplina.nome_da_disciplina}'

class Exames(models.Model):
    estudante = models.ForeignKey('Estudante', on_delete=models.CASCADE, related_name='exames',unique=True)
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE, related_name='exames')
    exame1 = models.FloatField(null=True, blank=True)
    recorrencia = models.FloatField(null=True, blank=True)

    def verificar_aprovacao(self):
        nota = self.recorrencia if self.recorrencia is not None else self.exame1
        if nota is not None:
            if 0 <= nota <= 9:
                return "Estudante não aprovado"
            elif 10 <= nota <= 20:
                return "Estudante aprovado"
        return self.nota

    def __str__(self):
        return f'Exame {self.estudante.nome_do_estudante} {self.disciplina.nome_da_disciplina}'

class Estudante(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True,unique=True)
    nome_do_estudante = models.CharField(max_length=100)
    segundo_nome = models.CharField(max_length=225)
    apelido_do_estudante = models.CharField(max_length=225)
    data_de_nascimento = models.DateField()
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
        return f'{self.nome_do_estudante} {self.apelido_do_estudante}'

class PagamentoMatricula(models.Model):
    PENDENTE = 'pendente'
    PAGA = 'paga'
    STATUS_CHOICES = [
        (PENDENTE, 'Pendente'),
        (PAGA, 'Paga'),
    ]

    estudante = models.ForeignKey(Estudante, on_delete=models.CASCADE)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    data_pagamento = models.DateField(null=True, blank=True)
    metodo_pagamento = models.CharField(max_length=50)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default=PENDENTE)

    def save(self, *args, **kwargs):
        if self.data_pagamento and self.data_pagamento <= date.today():
            self.status = self.PAGA
        else:
            self.status = self.PENDENTE
        super(PagamentoMatricula, self).save(*args, **kwargs)

    def __str__(self):
        return f'Matrícula {self.estudante.nome_do_estudante} {self.estudante.apelido_do_estudante} - {self.data_pagamento} - {self.get_status_display()}'

class PagamentoMensalidade(models.Model):
    PENDENTE = 'pendente'
    PAGA = 'paga'
    STATUS_CHOICES = [
        (PENDENTE, 'Pendente'),
        (PAGA, 'Paga'),
    ]

    estudante = models.ForeignKey(Estudante, on_delete=models.CASCADE)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    data_pagamento = models.DateField(null=True, blank=True)
    metodo_pagamento = models.CharField(max_length=50)
    mes_referente = models.CharField(max_length=20)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default=PENDENTE)

    def save(self, *args, **kwargs):
        if self.data_pagamento and self.data_pagamento <= date.today():
            self.status = self.PAGA
        else:
            self.status = self.PENDENTE
        super(PagamentoMensalidade, self).save(*args, **kwargs)

    def __str__(self):
        return f'Mensalidade {self.estudante.nome_do_estudante} {self.estudante.apelido_do_estudante} - {self.mes_referente} {self.data_pagamento} - {self.get_status_display()}'

class Funcionario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True,unique=True)
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
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True,unique=True)
    nome_acionista = models.CharField(max_length=255)
    segundo_nome_acionista = models.CharField(max_length=255)
    apelido_acionista = models.CharField(max_length=255)
    data_de_nascimento = models.DateField()
    identificacao = models.CharField(max_length=20, unique=True)
    nuit = models.CharField(max_length=20, unique=True)
    endereco = models.CharField(max_length=255)
    contacto = models.CharField(max_length=15)
    email = models.EmailField()

    def __str__(self):
        return self.nome_acionista


class Matricula(models.Model):
    numero = models.CharField(max_length=225)
    estudante = models.ForeignKey(Estudante, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    data_matricula = models.DateField(auto_now_add=True)
    semestre_lectivo = models.ForeignKey(SemestreLectivo, on_delete=models.CASCADE)

    def __str__(self):
        return f'Matrícula {self.estudante.nome_do_estudante} - {self.curso.nome_do_curso}'

class RenovacaoMatricula(models.Model):
    numero = models.CharField(max_length=225)
    estudante = models.ForeignKey(Estudante, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    data_renovacao = models.DateField(auto_now_add=True)
    ano_lectivo = models.ForeignKey(SemestreLectivo, on_delete=models.CASCADE)

    def __str__(self):
        return f'Renovação de Matrícula {self.estudante.nome_do_estudante} - {self.curso.nome_do_curso}'