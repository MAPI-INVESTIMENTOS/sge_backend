from .views import CustomLoginView
from knox import views as knox_views
from django.urls import path
from .views import (CursoListCreateAPIView, CursoRetrieveUpdateDestroyAPIView,
                    PagamentoMatriculaListCreateAPIView, PagamentoMatriculaRetrieveUpdateDestroyAPIView,
                    PagamentoMensalidadeListCreateAPIView, PagamentoMensalidadeRetrieveUpdateDestroyAPIView,
                    SemestreLectivoListCreateAPIView, SemestreLectivoRetrieveUpdateDestroyAPIView,
                    DisciplinaListCreateAPIView, DisciplinaRetrieveUpdateDestroyAPIView,
                    DocenteListCreateAPIView, DocenteRetrieveUpdateDestroyAPIView,
                    EstudanteListCreateAPIView, EstudanteRetrieveUpdateDestroyAPIView,
                    FuncionarioListCreateAPIView, FuncionarioRetrieveUpdateDestroyAPIView,
                    AcionistaListCreateAPIView, AcionistaRetrieveUpdateDestroyAPIView,
                    ExamesListCreateAPIView,ExamesRetrieveUpdateDestroyAPIView,
                    TesteListCreateAPIView,TesteRetrieveUpdateDestroyAPIView)

urlpatterns = [

    path('api/login/', CustomLoginView.as_view(), name='login'),
    path('api/logout/', knox_views.LogoutView.as_view(), name='logout'),
    path('api/logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'),

    ###
    path('cursos/', CursoListCreateAPIView.as_view(), name='curso-list-create'),
    path('cursos/<int:pk>/', CursoRetrieveUpdateDestroyAPIView.as_view(), name='curso-detail'),

    path('semestre-lectivo/', SemestreLectivoListCreateAPIView.as_view(), name='semestre-lectivo-list-create'),
    path('semestre-lectivo/<int:pk>/', SemestreLectivoRetrieveUpdateDestroyAPIView.as_view(), name='semestre-lectivo-detail'),

    path('disciplinas/', DisciplinaListCreateAPIView.as_view(), name='disciplina-list-create'),
    path('disciplinas/<int:pk>/', DisciplinaRetrieveUpdateDestroyAPIView.as_view(), name='disciplina-detail'),

    path('docentes/', DocenteListCreateAPIView.as_view(), name='docente-list-create'),
    path('docentes/<int:pk>/', DocenteRetrieveUpdateDestroyAPIView.as_view(), name='docente-detail'),

    path('estudantes/', EstudanteListCreateAPIView.as_view(), name='estudante-list-create'),
    path('estudantes/<int:pk>/', EstudanteRetrieveUpdateDestroyAPIView.as_view(), name='estudante-detail'),

    path('funcionarios/', FuncionarioListCreateAPIView.as_view(), name='funcionario-list-create'),
    path('funcionarios/<int:pk>/', FuncionarioRetrieveUpdateDestroyAPIView.as_view(), name='funcionario-detail'),

    path('acionistas/', AcionistaListCreateAPIView.as_view(), name='acionista-list-create'),
    path('acionistas/<int:pk>/', AcionistaRetrieveUpdateDestroyAPIView.as_view(), name='acionista-detail'),

    path('pmatricula/', PagamentoMatriculaListCreateAPIView.as_view(), name='pmatricula-list-create'),
    path('pmatricula/<int:pk>/', PagamentoMatriculaRetrieveUpdateDestroyAPIView.as_view(), name='pmatricula-detail'),

    path('pmensalidade/', PagamentoMensalidadeListCreateAPIView.as_view(), name='pmensalidade-list-create'),
    path('pmensalidade/<int:pk>/', PagamentoMensalidadeRetrieveUpdateDestroyAPIView.as_view(), name='pmensalidade-detail'),

    path('avaliacao/', TesteListCreateAPIView.as_view(), name='avaliacao-list-create'),
    path('avaliacao/<int:pk>/', TesteRetrieveUpdateDestroyAPIView.as_view(), name='avaliacao-detail'),

    path('avaliacaoexame/', ExamesListCreateAPIView.as_view(), name='avaliacaoexame-list-create'),
    path('avaliacao/<int:estudante_id>/', ExamesRetrieveUpdateDestroyAPIView.as_view(), name='avaliacaoexame-detail'),

    

]
