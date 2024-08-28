from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView

from rest_framework.authtoken.serializers import AuthTokenSerializer

from knox.models import AuthToken
from knox.views import LoginView as KnoxLoginView
from knox.auth import TokenAuthentication

from django.contrib.auth import login as django_login

from .models import (Curso, SemestreLectivo, Disciplina, Docente, Estudante, 
                     Funcionario, Acionista, DocenteDisciplina, 
                     EstudanteDisciplina, Avaliacao, DiretorCurso)
from .serializers import (DiretorCursoSerializer, CursoSerializer, SemestreLectivoSerializer, 
                          DisciplinaSerializer, DocenteSerializer, EstudanteSerializer, 
                          FuncionarioSerializer, AcionistaSerializer, DocenteDisciplinaSerializer, 
                          EstudanteDisciplinaSerializer, AvaliacaoSerializer)


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

class CursoListCreateView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    def get(self, request):
        cursos = Curso.objects.all()
        serializer = CursoSerializer(cursos, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CursoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CursoDetailView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    def get(self, request, pk):
        try:
            curso = Curso.objects.get(pk=pk)
        except Curso.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = CursoSerializer(curso)
        return Response(serializer.data)

    def put(self, request, pk):
        try:
            curso = Curso.objects.get(pk=pk)
        except Curso.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = CursoSerializer(curso, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            curso = Curso.objects.get(pk=pk)
        except Curso.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        curso.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# Repeat similar pattern for other models

class SemestreLectivoListCreateView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    def get(self, request):
        semestres = SemestreLectivo.objects.all()
        serializer = SemestreLectivoSerializer(semestres, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = SemestreLectivoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SemestreLectivoDetailView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    def get(self, request, pk):
        try:
            semestre = SemestreLectivo.objects.get(pk=pk)
        except SemestreLectivo.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = SemestreLectivoSerializer(semestre)
        return Response(serializer.data)

    def put(self, request, pk):
        try:
            semestre = SemestreLectivo.objects.get(pk=pk)
        except SemestreLectivo.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = SemestreLectivoSerializer(semestre, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            semestre = SemestreLectivo.objects.get(pk=pk)
        except SemestreLectivo.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        semestre.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class DisciplinaListCreateView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    def get(self, request):
        disciplinas = Disciplina.objects.all()
        serializer = DisciplinaSerializer(disciplinas, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = DisciplinaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DisciplinaDetailView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    def get(self, request, pk):
        try:
            disciplina = Disciplina.objects.get(pk=pk)
        except Disciplina.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = DisciplinaSerializer(disciplina)
        return Response(serializer.data)

    def put(self, request, pk):
        try:
            disciplina = Disciplina.objects.get(pk=pk)
        except Disciplina.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = DisciplinaSerializer(disciplina, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            disciplina = Disciplina.objects.get(pk=pk)
        except Disciplina.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        disciplina.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class DocenteListCreateView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    def get(self, request):
        docentes = Docente.objects.all()
        serializer = DocenteSerializer(docentes, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = DocenteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DocenteDetailView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    def get(self, request, pk):
        try:
            docente = Docente.objects.get(pk=pk)
        except Docente.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = DocenteSerializer(docente)
        return Response(serializer.data)

    def put(self, request, pk):
        try:
            docente = Docente.objects.get(pk=pk)
        except Docente.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = DocenteSerializer(docente, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            docente = Docente.objects.get(pk=pk)
        except Docente.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        docente.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class EstudanteListCreateView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    def get(self, request):
        estudantes = Estudante.objects.all()
        serializer = EstudanteSerializer(estudantes, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = EstudanteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class EstudanteDetailView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    def get(self, request, pk):
        try:
            estudante = Estudante.objects.get(pk=pk)
        except Estudante.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = EstudanteSerializer(estudante)
        return Response(serializer.data)

    def put(self, request, pk):
        try:
            estudante = Estudante.objects.get(pk=pk)
        except Estudante.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = EstudanteSerializer(estudante, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            estudante = Estudante.objects.get(pk=pk)
        except Estudante.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        estudante.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class FuncionarioListCreateView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    def get(self, request):
        funcionarios = Funcionario.objects.all()
        serializer = FuncionarioSerializer(funcionarios, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = FuncionarioSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class FuncionarioDetailView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    def get(self, request, pk):
        try:
            funcionario = Funcionario.objects.get(pk=pk)
        except Funcionario.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = FuncionarioSerializer(funcionario)
        return Response(serializer.data)

    def put(self, request, pk):
        try:
            funcionario = Funcionario.objects.get(pk=pk)
        except Funcionario.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = FuncionarioSerializer(funcionario, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            funcionario = Funcionario.objects.get(pk=pk)
        except Funcionario.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        funcionario.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class AcionistaListCreateView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    def get(self, request):
        acionistas = Acionista.objects.all()
        serializer = AcionistaSerializer(acionistas, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = AcionistaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AcionistaDetailView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    def get(self, request, pk):
        try:
            acionista = Acionista.objects.get(pk=pk)
        except Acionista.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = AcionistaSerializer(acionista)
        return Response(serializer.data)

    def put(self, request, pk):
        try:
            acionista = Acionista.objects.get(pk=pk)
        except Acionista.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = AcionistaSerializer(acionista, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            acionista = Acionista.objects.get(pk=pk)
        except Acionista.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        acionista.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class DocenteDisciplinaListCreateView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    def get(self, request):
        docente_disciplinas = DocenteDisciplina.objects.all()
        serializer = DocenteDisciplinaSerializer(docente_disciplinas, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = DocenteDisciplinaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DocenteDisciplinaDetailView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    def get(self, request, pk):
        try:
            docente_disciplina = DocenteDisciplina.objects.get(pk=pk)
        except DocenteDisciplina.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = DocenteDisciplinaSerializer(docente_disciplina)
        return Response(serializer.data)

    def put(self, request, pk):
        try:
            docente_disciplina = DocenteDisciplina.objects.get(pk=pk)
        except DocenteDisciplina.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = DocenteDisciplinaSerializer(docente_disciplina, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            docente_disciplina = DocenteDisciplina.objects.get(pk=pk)
        except DocenteDisciplina.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        docente_disciplina.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class EstudanteDisciplinaListCreateView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    def get(self, request):
        estudante_disciplinas = EstudanteDisciplina.objects.all()
        serializer = EstudanteDisciplinaSerializer(estudante_disciplinas, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = EstudanteDisciplinaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class EstudanteDisciplinaDetailView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    def get(self, request, pk):
        try:
            estudante_disciplina = EstudanteDisciplina.objects.get(pk=pk)
        except EstudanteDisciplina.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = EstudanteDisciplinaSerializer(estudante_disciplina)
        return Response(serializer.data)

    def put(self, request, pk):
        try:
            estudante_disciplina = EstudanteDisciplina.objects.get(pk=pk)
        except EstudanteDisciplina.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = EstudanteDisciplinaSerializer(estudante_disciplina, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            estudante_disciplina = EstudanteDisciplina.objects.get(pk=pk)
        except EstudanteDisciplina.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        estudante_disciplina.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class AvaliacaoListCreateView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    def get(self, request):
        avaliacoes = Avaliacao.objects.all()
        serializer = AvaliacaoSerializer(avaliacoes, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = AvaliacaoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AvaliacaoDetailView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    def get(self, request, pk):
        try:
            avaliacao = Avaliacao.objects.get(pk=pk)
        except Avaliacao.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = AvaliacaoSerializer(avaliacao)
        return Response(serializer.data)

    def put(self, request, pk):
        try:
            avaliacao = Avaliacao.objects.get(pk=pk)
        except Avaliacao.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = AvaliacaoSerializer(avaliacao, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            avaliacao = Avaliacao.objects.get(pk=pk)
        except Avaliacao.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        avaliacao.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class DiretorCursoListCreateView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    def get(self, request):
        diretores = DiretorCurso.objects.all()
        serializer = DiretorCursoSerializer(diretores, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = DiretorCursoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DiretorCursoDetailView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    def get(self, request, pk):
        try:
            diretor = DiretorCurso.objects.get(pk=pk)
        except DiretorCurso.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = DiretorCursoSerializer(diretor)
        return Response(serializer.data)

    def put(self, request, pk):
        try:
            diretor = DiretorCurso.objects.get(pk=pk)
        except DiretorCurso.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = DiretorCursoSerializer(diretor, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            diretor = DiretorCurso.objects.get(pk=pk)
        except DiretorCurso.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        diretor.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class EstudanteAvaliacaoListCreateView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    def get(self, request, estudante_id):
        try:
            estudante = Estudante.objects.get(pk=estudante_id)
        except Estudante.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        avaliacoes = Avaliacao.objects.filter(estudante=estudante)
        serializer = AvaliacaoSerializer(avaliacoes, many=True)
        return Response(serializer.data)

    def post(self, request, estudante_id):
        try:
            estudante = Estudante.objects.get(pk=estudante_id)
        except Estudante.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        request.data['estudante'] = estudante_id
        serializer = AvaliacaoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class EstudanteAvaliacaoDetailView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    def get(self, request, estudante_id, pk):
        try:
            estudante = Estudante.objects.get(pk=estudante_id)
            avaliacao = Avaliacao.objects.get(pk=pk, estudante=estudante)
        except (Estudante.DoesNotExist, Avaliacao.DoesNotExist):
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = AvaliacaoSerializer(avaliacao)
        return Response(serializer.data)

    def put(self, request, estudante_id, pk):
        try:
            estudante = Estudante.objects.get(pk=estudante_id)
            avaliacao = Avaliacao.objects.get(pk=pk, estudante=estudante)
        except (Estudante.DoesNotExist, Avaliacao.DoesNotExist):
            return Response(status=status.HTTP_404_NOT_FOUND)
        request.data['estudante'] = estudante_id
        serializer = AvaliacaoSerializer(avaliacao, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, estudante_id, pk):
        try:
            estudante = Estudante.objects.get(pk=estudante_id)
            avaliacao = Avaliacao.objects.get(pk=pk, estudante=estudante)
        except (Estudante.DoesNotExist, Avaliacao.DoesNotExist):
            return Response(status=status.HTTP_404_NOT_FOUND)
        avaliacao.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)





"""
class DiretorCursoCreateAPIView(generics.CreateAPIView):
    queryset = Curso.objects.all()
    serializer_class = DiretorCursoSerializer    
    #permission_classes = [IsAuthenticated]

class DiretorCursoRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Curso.objects.all()
    serializer_class = DiretorCursoSerializer
"""

"""
class AvaliacaoListCreateView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        avaliacoes = Avaliacao.objects.all()
        serializer = AvaliacaoSerializer(avaliacoes, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = AvaliacaoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AvaliacaoDetailView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, pk):
        try:
            avaliacao = Avaliacao.objects.get(pk=pk)
        except Avaliacao.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = AvaliacaoSerializer(avaliacao)
        return Response(serializer.data)

    def put(self, request, pk):
        try:
            avaliacao = Avaliacao.objects.get(pk=pk)
        except Avaliacao.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = AvaliacaoSerializer(avaliacao, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            avaliacao = Avaliacao.objects.get(pk=pk)
        except Avaliacao.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        avaliacao.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



        #########################################
        class LoginAPI(KnoxLoginView):
    permission_classes = (permissions.AllowAny,)
    queryset = Empresa.objects.all()
    serializer_class = Empresa

    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        print(request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        grupo = None
        identifica = None
        if user.groups.exists():
            grupo = user.groups.all()[0].name
            identifica = user.id
        if user.is_superuser:
            grupo = 'Admin'
            identifica = user.id
        _, token = AuthToken.objects.create(user)

        ope = 1

        if grupo!="tribunal" and grupo!="operario" and grupo!="arquivo" :
            ope = Empresa.objects.get(user=user.id)
            ope = ope.Representante
        nuit = '2323'

        return Response({'token': token, 'nome_empresa':ope,'grupo': grupo})

"""