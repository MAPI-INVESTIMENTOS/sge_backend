from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView 
from rest_framework.permissions import AllowAny
from rest_framework.generics import get_object_or_404

######
from rest_framework import permissions
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.views import LoginView as KnoxLoginView
from knox.auth import TokenAuthentication
from django.contrib.auth import login as django_login
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from .models import (Curso, SemestreLectivo, Disciplina, Docente, Funcionario, Acionista, 
                     DocenteDisciplina, DiretorCurso,Estudante,EstudanteDisciplina,Pagamento,Avaliacao)
from .serializers import (
                            DiretorCursoSerializer, CursoSerializer, SemestreLectivoSerializer, EstudanteSerializer,EstudanteDisciplinaSerializer,
                            DisciplinaSerializer, DocenteSerializer, FuncionarioSerializer, AcionistaSerializer, DocenteDisciplinaSerializer,
                            PagamentoSerializer,AvaliacaoSerializer)
from knox.auth import AuthToken
#Login views
""""
from knox.views import LoginView as KnoxLoginView
from knox.auth import AuthToken
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.authtoken.serializers import AuthTokenSerializer
from django.contrib.auth.models import User
from .models import Docente, Estudante, DiretorCurso, Funcionario, Acionista

class LoginAPI(KnoxLoginView):
    permission_classes = (permissions.AllowAny,)
    authentication_classes = [TokenAuthentication]
    
    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        grupo = None
        identifica = None
        nome_completo = None
        nuit = None

        # Verificar grupo do usuário
        if user.groups.exists():
            grupo = user.groups.all()[0].name
            identifica = user.id
        if user.is_superuser:
            grupo = 'Admin'
            identifica = user.id

        # Autenticar token
        _, token = AuthToken.objects.create(user)

        # Identificar o tipo de usuário
        if grupo == "docente":
            try:
                docente = Docente.objects.get(user=user.id)
                nome_completo = f'{docente.nome} {docente.apelido}'
                nuit = docente.nuit
            except Docente.DoesNotExist:
                nome_completo = "Docente não encontrado"
        elif grupo == "estudante":
            try:
                estudante = Estudante.objects.get(user=user.id)
                nome_completo = f'{estudante.nome} {estudante.apelido}'
                nuit = estudante.nuit
            except Estudante.DoesNotExist:
                nome_completo = "Estudante não encontrado"
        elif grupo == "diretor_curso":
            try:
                diretor = DiretorCurso.objects.get(user=user.id)
                nome_completo = f'{diretor.nome} {diretor.apelido}'
                nuit = diretor.nuit
            except DiretorCurso.DoesNotExist:
                nome_completo = "Diretor de Curso não encontrado"
        elif grupo == "funcionario":
            try:
                funcionario = Funcionario.objects.get(user=user.id)
                nome_completo = f'{funcionario.nome} {funcionario.apelido}'
                nuit = funcionario.nuit
            except Funcionario.DoesNotExist:
                nome_completo = "Funcionário não encontrado"
        elif grupo == "acionista":
            try:
                acionista = Acionista.objects.get(user=user.id)
                nome_completo = f'{acionista.nome} {acionista.apelido}'
                nuit = acionista.nuit
            except Acionista.DoesNotExist:
                nome_completo = "Acionista não encontrado"
        else:
            nome_completo = "Usuário não identificado"

        return Response({
            'token': token,
            'nome_completo': nome_completo,
            'grupo': grupo,
            'nuit': nuit,
        })


"""
class CustomLoginView(KnoxLoginView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        django_login(request, user)
        
        user_type = None
        redirect_url = None
        
        if Funcionario.objects.filter(user=user).exists():
            user_type = "funcionario"
            redirect_url = "/funcionario/"
        elif Estudante.objects.filter(user=user).exists():
            user_type = "estudante"
            redirect_url = "/estudante/"
        elif Docente.objects.filter(user=user).exists():
            user_type = "docente"
            redirect_url = "/docente/"
        elif Acionista.objects.filter(user=user).exists():
            user_type = "acionista"
            redirect_url = "/acionista/"
        else:
            return Response({'error': 'User type not found'}, status=status.HTTP_400_BAD_REQUEST)
        _, token = AuthToken.objects.create(user)
        print(token)
        return Response({
            "username": user.username,
            "email": user.email,
            "token":token,
            'url':redirect_url
        })





#  director d0 curso
class DiretorCursosAPIView(generics.ListCreateAPIView):
    queryset = DiretorCurso.objects.all()
    serializer_class = DiretorCursoSerializer
    permission_classes = [AllowAny]
#    authentication_classes = [TokenAuthentication]

    def get(self, request):
        diretorcursos = self.queryset.all()
        serializer = self.serializer_class(diretorcursos, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    

class DiretorCursoAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = DiretorCurso.objects.all()
    serializer_class = DiretorCursoSerializer
    permission_classes = [AllowAny]
#    authentication_classes = [TokenAuthentication]
    def get(self, request, pk):
        diretorcurso = get_object_or_404(self.queryset, pk=pk)
        serializer = self.serializer_class(diretorcurso)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        diretorcurso = get_object_or_404(self.queryset, pk=pk)
        serializer = self.serializer_class(diretorcurso, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        diretorcurso = get_object_or_404(self.queryset, pk=pk)
        diretorcurso.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


#cursos
class CursosAPIView(generics.ListCreateAPIView):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer
    permission_classes = [AllowAny]
    authentication_classes = [TokenAuthentication]

    def get(self, request):
        cursos = self.queryset.all()
        serializer = self.serializer_class(cursos, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CursoAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer
    permission_classes = [AllowAny]
   # authentication_classes = [TokenAuthentication]
"""
    def get(self, request, pk):
        curso = get_object_or_404(self.queryset, pk=pk)
        serializer = self.serializer_class(curso)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        curso = get_object_or_404(self.queryset, pk=pk)
        serializer = self.serializer_class(curso, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        curso = get_object_or_404(self.queryset, pk=pk)
        curso.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
"""

#semestre
class SemestresLectivoAPIView(generics.ListCreateAPIView):
    queryset = SemestreLectivo.objects.all()
    serializer_class = SemestreLectivoSerializer
    permission_classes = [AllowAny]
 #   authentication_classes = [TokenAuthentication]
    #veros

    def get_queryset(self):
        curso_pk = self.kwargs.get('curso_pk')
        if curso_pk:
            return self.queryset.filter(curso_id=curso_pk)
        return self.queryset.all()

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
"""
    def get(self, request):
        semestres = self.queryset.all()
        serializer = self.serializer_class(semestres, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# def get_queryset trabalha com lista
    def get_queryset(self):
        if self.kwargs.get('curso_pk'):
            return self.queryset.filter(curso_id =self.kwargs.get('curso_pk'))
        return self.queryset.all()
    
    def get_queryset(self):
        curso_pk = self.kwargs.get('curso_pk')
        if curso_pk:
            return self.queryset.filter(curso_id=curso_pk)
        return self.queryset.all()
    
def get(self, request, curso_pk=None):
        # Filtra os semestres pelo curso associado
        curso = Curso.objects.get(pk=curso_pk)
        semestres = SemestreLectivo.objects.filter(curso=curso)
        serializer = self.serializer_class(semestres, many=True)
        return Response(serializer.data)    

        """
class SemestreLectivoAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = SemestreLectivo.objects.all()
    serializer_class = SemestreLectivoSerializer
#   permission_classes = [IsAuthenticated]
    permission_classes = [AllowAny]
    authentication_classes = [TokenAuthentication]

    """def get(self, request, pk):
        semestre = get_object_or_404(self.queryset, pk=pk)
        serializer = self.serializer_class(semestre)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        semestre = get_object_or_404(self.queryset, pk=pk)
        serializer = self.serializer_class(semestre, dados=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        semestre = get_object_or_404(self.queryset, pk=pk)
        semestre.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    """
# get_object trabalha com um objecto especifico
    def get_object(self):
        if self.kwargs.get('curso_pk'):
            return get_object_or_404(self.get_queryset(), curso_id=self.kwargs.get('curso_pk'), pk=self.kwargs.get('semestrelectivo_pk'))
        return get_object_or_404(self.get_queryset(), pk=self.kwargs.get('semestrelectivo_pk'))
    
    def get_object(self):
        curso_pk = self.kwargs.get('curso_pk')
        semestrelectivo_pk = self.kwargs.get('semestrelectivo_pk')
        if curso_pk and semestrelectivo_pk:
            return get_object_or_404(self.get_queryset(), curso_id=curso_pk, pk=semestrelectivo_pk)
        return get_object_or_404(self.get_queryset(), pk=semestrelectivo_pk)


#disciplina

class DisciplinasAPIView(generics.ListAPIView):
    serializer_class = DisciplinaSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        # Extraindo parâmetros da URL
        curso_pk = self.kwargs.get('curso_pk')
        semestrelectivo_pk = self.kwargs.get('semestrelectivo_pk')

        # Iniciando o queryset com todos os objetos de Disciplina
        queryset = Disciplina.objects.all()

        # Filtrando o queryset com base nos parâmetros da URL fornecidos
        if curso_pk:
            queryset = queryset.filter(curso__id=curso_pk)
        if semestrelectivo_pk:
            queryset = queryset.filter(semestre__id=semestrelectivo_pk)
        
        return queryset


class DisciplinasAPIView(generics.ListAPIView):
    serializer_class = DisciplinaSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        # Extraindo parâmetros da URL
        semestrelectivo_pk = self.kwargs.get('semestrelectivo_pk')

        # Iniciando o queryset com todos os objetos de Disciplina
        queryset = Disciplina.objects.all()

        # Filtrando o queryset com base no parâmetro semestrelectivo_pk
        if semestrelectivo_pk:
            queryset = queryset.filter(semestre__id=semestrelectivo_pk)
        
        return queryset


class DisciplinaAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Disciplina.objects.all()
    serializer_class = DisciplinaSerializer
    permission_classes = [AllowAny]

    def get_object(self):
        semestrelectivo_pk = self.kwargs.get('semestrelectivo_pk')
        disciplina_pk = self.kwargs.get('disciplina_pk')
        if semestrelectivo_pk and disciplina_pk:
            return get_object_or_404(self.get_queryset(), semestre_id=semestrelectivo_pk, pk=disciplina_pk)
        return get_object_or_404(self.get_queryset(), pk=disciplina_pk)




"""
class DisciplinaAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Disciplina.objects.all()
    serializer_class = DisciplinaSerializer
    permission_classes = [AllowAny]
#    authentication_classes = [TokenAuthentication]

    def get(self, request, pk):
        disciplina = get_object_or_404(self.queryset, pk=pk)
        serializer = self.serializer_class(disciplina)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        disciplina = get_object_or_404(self.queryset, pk=pk)
        serializer = self.serializer_class(disciplina, dados=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        disciplina = get_object_or_404(self.queryset, pk=pk)
        disciplina.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def get_object(self):
        if self.kwargs.get('semestrelectivo_pk'):
            return get_object_or_404(self.get_queryset(), semestrelectivo_id=self.kwargs.get('semestrelectivo_pk'), pk=self.kwargs.get('disciplina_pk'))
        return get_object_or_404(self.get_queryset(), pk=self.kwargs.get('disciplina_pk'))

    def get_object(self):
        if self.kwargs.get('semestrelectivo_pk'):
            return get_object_or_404(self.get_queryset(), semestre_id=self.kwargs.get('semestrelectivo_pk'), pk=self.kwargs.get('disciplina_pk'))
        return get_object_or_404(self.get_queryset(), pk=self.kwargs.get('disciplina_pk'))

    def get_object(self):
        semestrelectivo_pk = self.kwargs.get('semestrelectivo_pk')
        disciplina_pk = self.kwargs.get('disciplina_pk')
        if semestrelectivo_pk and disciplina_pk:
            return get_object_or_404(self.get_queryset(), semestre_id=semestrelectivo_pk, pk=disciplina_pk)
        return get_object_or_404(self.get_queryset(), pk=disciplina_pk)
"""
#docente
class DocentesAPIView(generics.ListCreateAPIView):
    queryset = Docente.objects.all()
    serializer_class = DocenteSerializer
    permission_classes = [AllowAny]
   # authentication_classes = [TokenAuthentication]
"""
    def get(self, request):
        docentes = self.queryset.all()
        serializer = self.serializer_class(docentes, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
"""
class DocenteAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Docente.objects.all()
    serializer_class = DocenteSerializer
    permission_classes = [AllowAny]
  #  authentication_classes = [TokenAuthentication]
"""
    def get(self, request, pk):
        docente = get_object_or_404(self.queryset, pk=pk)
        serializer = self.serializer_class(docente)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        docente = get_object_or_404(self.queryset, pk=pk)
        serializer = self.serializer_class(docente, dados=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        docente = get_object_or_404(self.queryset, pk=pk)
        docente.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
"""
#Estudante
class EstudantesAPIView(generics.ListCreateAPIView):
    queryset = Estudante.objects.all()
    serializer_class = EstudanteSerializer
    permission_classes = [AllowAny]
  #  authentication_classes = [TokenAuthentication]

    def get(self, request):
        estudantes = self.queryset.all()
        serializer = self.serializer_class(estudantes, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 

class EstudanteAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Estudante.objects.all()
    serializer_class = EstudanteSerializer
    permission_classes = [AllowAny]
  #  authentication_classes = [TokenAuthentication]

    def get(self, request, pk):
        estudante = get_object_or_404(self.queryset, pk=pk)
        serializer = self.serializer_class(estudante)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        estudante = get_object_or_404(self.queryset, pk=pk)
        serializer = self.serializer_class(estudante, dados=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        estudante = get_object_or_404(self.queryset, pk=pk)
        estudante.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class EstudantesDisciplinasAPIView(generics.ListCreateAPIView):
    queryset = EstudanteDisciplina.objects.all()
    serializer_class = EstudanteDisciplinaSerializer
    permission_classes = [AllowAny]
   # authentication_classes = [TokenAuthentication]

class EstudanteDisciplinaAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = EstudanteDisciplina.objects.all()
    serializer_class = EstudanteDisciplinaSerializer
    permission_classes = [AllowAny]
#    authentication_classes = [TokenAuthentication]

class PagamentosAPIView(generics.ListCreateAPIView):
    queryset = Pagamento.objects.all()
    serializer_class = PagamentoSerializer
    permission_classes = [AllowAny]
#    authentication_classes = [TokenAuthentication]

def get_queryset(self):
        estudante_id = self.kwargs['estudante_id']
        return Pagamento.objects.filter(estudante_id=estudante_id)    

class PagamentoAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Pagamento.objects.all()
    serializer_class = PagamentoSerializer
#    permission_classes = [IsAuthenticated]
    permission_classes = [AllowAny]
#    authentication_classes = [TokenAuthentication]

    def get_object(self):
        estudante_id = self.kwargs['estudante_id']
        pagamento_id = self.kwargs['pagamento_id']
        return get_object_or_404(Pagamento, estudante_id=estudante_id, id=pagamento_id)


class AvaliacoesAPIView(generics.ListCreateAPIView):
    serializer_class = AvaliacaoSerializer
    permission_classes = [IsAuthenticated]  # Ensure that only authenticated users can access this view

    def get_queryset(self):
        # Get the authenticated user
        user = self.request.user

        # Retrieve the associated student (assuming the user model is related to the Estudante model)
        estudante = getattr(user, 'estudante', None)

        # Filter evaluations by the authenticated student's ID
        if estudante:
            return Avaliacao.objects.filter(estudante=estudante)
        else:
            return Avaliacao.objects.none() 

class AvaliacaoAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer
#    permission_classes = [IsAuthenticated]
    permission_classes = [AllowAny]
    lookup_field = 'avaliacao_id'
    

    def get_object(self):
        estudante_id = self.kwargs['estudante_id']
        avaliacao_id = self.kwargs['avaliacao_id']
        return get_object_or_404(Avaliacao, estudante_id=estudante_id, id=avaliacao_id)





#funcionario
class FuncionariosAPIView(generics.ListCreateAPIView):
    queryset = Funcionario.objects.all()
    serializer_class = FuncionarioSerializer
#    permission_classes = [IsAuthenticated]
    permission_classes = [AllowAny]

    def get(self, request):
        funcionarios = self.queryset.all()
        serializer = self.serializer_class(funcionarios, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class FuncionarioAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Funcionario.objects.all()
    serializer_class = FuncionarioSerializer
#    permission_classes = [IsAuthenticated]
    permission_classes = [AllowAny]

    def get(self, request, pk):
        funcionario = get_object_or_404(self.queryset, pk=pk)
        serializer = self.serializer_class(funcionario)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        funcionario = get_object_or_404(self.queryset, pk=pk)
        serializer = self.serializer_class(funcionario, dados=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        funcionario = get_object_or_404(self.queryset, pk=pk)
        funcionario.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


#acionista
class AcionistasAPIView(generics.ListCreateAPIView):
    queryset = Acionista.objects.all()
    serializer_class = AcionistaSerializer
#    permission_classes = [IsAuthenticated]
    permission_classes = [AllowAny]

class AcionistaAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Acionista.objects.all()
    serializer_class = AcionistaSerializer
#    permission_classes = [IsAuthenticated]
    permission_classes = [AllowAny]
    authentication_classes = [TokenAuthentication]


#docente
class DocenteDisciplinasAPIView(generics.ListCreateAPIView):
    queryset = DocenteDisciplina.objects.all()
    serializer_class = DocenteDisciplinaSerializer
#    permission_classes = [IsAuthenticated]
    permission_classes = [AllowAny]
    authentication_classes = [TokenAuthentication]


class DocenteDisciplinaAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = DocenteDisciplina.objects.all()
    serializer_class = DocenteDisciplinaSerializer
#    permission_classes = [IsAuthenticated]
    permission_classes = [AllowAny]
    authentication_classes = [TokenAuthentication]


