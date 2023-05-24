# class Pessoa:
#     def __init__(self, nome, sobrenome, idade):
#         self.nome = nome
#         self.sobrenome = sobrenome
#         self.idade = idade


#----------------------------------------------------------------------------
# p1 = Pessoa('Luiz', 'Otávio', 18)
# # p1.nome = 'Luiz'
# # p1.sobrenome = 'Otávio'

# p2 = Pessoa('Maria', 'Joana', 20)
# # p2.nome = 'Maria'
# # p2.sobrenome = 'Joana'

# print(p1.nome)
# print(p1.sobrenome)
# print(p1.idade)

# print(p2.nome)
# print(p2.sobrenome)

#----------------------------------------------------------------------------
# class Carro():
#     def __init__(self, marca, modelo, cor):
#         self.marca = marca
#         self.modelo = modelo
#         self.cor = cor
    
#     def acelerar(self):
#         print(f"{self.modelo} está acelerando...")


# c1 = Carro('Chevrolet', 'Corsa', 'Vermelho')
# c2 = Carro('Fiat', 'Siena', 'Branca')
# c3 = Carro('Hyundai', 'HB20', 'Branca')

# print(f'O carro da marca {c1.marca} e do modelo {c1.modelo} tem a cor {c1.cor}')
# c1.acelerar()
# print(f'O carro da marca {c2.marca} e do modelo {c2.modelo} tem a cor {c2.cor}')
# c2.acelerar()
# print(f'O carro da marca {c3.marca} e do modelo {c3.modelo} tem a cor {c3.cor}')
# c3.acelerar()
# print()


#----------------------------------------------------------------------------
# class Pessoa():
#     def __init__(self, nome, sobrenome):
#         self.nome = nome
#         self.sobrenome = sobrenome


# p1 = Pessoa("Gustavo","Nascimento")
# p2 = Pessoa("Elyan", "Sousa")

# print(f"A pessoa nomeada {p2.nome} {p2.sobrenome} tem o carro {c1.modelo}")
# print(f"A pessoa nomeada {p1.nome} {p1.sobrenome} tem o carro {c2.modelo}")

#----------------------------------------------------------------------------
# class Animal:
#     def __init__(self, nome):
#         self.nome = nome
    
#     def acao(self):
#         return(f'{self.nome} está executando uma ação')
    
#     def comendo(self, alimento):
#         return(f'{self.nome} está comendo {alimento}')
        
# leao = Animal('Leão')
# print(leao.nome)
# print(leao.acao())
# print(leao.comendo("Zebra"))

#----------------------------------------------------------------------------
# class Camera:
#     def __init__(self, nome, filmando=False):
#         self.nome = nome
#         self.filmando = filmando

#     def filmar(self):
#         if self.filmando is True:
#             print(f"{self.nome} JÁ está filmando...")
#             return
        
#         print(f"{self.nome} está filmando...")
#         self.filmando = True

#     def parar_filmar(self):
#         if not self.filmando is True:
#             print(f"{self.nome} não está filmando...")
#             return
        
#         print(f"{self.nome} está parando de filmar")
#         self.filmando = False
    
#     def fotografar(self):
#         if self.filmando is True:
#             print(f"{self.nome} não posso fotografar (Já está filmando)")
#             return
        
#         print(f'{self.nome} está fotografando')

# c1 = Camera('Canon')
# c2 = Camera('Sony')
# c1.filmar()
# c1.filmar()
# c1.fotografar()
# c1.parar_filmar()
# c1.fotografar()
# print()
# c2.parar_filmar()
# c2.filmar()
# c2.fotografar()
# c2.parar_filmar()
# c2.fotografar()


#----------------------------------------------------------------------------
# import datetime
# class Pessoa():
#     atributo = 'Valor_qualquer'
#     ano_atual = datetime.datetime.now().year
    
#     def __init__(self, nome,idade):
#         self.nome = nome
#         self.idade = idade
        
#     def get_ano_nascimento(self):
#         print (Pessoa.ano_atual- self.idade)
    

# p1 = Pessoa('João', 22)
# p2 = Pessoa('Helena', 12)

# Pessoa.get_ano_nascimento(p1)
# Pessoa.get_ano_nascimento(p2)

# print(p1.__dict__) # Ver o dicionario {'nome': 'João', 'idade': 22}, aqui não é apenas leitura como vars, posso mudar como p1.__dict__['outra'] = 'coisa'
# print(vars(p1)) # Vai te mostrar o dict também 

#----------------------------------------------------------------------------
#Métodos de classe + facotires (Fábricas)
#São métodos onde "self" será "cls", ou seja,
#ao invés de receber a instância no primeiro
#parâmetro, receberemos a própria classe.

# class Pessoa:
#     ano = 2023
    
#     def __init__(self, nome, idade):
#         self.nome = nome
#         self.idade = idade
   
#     @classmethod
#     def metodo_de_classe(cls):
#         print('Hey')
    
#     @classmethod
#     def criar_50_anos(cls, nome):
#         return cls(nome, 50)
    
#     @classmethod
#     def criar_sem_nome(cls, idade):
#         return cls('Anônima', idade)

# p1 = Pessoa('João', 32)
# print(Pessoa.ano) 

# p2 = Pessoa.criar_50_anos('Helena')
# print(p2.nome, p2.idade)
# print(p2.__dict__)

# p3 = Pessoa('Anônima', 23)
# print(p3.nome, p3.idade)

# p4 = Pessoa.criar_sem_nome(25)
# print(p4.nome, p4.idade)

#----------------------------------------------------------------------------

# method vs @classmethod vs @staticmethod
# method - self, método de instância
# @classmethod - cls, método de classe
# @staticmethod - método estático (❌self, ❌cls)
# class Connection:
#     def __init__(self, host='localhost'):
#         self.host = host
#         self.user = None
#         self.password = None

#     def set_user(self, user):
#         self.user = user

#     def set_password(self, password):
#         self.password = password

#     @classmethod
#     def create_with_auth(cls, user, password):
#         connection = cls()
#         connection.user = user
#         connection.password = password
#         return connection

#     @staticmethod
#     def log(msg):
#         print('LOG:', msg)


# def connection_log(msg):
#     print('LOG:', msg)


# # c1 = Connection()
# c1 = Connection.create_with_auth('luiz', '1234')
# # c1.set_user('luiz')
# # c1.set_password('123')
# print(Connection.log('Essa é a mensagem de log'))
# print(c1.user)
# print(c1.password)


#----------------------------------------------------------------------------

# @property - um getter no modo Pythônico
# getter - um método para obter um atributo
# cor -> get_cor()
# modo pythônico - modo do Python de fazer coisas
# @property é uma propriedade do objeto, ela
# é um método que se comporta como um
# atributo 🤯 🤯 🤯
# Geralmente é usada nas seguintes situações:
# - como getter
# - p/ evitar quebrar código cliente
# - p/ habilitar setter
# - p/ executar ações ao obter um atributo
# Código cliente - é o código que usa seu código
# class Caneta:
#     def __init__(self, cor):
#         self.cor_tinta = cor

#     @property
#     def cor(self):
#         print('PROPERTY')
#         return self.cor_tinta

#     @property
#     def cor_tampa(self):
#         return 123456

# ###########################


# caneta = Caneta('Azul')
# print(caneta.cor)
# print(caneta.cor)
# print(caneta.cor)
# print(caneta.cor)
# print(caneta.cor)
# print(caneta.cor)
# print(caneta.cor_tampa)

#####################################

# class Caneta:
#     def __init__(self, cor):
#         self.cor_tinta = cor

#     def get_cor(self):
#         print('GET COR')
#         return self.cor_tinta

# ###########################


# caneta = Caneta('Azul')
# print(caneta.get_cor())
# print(caneta.get_cor())
# print(caneta.get_cor())
# print(caneta.get_cor())
# print(caneta.get_cor())

#----------------------------------------------------------------------------

# @property + @setter - getter e setter no modo Pythônico
# - como getter
# - p/ evitar quebrar código cliente
# - p/ habilitar setter
# - p/ executar ações ao obter um atributo
# Atributos que começar com um ou dois underlines
# não devem ser usados fora da classe.


class Caneta:
    def __init__(self, cor):
        self.cor_tinta = cor

    @property
    def cor(self):
        print('PROPERTY')
        return self.cor_tinta

def mostrar(caneta):
    return caneta.cor

caneta = Caneta("Azul")
print(caneta.cor)