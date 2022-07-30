from rest_framework import viewsets
from mainApp.models import Aluno
from mainApp.serializer import AlunoSerializer

class AlunosViewSet(viewsets.ModelViewSet):
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer

