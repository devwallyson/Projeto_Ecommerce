from django.shortcuts import render, get_object_or_404, redirect
from .forms import CustomUserCreationForm
from .models import Produto, Carrinho, ItemCarrinho, Pedido,Endereco
from django.contrib.auth.decorators import login_required
from django.contrib import messages


@login_required
def minha_view_protegida(request):
    return render(request, 'loja/protegido.html')


def listar_produtos(request):
    produtos = Produto.objects.all()
    return render(request, 'loja/listar_produtos.html', {'produtos': produtos})


def registrar(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'loja/registrar.html', {'form': form})


@login_required
def adicionar_ao_carrinho(request, produto_id):
    produto = get_object_or_404(Produto, id=produto_id)
    quantidade_desejada = int(request.POST.get('quantidade', 1))
    
    
    if quantidade_desejada > produto.estoque:
        messages.error(request, f"Desculpe, só temos {produto.estoque} unidade(s) de {produto.nome} em estoque.")
        return redirect('detalhes_produto', produto_id=produto.id)
    
   
    carrinho, _ = Carrinho.objects.get_or_create(usuario=request.user)

    
    item_carrinho, criado = ItemCarrinho.objects.get_or_create(carrinho=carrinho, produto=produto)

    if criado:
        
        item_carrinho.quantidade = quantidade_desejada
    else:
       
        if item_carrinho.quantidade + quantidade_desejada > produto.estoque:
            messages.error(request, f"Você está tentando adicionar mais unidades do que temos em estoque.")
            return redirect('carrinho')
        item_carrinho.quantidade += quantidade_desejada

    item_carrinho.save()
    messages.success(request, f"{quantidade_desejada} unidade(s) de {produto.nome} adicionada(s) ao carrinho.")
    return redirect('ver_carrinho')

@login_required
def ver_carrinho(request):
    carrinho = Carrinho.objects.filter(usuario=request.user).first()
    if not carrinho:
        itens = []
        total = 0
    else:
        itens = ItemCarrinho.objects.filter(carrinho=carrinho)
        total = sum(item.get_total_preco() for item in itens)
    
    return render(request, 'loja/ver_carrinho.html', {'itens': itens, 'total': total})

@login_required
def remover_do_carrinho(request, item_id):
    item = get_object_or_404(ItemCarrinho, id=item_id)
    
    
    item.delete()
    
    messages.success(request, 'Produto removido do carrinho.')
    return redirect('ver_carrinho')


@login_required
def finalizar_compra(request):
    carrinho = Carrinho.objects.filter(usuario=request.user).first()
    
    
    if not carrinho:
        return redirect('ver_carrinho')
    
    itens = ItemCarrinho.objects.filter(carrinho=carrinho)
    total = sum(item.get_total_preco() for item in itens)

    if request.method == 'POST':
        
        pedido = Pedido.objects.create(usuario=request.user, total=total)
        for item in itens:
            pedido.produtos.add(item.produto)
        
        carrinho.delete()

        messages.success(request, 'Compra finalizada com sucesso.')
        return redirect('confirmacao_pedido', pedido_id=pedido.id)

    return render(request, 'loja/finalizar_compra.html', {'itens': itens, 'total': total})

@login_required
def atualizar_quantidade_carrinho(request, item_id):
    item = get_object_or_404(ItemCarrinho, id=item_id, carrinho__usuario=request.user)
    nova_quantidade = int(request.POST.get('quantidade'))
    if nova_quantidade > item.produto.estoque:
        messages.error(request, f"Desculpe, só temos {item.produto.estoque} unidade(s) de {item.produto.nome} em estoque.")
    elif nova_quantidade < 1:
        messages.error(request, "A quantidade mínima é 1.")
    else:
        item.quantidade = nova_quantidade
        item.save()
        messages.success(request, f"Quantidade de {item.produto.nome} atualizada para {nova_quantidade}.")

    return redirect('ver_carrinho')

def calcular_total_pedido(usuario):
    carrinho = Carrinho.objects.filter(usuario=usuario).first()
    if not carrinho:
        return 0
    itens = ItemCarrinho.objects.filter(carrinho=carrinho)
    total = sum(item.get_total_preco() for item in itens)
    return total

@login_required
def processar_pagamento(request):
    if request.method == 'POST':
        cidade = request.POST['cidade']
        cep = request.POST['cep']
        complemento = request.POST.get('complemento', '')
        numero = request.POST['numero']
        metodo_pagamento = request.POST['pagamento']

        if metodo_pagamento == 'cartao':
            numero_cartao = request.POST['numero_cartao']
            validade_cartao = request.POST['validade_cartao']
            cvv_cartao = request.POST['cvv_cartao']
        elif metodo_pagamento == 'pix':
            chave_pix = request.POST['chave_pix']

        endereco = Endereco.objects.create(
            usuario=request.user,
            cidade=cidade,
            cep=cep,
            complemento=complemento,
            numero=numero
        )

        pedido = Pedido.objects.create(usuario=request.user, total=calcular_total_pedido(request.user))
        pedido.endereco = endereco
        pedido.save()

        messages.success(request, 'Pagamento realizado com sucesso.')
        return redirect('pagamento_realizado', pedido_id=pedido.id)

    return render(request, 'loja/finalizar_pagamento.html')


@login_required
def confirmacao_pedido(request, pedido_id):
    pedido = get_object_or_404(Pedido, id=pedido_id, usuario=request.user)
    return render(request, 'loja/confirmacao_pedido.html', {'pedido': pedido})

@login_required
def pagamento_realizado(request, pedido_id):
    pedido = get_object_or_404(Pedido, id=pedido_id, usuario=request.user)
    return render(request, 'loja/pagamento_realizado.html', {'pedido': pedido})

