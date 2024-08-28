from django.urls import path
from .views import CustomLoginView
from knox import views as knox_views
from knox import views as login 


from .views import (
    DiretorCursosAPIView, DiretorCursoAPIView,
    CursosAPIView, CursoAPIView,
    SemestresLectivoAPIView, SemestreLectivoAPIView,
    DisciplinasAPIView, DisciplinaAPIView,
    DocentesAPIView, DocenteAPIView,
    FuncionariosAPIView, FuncionarioAPIView,
    AcionistasAPIView, AcionistaAPIView,
    DocenteDisciplinasAPIView, DocenteDisciplinaAPIView,
    EstudanteAPIView, EstudantesAPIView,
    EstudanteDisciplinaAPIView, EstudantesDisciplinasAPIView,
    AvaliacaoAPIView,AvaliacoesAPIView,
    ExameAPIView,ExamesAPIView,
    PagamentoAPIView,PagamentosAPIView,
    EstudanteCursoListCreateAPIView, EstudanteCursoDetailAPIView
)

urlpatterns = [
    #Login

   # path('api/login/', knox_views.LoginView.as_view(), name='login'),
    path('api/login/', CustomLoginView.as_view(), name='login'),
    path('api/logout/', knox_views.LogoutView.as_view(), name='logout'),
    path('api/logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'),


    # DiretorCurso
    path('diretorcursos/', DiretorCursosAPIView.as_view(), name='diretorcursos-list-create'),
    path('diretorcursos/<int:pk>/', DiretorCursoAPIView.as_view(), name='diretorcurso-detail'),

    # Curso
    path('cursos/', CursosAPIView.as_view(), name='cursos-list-create'),
    path('cursos/<int:pk>/', CursoAPIView.as_view(), name='curso-detail'),

    # SemestreLectivo
    path('semestres/', SemestresLectivoAPIView.as_view(), name='semestreslectivo-list'),
    path('semestres/<int:pk>/', SemestreLectivoAPIView.as_view(), name='semestre'),
    path('cursos/<int:curso_pk>/semestres/', SemestresLectivoAPIView.as_view(), name='semestreslectivo-list-create'),
    path('cursos/<int:curso_pk>/semestres/<int:semestrelectivo_pk>/', SemestreLectivoAPIView.as_view(), name='semestrelectivo-detail'),

    # Disciplina
    path('disciplinas/', DisciplinasAPIView.as_view(), name='disciplinas-list'),
    path('disciplinas/<int:pk>/', DisciplinaAPIView.as_view(), name='disciplina'),
    path('cursos/<int:curso_pk>/semestres/<int:semestrelectivo_pk>/disciplinas/', DisciplinasAPIView.as_view(), name='disciplinas-list-create'),
    path('cursos/<int:curso_pk>/semestres/<int:semestrelectivo_pk>/disciplinas/<int:disciplina_pk>/', DisciplinaAPIView.as_view(), name='disciplina-detail'),
    #path('semestres/<int:semestrelectivo_pk>/disciplinas/', DisciplinasAPIView.as_view(), name='disciplinas-list-create'),
    #path('semestres/<int:semestrelectivo_pk>/disciplinas/<int:disciplina_pk>/', DisciplinaAPIView.as_view(), name='disciplina-detail'),
    # Docente
    path('docentes/', DocentesAPIView.as_view(), name='docentes-list-create'),
    path('docentes/<int:pk>/', DocenteAPIView.as_view(), name='docente-detail'),

    # Estudante
    path('estudantes/', EstudantesAPIView.as_view(), name='estudantes-list-create'),
    path('estudantes/<int:pk>/', EstudanteAPIView.as_view(), name='estudante-detail'),

    # EstudanteDisciplina
    path('estudantedisciplinas/', EstudantesDisciplinasAPIView.as_view(), name='estudantedisciplinas-list-create'),
    path('estudantedisciplinas/<int:pk>/', EstudanteDisciplinaAPIView.as_view(), name='estudantedisciplina-detail'),

    # Avaliação
    path('avaliacoes/', AvaliacoesAPIView.as_view(), name='avaliacoes-list-create'),
    path('avaliacoes/<int:pk>/', AvaliacaoAPIView.as_view(), name='avaliacao-detail'),
    path('estudantes/avaliacoes/', AvaliacoesAPIView.as_view(), name='avaliacoes-estudante'),
    path('estudantes/<int:estudante_id>/avaliacoes/<int:avaliacao_id>/', AvaliacaoAPIView.as_view(), name='avaliacao-estudante-detail'),

    path('exames/', ExamesAPIView.as_view(), name='avaliacoes-list-create'),
    path('exames/<int:pk>/', ExameAPIView.as_view(), name='avaliacao-detail'),
    path('estudantes/exames/', ExamesAPIView.as_view(), name='exames-estudante'),
    path('estudantes/<int:estudante_id>/exames/<int:exame_id>/', ExameAPIView.as_view(), name='exames-estudante-detail'),
  #  path('avaliacoes/<int:estudante_id>/', AvaliacaoAPIView.as_view(), name='avaliacoes-list-by-estudante'),

    # Pagamento
    path('pagamentos/', PagamentosAPIView.as_view(), name='pagamentos-list-create'),
    path('pagamentos/<int:pk>/', PagamentoAPIView.as_view(), name='pagamento-detail'),
    path('estudantes/<int:estudante_id>/pagamentos/', PagamentosAPIView.as_view(), name='estudante-pagamentos'),
    path('estudantes/pagamentos/', PagamentosAPIView.as_view(), name='estudante-pagamentos'),
    path('estudantes/<int:estudante_id>/pagamentos/<int:pagamento_id>/', PagamentoAPIView.as_view(), name='pagamento-estudante-detail'),

    # Funcionario
    path('funcionarios/', FuncionariosAPIView.as_view(), name='funcionarios-list-create'),
    path('funcionarios/<int:pk>/', FuncionarioAPIView.as_view(), name='funcionario-detail'),

    # Acionista
    path('acionistas/', AcionistasAPIView.as_view(), name='acionistas-list-create'),
    path('acionistas/<int:pk>/', AcionistaAPIView.as_view(), name='acionista-detail'),

    # DocenteDisciplina
    path('docentesdisciplinas/', DocenteDisciplinasAPIView.as_view(), name='docentedisciplinas-list-create'),
    path('docentesdisciplinas/<int:pk>/', DocenteDisciplinaAPIView.as_view(), name='docentedisciplina-detail'),

    #estudantecurso
    path('estudantes-cursos/', EstudanteCursoListCreateAPIView.as_view(), name='estudantecurso-list-create'),
    path('estudantes-cursos/<int:pk>/', EstudanteCursoDetailAPIView.as_view(), name='estudantecurso-detail'),
]
