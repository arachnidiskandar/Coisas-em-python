'''Create an application which manages an inventory of products. Create a product class which has a price, id, and quantity on hand. Then create an inventory class which keeps track of various products and can sum up the inventory value.'''
class Inventory:
    def __init__(self):
        self.productlist = []

    def addOrdelete(self,produto,add):
        if add is True:
            self.productlist.append(produto)
        else:
            self.productlist.remove(produto)

    #def searchItem(self,id):


    def showAll(self):
        value = 0
        for product in self.productlist:
            print("ID product: {}\n" \
                    "Price: {}\n" \
                    "Quantity: {}\n".format(product.ID,
                                            product.price,
                                            product.qntd))
            value += (product.price * product.qntd)
        print ("Valor total em estoque:", value)

class Item(object):
   #constructor
    def __init__(self, idProduct, priceProduct, quanityProduct):
        self._ID= idProduct
        self._price = priceProduct
        self._quantity = quanityProduct

    #getters
    @property
    def price(self):
        return self._price

    @property
    def ID(self):
        return self._ID

    @property
    def qntd(self):
        return self._quantity

    #setters
    @price.setter
    def price(self, newPrice):
        if newPrice > 0:
            self._price = newPrice
        else:
            print("The price cant be lower or equal than zero.")

    @qntd.setter
    def qntd(self, valor_operação):
        valor, operação = valor_operação
        if operação is True:
            self._quantity += valor
        else:
            if valor > self._quantity:
                self._quantity = 0
            else:
                self._quantity -= valor

    def __str__(self):
        return      "ID product: {}\n" \
                    "Price: {}\n"\
                    "Quantity: {}\n".format(self._ID, self._price, self._quantity)

def alterarItem(itens):
    my_itens = itens
    while True:
        try:
            id = int(input("Insira o ID do item que deseja alterar.\t\t0-Retornar\n"))
            if id == 0:
                break
            else:
                if id in list(my_itens.keys()):  # Verifica se está nos itens adicionados.
                    alteração = int(input("1-Alterar preço.\t2-Alterar a qntd.\n"))
                    if alteração is 1:
                        try:
                            novo_preço = float(input("Insira o novo preço.\n"))
                            my_itens[id].price = novo_preço
                            print("Produto alterado.\n", my_itens[id])
                            return my_itens
                            break
                        except ValueError:
                            print("Preço inválido.\n")
                    elif alteração is 2:
                        try:
                            qntd = int(input("Insira a nova qntd.\n"))
                            try:
                                op = int(input('1-Adicionar 2- Remover.'))
                                if op is 1:
                                    op = True
                                elif op is 2:
                                    op = False
                                else:
                                    print('Opção inválida.')
                            except ValueError:
                                print("Opção inválida.")
                            valor = qntd,op
                            my_itens[id].qntd = valor
                            print("Produto alterado.\n", my_itens[id])
                            return my_itens
                            break
                        except ValueError:
                            print("Qntd. inválida.\n")
                    else:
                        print('Operação inválida.\n')
                else:
                    print("Item não encontrado.\n")
        except ValueError:
            print("ID inválido.\n")

def main():
    storage = Inventory()
    my_itens = {}
    while True:     #loop programa.
        try:
            main_menu = int(input("1-Gerenciar estoque.\t2-Fechar Programa.\n"))
            if main_menu is 1:
                while True:     #loop inventário.
                    try:
                        invetory_menu = int(input("1-Adicionar um novo item\t2-Remover um item.\n\n"
                                                "3-Alterar um item.\t4-Mostrar Todos os itens.\n\n"
                                                "5-Retornar.\n"))
                        if invetory_menu is 1:
                            id, preço, qntd = (input("Insira o ID, o preço e a qntd.(Separados por ',')\n").split(','))
                            id,preço,qntd = int(id), float(preço), int(qntd)
                            my_itens[id] = Item(id, preço, qntd)
                            storage.addOrdelete(my_itens[id],True)
                        elif invetory_menu is 2:
                            remover_id = int(input("Insira o ID do item q deseja remover:\n"))
                            storage.addOrdelete(my_itens[remover_id], False)
                            my_itens.pop('id', None)
                        elif invetory_menu is 3:
                            my_itens = alterarItem(my_itens)
                        elif invetory_menu is 4:
                            storage.showAll()
                        elif invetory_menu is 5:
                            break
                        else:
                            print("Opção inválida. Digite novamente.\n")

                    except ValueError:
                        print("Opção inválida. Digite novamente.\n")
            elif main_menu is 2:
                break
            else:
                print("Opção inválida. Digite novamente.\n")
        except ValueError:
            print("Opção inválida. Digite novamente.\n")
if __name__ == '__main__':
    main()
