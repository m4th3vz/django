from django.db import models

class Todo(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    deadline = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

# models.py: Define os modelos (classes) que representam as tabelas do banco de dados.

# Cada classe herda de models.Model e representa uma entidade do sistema, como uma tarefa, usuário, etc.
# Os atributos da classe correspondem às colunas da tabela no banco, definindo o tipo de dado e regras.
# O Django usa esses modelos para criar, consultar, atualizar e deletar registros no banco de dados.
# Além disso, os modelos facilitam a manipulação dos dados de forma orientada a objetos dentro do código.
