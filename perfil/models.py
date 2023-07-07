from django.db import models

# Create your models here.

class Categoria(models.Model): # utilizado para criar minha primeira tabela chamada perfil_categoria
    categoria = models.CharField(max_length = 50)
    essencial = models.BooleanField(default = False)
    valor_planejamento = models.FloatField(default = 0) # linhas 6,7,8 são os campos da minha tabela

    def __str__(self):
        return self.categoria
    


class Conta(models.Model): # utilizado para criar minha segunda tabela chamada perfil_conta
    banco_choices = (
        ('NU', 'Nubank'),
        ('CE', 'Caixa Ecônomica'),
        ('BB', 'Banco do Brasil'),
    )

    tipo_choices = (
        ('PF', 'Pessoa Física'), 
        ('PJ', 'Pessoa Jurídica')
    )

    apelido = models.CharField(max_length = 50)
    banco = models.CharField(max_length = 2, choices = banco_choices)
    tipo = models.CharField(max_length = 2, choices = tipo_choices)
    valor = models.FloatField()
    icone = models.ImageField(upload_to = 'icones')


def __str__(self):
    return self.apelido



