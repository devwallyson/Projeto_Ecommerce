from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('produtos/', views.listar_produtos, name='listar_produtos'),
    path('login/', auth_views.LoginView.as_view(template_name='loja/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('registrar/', views.registrar, name='registrar'),
    path('carrinho/', views.ver_carrinho, name='ver_carrinho'),
    path('adicionar_ao_carrinho/<int:produto_id>/', views.adicionar_ao_carrinho, name='adicionar_ao_carrinho'),
    path('carrinho/remover/<int:item_id>/', views.remover_do_carrinho, name='remover_do_carrinho'),
    path('finalizar/', views.finalizar_compra, name='finalizar_compra'),
    path('confirmacao/<int:pedido_id>/', views.confirmacao_pedido, name='confirmacao_pedido'),
    path('atualizar-quantidade/<int:item_id>/', views.atualizar_quantidade_carrinho, name='atualizar_quantidade_carrinho'),
    path('processar_pagamento/', views.processar_pagamento, name='processar_pagamento'),
    path('pagamento_realizado/<int:pedido_id>/',views.pagamento_realizado, name='pagamento_realizado'),
    


    
]
