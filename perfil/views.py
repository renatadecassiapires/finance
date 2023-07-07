from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Conta, Categoria
from django.contrib import messages
from django.contrib.messages import constants
from django.db.models import Sum #para aqueles q estão um pouco mais avançados em django (seria para diminuir linhas e deixar código mais limpo)

# Create your views here.
def home(request):
    contas = Conta.objects.all()

    total_contas = 0  
    for conta in contas:
        total_contas += conta.valor

    return render(request, 'home.html', { 'contas' : contas, 'total_contas': total_contas })


def gerenciar(request): # função que renderiza nossa interface (tudo o q eu quero q apareça na tela do front)
    contas = Conta.objects.all()
    categorias = Categoria.objects.all()

    # total_contas = contas.aggregate(Sum('valor'))['valor__sum'] # ultizado para substituir linhas abaixo (15 ao 17)
    total_contas = 0
    for conta in contas:
        total_contas += conta.valor

    return render(request, 'gerenciar.html', {'contas': contas, 'total_contas': total_contas, 'categorias' : categorias})

def cadastrar_banco(request):
    apelido = request.POST.get('apelido')
    banco = request.POST.get('banco')
    tipo = request.POST.get('tipo')
    valor = request.POST.get('valor')
    icone = request.FILES.get('icone')

    if len(apelido.strip()) == 0 or len(valor.strip()) == 0: # código para mostrar msg de erro caso apelido ou valor sejam iguais a zero ou iguais a espaços vazios
        messages.add_message(request, constants.ERROR, 'Favor preencher todos os campos')
        return redirect('/perfil/gerenciar/')

    conta = Conta(
        apelido = apelido, 
        banco = banco, 
        tipo = tipo, 
        valor = valor, 
        icone = icone
    )
    conta.save()

    messages.add_message(request, constants.SUCCESS, 'Parabéns, conta cadastrada com sucesso')
    return redirect('/perfil/gerenciar/')

def deletar_banco(request, id):
    conta = Conta.objects.get(id = id)
    conta.delete()

    messages.add_message(request, constants.SUCCESS, 'Parabéns, conta deletada com sucesso')
    return redirect('/perfil/gerenciar/')

def cadastrar_categoria(request):
    nome = request.POST.get('categoria')
    essencial = bool(request.POST.get('essencial'))

    categoria = Categoria(
        categoria = nome,
        essencial = essencial
    )

    categoria.save()

    messages.add_message(request, constants.SUCCESS, 'Parabéns, Categoria cadastrada com sucesso')
    return redirect('/perfil/gerenciar/')

def update_categoria(request, id): 
    categoria = Categoria.objects.get(id = id)
    categoria.essencial = not categoria.essencial
    categoria.save()

    return redirect('/perfil/gerenciar/')
