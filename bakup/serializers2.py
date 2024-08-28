from rest_framework import serializers
from .models import (Curso, SemestreLectivo, Disciplina, Docente, Estudante, 
                     Funcionario, Acionista, PagamentoMatricula, PagamentoMensalidade,Teste,Exames)

class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = '__all__'

class SemestreLectivoSerializer(serializers.ModelSerializer):
    class Meta:
        model = SemestreLectivo
        fields = '__all__'


class DisciplinaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Disciplina
        fields = '__all__'

class DocenteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Docente
        fields = '__all__'


class EstudanteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estudante
        fields = '__all__'


class FuncionarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Funcionario
        fields = '__all__'


class AcionistaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Acionista
        fields = '__all__'

class PagamentoMatriculaSerializer(serializers.ModelSerializer):
    class Meta:
        model = PagamentoMatricula
        fields = '__all__'


class PagamentoMensalidadeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PagamentoMensalidade
        fields = '__all__'

"""
class AvaliacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Avaliacao
        fields = '__all__'


class AvaliacaoExameSerializer(serializers.ModelSerializer):
    class Meta:
        model = AvaliacaoExame
        fields = '__all__'

"""
class TesteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teste
        fields = '__all__'

class ExamesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exames
        fields = '__all__'