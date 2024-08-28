from rest_framework import serializers
from .models import (
    Curso, SemestreLectivo, Disciplina, Docente,Estudante,Avaliacao,Pagamento,Exames,
    EstudanteDisciplina, Funcionario, Acionista, DocenteDisciplina,DiretorCurso,EstudanteCurso)

class DiretorCursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = DiretorCurso
        fields = '__all__'

class CursoSerializer(serializers.ModelSerializer):
    diretor = DiretorCursoSerializer(read_only=True)

    class Meta:
        model = Curso
        fields = ['id', 'codigo', 'nome', 'descricao', 'diretor']

class SemestreLectivoSerializer(serializers.ModelSerializer):
    class Meta:
        model = SemestreLectivo
        fields = '__all__'



class DocenteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Docente
        fields = '__all__'

        
class DisciplinaSerializer(serializers.ModelSerializer):
    semestre=SemestreLectivoSerializer()
    docente_responsavel=DocenteSerializer()
    semestre = serializers.PrimaryKeyRelatedField(queryset=SemestreLectivo.objects.all())
    docente_responsavel = serializers.PrimaryKeyRelatedField(queryset=Docente.objects.all())
    class Meta:
        model = Disciplina
        fields = ['id', 'codigo', 'nome', 'carga_horaria', 'descricao', 'semestre', 'docente_responsavel']


class FuncionarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Funcionario
        fields = '__all__'

class AcionistaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Acionista
        fields = '__all__'

class DocenteDisciplinaSerializer(serializers.ModelSerializer):
    class Meta:
        model = DocenteDisciplina
        fields = '__all__'


class EstudanteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estudante
        fields = '__all__'

class EstudanteDisciplinaSerializer(serializers.ModelSerializer):
    class Meta:
        model = EstudanteDisciplina
        fields = '__all__'


class AvaliacaoSerializer(serializers.ModelSerializer):
    disciplina=DisciplinaSerializer()
    estudante=EstudanteSerializer()
    class Meta:
        model = Avaliacao
        fields = ['id','estudante','disciplina','nota1','nota2','nota3','nota4',]

class ExamesSerializer(serializers.ModelSerializer):
    disciplina=DisciplinaSerializer()
    estudante=EstudanteSerializer()
    class Meta:
        model = Exames
        fields = ['id','estudante','disciplina','exame','exame_recorrencia']

class PagamentoSerializer(serializers.ModelSerializer):
    estudante_nome = serializers.CharField(source='estudante.nome', read_only=True)
    estudante_id = serializers.IntegerField(source='estudante.id')  # Remover read_only aqui
    estudante_id = serializers.IntegerField()


    class Meta:
        model = Pagamento
        fields = ['id', 'tipo_pagamento', 'valor', 'data_pagamento', 'metodo_pagamento', 'mes_referente', 'estudante_nome', 'estudante_id']

    def create(self, validated_data):
        # Substituir estudante pelo estudante autenticado
        estudante = self.context['request'].user.estudante
        validated_data['estudante'] = estudante
        return super().create(validated_data)
    
    def create(self, validated_data):
        estudante_id = validated_data.pop('estudante_id')
        estudante = Estudante.objects.get(id=estudante_id)
        pagamento = Pagamento.objects.create(estudante=estudante, **validated_data)
        return pagamento



class EstudanteCursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = EstudanteCurso
        fields = ['id', 'estudante', 'curso']

    def validate(self, data):
        # Validar se o estudante já está inscrito no curso
        if EstudanteCurso.objects.filter(estudante=data['estudante'], curso=data['curso']).exists():
            raise serializers.ValidationError("O estudante já está inscrito neste curso.")
        return data