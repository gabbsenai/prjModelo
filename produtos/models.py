from django.db import models

#Esta definição de classe define um modelo Django chamado Categoria com um único campo nome (um campo de caractere com um comprimento máximo de 100 caracteres).
class Categoria(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

#Esta definição de classe define um modelo Django chamado Produto com quatro campos: nome, preco, categoria e imagem.
class Produto(models.Model):
    nome = models.CharField(max_length=100)
    preco = models.FloatField()
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    imagem = models.ImageField(upload_to='produtos/', null=True, blank=True)

    def __str__(self):
        return self.nome