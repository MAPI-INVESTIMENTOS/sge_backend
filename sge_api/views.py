from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView 
from rest_framework.permissions import AllowAny
from rest_framework.generics import get_object_or_404
from knox.views import LoginView as KnoxLoginView
from knox.auth import AuthToken
from rest_framework import permissions
from rest_framework.authtoken.serializers import AuthTokenSerializer
from django.contrib.auth.models import User
from knox.auth import TokenAuthentication
from django.contrib.auth import login as django_login
from rest_framework import status
from rest_framework.permissions import IsAuthenticated


from .models import (Curso, SemestreLectivo, Disciplina, Docente, Funcionario, Acionista,Exames,EstudanteCurso,
                     DocenteDisciplina, DiretorCurso,Estudante,EstudanteDisciplina,Pagamento,Avaliacao)
from .serializers import (
                            DiretorCursoSerializer, CursoSerializer, SemestreLectivoSerializer, EstudanteSerializer,EstudanteDisciplinaSerializer,
                            DisciplinaSerializer, DocenteSerializer, FuncionarioSerializer, AcionistaSerializer, DocenteDisciplinaSerializer,
                            PagamentoSerializer,AvaliacaoSerializer,ExamesSerializer,EstudanteCursoSerializer)

#Login views

from .models import Docente, Estudante, DiretorCurso, Funcionario, Acionista


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
    authentication_classes = [TokenAuthentication]

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
    authentication_classes = [TokenAuthentication]

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
    authentication_classes = [TokenAuthentication]


#semestre
class SemestresLectivoAPIView(generics.ListCreateAPIView):
    queryset = SemestreLectivo.objects.all()
    serializer_class = SemestreLectivoSerializer
    permission_classes = [AllowAny]
    authentication_classes = [TokenAuthentication]
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

class SemestreLectivoAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = SemestreLectivo.objects.all()
    serializer_class = SemestreLectivoSerializer
    permission_classes = [AllowAny]
    authentication_classes = [TokenAuthentication]


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
class DisciplinasAPIView(generics.ListCreateAPIView):
    queryset = Disciplina.objects.all()
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


#docente
class DocentesAPIView(generics.ListCreateAPIView):
    queryset = Docente.objects.all()
    serializer_class = DocenteSerializer
    permission_classes = [AllowAny]
    authentication_classes = [TokenAuthentication]

class DocenteAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Docente.objects.all()
    serializer_class = DocenteSerializer
    permission_classes = [AllowAny]
    authentication_classes = [TokenAuthentication]

#Estudante
class EstudantesAPIView(generics.ListCreateAPIView):
    queryset = Estudante.objects.all()
    serializer_class = EstudanteSerializer
    permission_classes = [AllowAny]
    authentication_classes = [TokenAuthentication]

class EstudanteAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Estudante.objects.all()
    serializer_class = EstudanteSerializer
    permission_classes = [AllowAny]
    authentication_classes = [TokenAuthentication]

class EstudantesDisciplinasAPIView(generics.ListCreateAPIView):
    queryset = EstudanteDisciplina.objects.all()
    serializer_class = EstudanteDisciplinaSerializer
    permission_classes = [AllowAny]
    authentication_classes = [TokenAuthentication]

class EstudanteDisciplinaAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = EstudanteDisciplina.objects.all()
    serializer_class = EstudanteDisciplinaSerializer
    permission_classes = [AllowAny]
    authentication_classes = [TokenAuthentication]

class PagamentosAPIView(generics.ListCreateAPIView):
    serializer_class = PagamentoSerializer
    permission_classes = [AllowAny]
    authentication_classes = [TokenAuthentication]

    def get_queryset(self):
        # Get the student from the authenticated user
        estudante = self.request.user.estudante
        return Pagamento.objects.filter(estudante=estudante)
    

class PagamentoAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PagamentoSerializer
    permission_classes = [AllowAny]
    authentication_classes = [TokenAuthentication]

    def get_object(self):
        estudante = self.request.user.estudante
        pagamento_id = self.kwargs['pagamento_id']
        return get_object_or_404(Pagamento, estudante=estudante, id=pagamento_id)



class AvaliacoesAPIView(generics.ListCreateAPIView):
    serializer_class = AvaliacaoSerializer
    permission_classes = [AllowAny]  # Ensure that only authenticated users can access this view
    authentication_classes = [TokenAuthentication]

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
    permission_classes = [AllowAny]
    authentication_classes = [TokenAuthentication]
    lookup_field = 'avaliacao_id'
    
    def get_object(self):
        estudante_id = self.kwargs['estudante_id']
        avaliacao_id = self.kwargs['avaliacao_id']
        return get_object_or_404(Avaliacao, estudante_id=estudante_id, id=avaliacao_id)


class ExamesAPIView(generics.ListCreateAPIView):
    serializer_class = ExamesSerializer
    permission_classes = [AllowAny]  # Ensure that only authenticated users can access this view
    authentication_classes = [TokenAuthentication]

    def get_queryset(self):
        # Get the authenticated user
        user = self.request.user

        # Retrieve the associated student (assuming the user model is related to the Estudante model)
        estudante = getattr(user, 'estudante', None)

        # Filter evaluations by the authenticated student's ID
        if estudante:
            return Exames.objects.filter(estudante=estudante)
        else:
            return Exames.objects.none() 

class ExameAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Exames.objects.all()
    serializer_class = ExamesSerializer
    permission_classes = [AllowAny]
    authentication_classes = [TokenAuthentication]
    lookup_field = 'exame_id'
    
    def get_object(self):
        estudante_id = self.kwargs['estudante_id']
        exame_id = self.kwargs['exame_id']
        return get_object_or_404(Exames, estudante_id=estudante_id, id=exame_id)


#funcionario
class FuncionariosAPIView(generics.ListCreateAPIView):
    queryset = Funcionario.objects.all()
    serializer_class = FuncionarioSerializer
    permission_classes = [AllowAny]
    authentication_classes = [TokenAuthentication]

class FuncionarioAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Funcionario.objects.all()
    serializer_class = FuncionarioSerializer
    permission_classes = [AllowAny]
    authentication_classes = [TokenAuthentication]


#acionista
class AcionistasAPIView(generics.ListCreateAPIView):
    queryset = Acionista.objects.all()
    serializer_class = AcionistaSerializer
    permission_classes = [AllowAny]
    authentication_classes = [TokenAuthentication]

class AcionistaAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Acionista.objects.all()
    serializer_class = AcionistaSerializer
    permission_classes = [AllowAny]
    authentication_classes = [TokenAuthentication]


#docente
class DocenteDisciplinasAPIView(generics.ListCreateAPIView):
    queryset = DocenteDisciplina.objects.all()
    serializer_class = DocenteDisciplinaSerializer
    permission_classes = [AllowAny]
    authentication_classes = [TokenAuthentication]


class DocenteDisciplinaAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = DocenteDisciplina.objects.all()
    serializer_class = DocenteDisciplinaSerializer
    permission_classes = [AllowAny]
    authentication_classes = [TokenAuthentication]


class EstudanteCursoListCreateAPIView(generics.ListCreateAPIView):
    queryset = EstudanteCurso.objects.all()
    serializer_class = EstudanteCursoSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class EstudanteCursoDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = EstudanteCurso.objects.all()
    serializer_class = EstudanteCursoSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [AllowAny]