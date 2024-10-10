from django.db import models

# Create your models here.
class Produto (models.Model):
    nome = models.CharField(max_length=250)
    descricao = models.TextField()
    preco = models.DecimalField(max_digits=15, decimal_places=2)
    estoque = models.IntegerField()
    imagem = models.ImageField(upload_to='produtos/', blank=True, null=True)

    def __str__(self):
        return self.nome
    
class Carrinho (models.Model):
    usuario = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Carrinho de {self.usuario}'   

class Endereco(models.Model):
    usuario = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    cidade = models.CharField(max_length=100)
    cep = models.CharField(max_length=9)
    complemento = models.CharField(max_length=100, blank=True, null=True)
    numero = models.CharField(max_length=10)

    def __str__(self):
        return f'{self.cidade}, {self.cep}'     
    
class Pedido(models.Model):
    usuario = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    produtos = models.ManyToManyField(Produto)
    total = models.DecimalField(max_digits=15, decimal_places=2)   
    criado_em = models.DateTimeField(auto_now_add=True)
    endereco = models.ForeignKey(Endereco,on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f'Pedido {self.id} - {self.usuario} '
    
class ItemCarrinho(models.Model):
    carrinho = models.ForeignKey(Carrinho, on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f'{self.quantidade}x {self.produto.nome}'
    
    def get_total_preco(self):
        return self.quantidade * self.produto.preco  
    
    
  
