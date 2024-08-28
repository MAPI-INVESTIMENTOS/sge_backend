from django.contrib import admin
from .models import (Docente,Estudante, Curso, SemestreLectivo, Disciplina,DiretorCurso,EstudanteDisciplina,
                    Acionista, Funcionario,DocenteDisciplina,Avaliacao,Pagamento,Exames,EstudanteCurso)

admin.site.register(Curso)
admin.site.register(Disciplina)
admin.site.register(Docente)
admin.site.register(SemestreLectivo)
admin.site.register(Funcionario)
admin.site.register(Acionista)
admin.site.register(Estudante)
admin.site.register(DocenteDisciplina)
admin.site.register(DiretorCurso)
admin.site.register(EstudanteDisciplina)
admin.site.register(Avaliacao)
admin.site.register(Exames)
admin.site.register(Pagamento)
admin.site.register(EstudanteCurso)
