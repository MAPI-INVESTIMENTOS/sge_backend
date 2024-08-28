from rest_framework import permissions
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.views import LoginView as KnoxLoginView
from django.contrib.auth import login as django_login
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

##
from rest_framework import generics
from .models import (Curso, SemestreLectivo, Disciplina, Docente, Estudante, Exames, Teste,
                     Funcionario, Acionista, PagamentoMatricula, PagamentoMensalidade
                     )
from .serializers import (CursoSerializer, SemestreLectivoSerializer, DisciplinaSerializer, 
                          DocenteSerializer, EstudanteSerializer, FuncionarioSerializer, AcionistaSerializer, 
                          PagamentoMatriculaSerializer, PagamentoMensalidadeSerializer,
                          TesteSerializer,ExamesSerializer)


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

        response = super(CustomLoginView, self).post(request, format=None)
        response.data['redirect_url'] = redirect_url
        response.data['user_type'] = user_type
        response.data['user_info'] = {
            "username": user.username,
            "email": user.email,
        }
        return response








# Curso Views
class CursoListCreateAPIView(generics.ListCreateAPIView):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer        
    #permission_classes = [IsAuthenticated]

class CursoRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer
    #permission_classes = [IsAuthenticated]

# PagamentoMatricula Views
class PagamentoMatriculaListCreateAPIView(generics.ListCreateAPIView):
    queryset = PagamentoMatricula.objects.all()
    serializer_class = PagamentoMatriculaSerializer
    #permission_classes = [IsAuthenticated]

class PagamentoMatriculaRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PagamentoMatricula.objects.all()
    serializer_class = PagamentoMatriculaSerializer
    #permission_classes = [IsAuthenticated]

# PagamentoMensalidade Views
class PagamentoMensalidadeListCreateAPIView(generics.ListCreateAPIView):
    queryset = PagamentoMensalidade.objects.all()
    serializer_class = PagamentoMensalidadeSerializer
    #permission_classes = [IsAuthenticated]


class PagamentoMensalidadeRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PagamentoMensalidade.objects.all()
    serializer_class = PagamentoMensalidadeSerializer
    #permission_classes = [IsAuthenticated]


# SemestreLectivo Views
class SemestreLectivoListCreateAPIView(generics.ListCreateAPIView):
    queryset = SemestreLectivo.objects.all()
    serializer_class = SemestreLectivoSerializer
    #permission_classes = [IsAuthenticated]


class SemestreLectivoRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = SemestreLectivo.objects.all()
    serializer_class = SemestreLectivoSerializer
    #permission_classes = [IsAuthenticated]


# Disciplina Views
class DisciplinaListCreateAPIView(generics.ListCreateAPIView):
    queryset = Disciplina.objects.all()
    serializer_class = DisciplinaSerializer
    #permission_classes = [IsAuthenticated]


class DisciplinaRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Disciplina.objects.all()
    serializer_class = DisciplinaSerializer
    #permission_classes = [IsAuthenticated]


# Turma Views


# Docente Views
class DocenteListCreateAPIView(generics.ListCreateAPIView):
    queryset = Docente.objects.all()
    serializer_class = DocenteSerializer
    #permission_classes = [IsAuthenticated]


class DocenteRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Docente.objects.all()
    serializer_class = DocenteSerializer
    #permission_classes = [IsAuthenticated]


# Estudante Views
class EstudanteListCreateAPIView(generics.ListCreateAPIView):
    queryset = Estudante.objects.all()
    serializer_class = EstudanteSerializer
    #permission_classes = [IsAuthenticated]


class EstudanteRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Estudante.objects.all()
    serializer_class = EstudanteSerializer
    #permission_classes = [IsAuthenticated]

    
# Funcionario Views
class FuncionarioListCreateAPIView(generics.ListCreateAPIView):
    queryset = Funcionario.objects.all()
    serializer_class = FuncionarioSerializer
    #permission_classes = [IsAuthenticated]


class FuncionarioRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Funcionario.objects.all()
    serializer_class = FuncionarioSerializer
    #permission_classes = [IsAuthenticated]


# Acionista Views
class AcionistaListCreateAPIView(generics.ListCreateAPIView):
    queryset = Acionista.objects.all()
    serializer_class = AcionistaSerializer
    #permission_classes = [IsAuthenticated]


class AcionistaRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Acionista.objects.all()
    serializer_class = AcionistaSerializer
    #permission_classes = [IsAuthenticated]


# Leciona Views
class TesteListCreateAPIView(generics.ListCreateAPIView):
    queryset = Teste.objects.all()
    serializer_class = TesteSerializer
    #permission_classes = [IsAuthenticated]


class TesteRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Teste.objects.all()
    serializer_class = TesteSerializer
    #permission_classes = [IsAuthenticated]


class ExamesListCreateAPIView(generics.ListCreateAPIView):
    queryset = Exames.objects.all()
    serializer_class = ExamesSerializer
    #permission_classes = [IsAuthenticated]


class ExamesRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TesteSerializer

    def get_queryset(self):
        estudante_id = self.kwargs['estudante_id']
        return Teste.objects.filter(estudante_id=estudante_id)

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
