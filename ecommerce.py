# TODO: Vamos implementar uma simulação para vendas de um sistema de e-commerce
class Cliente:
    def __init__(self, nome):
        self._nome = nome

    @property
    def nome(self):
        return self._nome


class Produto:
    def __init__(self, descricao, preco):
        self._descricao = descricao
        self._preco = preco

    @property
    def preco(self):
        return self._preco

    @property
    def descricao(self):
        return self._descricao


class Item:
    def __init__(self, produto, quantidade):
        self._produto = produto
        self._quantidade = quantidade

    @property
    def produto(self):
        return self._produto

    @property
    def quantidade(self):
        return self._quantidade

    @property
    def sub_total(self):
        return self._produto.preco * self._quantidade


class Pedido:
    def __init__(self, cliente):
        self._cliente = cliente
        self._carrinho = []

    def adicionar_item(self, item):
        self._carrinho.append(item)

    def calcular_preco(self):
        valor = 0
        for item in self._carrinho:
            valor += item.sub_total
        return valor

    def imprimir_pedido(self):
        print(f"Cliente : {self._cliente.nome}")
        for item in self._carrinho:
            print(
                f"Item: {item.produto.descricao}, Quantidade: {item.quantidade}, Preço Unitario: R${item.produto.preco}, Sub Total: R${item.sub_total}")


class Pagamento:
    def __init__(self, pix, cartao):
        self._pix = pix
        self._cartao = cartao


fogao = Produto('Fogão 8 bocas', 2500)
televisao = Produto('Televisao 32 polegadas', 1800)
notebook = Produto('Notebook', 3000)

joao = Cliente("João")

item1 = Item(fogao, 10)
item2 = Item(televisao, 5)
item3 = Item(notebook, 9)

pedido = Pedido(joao)
pedido.adicionar_item(item1)
pedido.adicionar_item(item2)
pedido.adicionar_item(item3)

total = pedido.calcular_preco()
imprimir = pedido.imprimir_pedido()
print(f"Total: R${total}")



