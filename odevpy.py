# AD SOYAD: Abdurrahim Ağca 
# Numara: 213405520

from enum import Enum


class Winner(Enum):
    LEFT = 1
    RIGHT = 2
    TIE = 3


class Link:
    #init constractor
    #self refers object itself, this. 
    def __init__(self, strength, points):
        self.__strenght = strength
        self.__points = points

    @property
    def strength(self):
        return self.__strenght

    @property
    def points(self):
        return self.__points

    def __str__(self):
        return f"<S:{self.__strenght}, P:{self.__points}>"


class Chain:
    def __init__(self):
        self.__links = []

    def add_links(self, links):
        for link in links:
            self.__links.append(link)

    # değiştirilebilir alan başlangıcı

    def hang(self, link_index):
        """ 
        Zinciri kaçıncı halkadan askıya asacağınız 
        link_index ile veriliyor. 
        Asma işlemi yapılınca en zayıf halkalar kırılacaktır.
        Zayıf halkalar kırılınca self.__links güncellenmelidir. 
        """
        print(self.__links)
        print(Link.strength)
        self.__links
        
        
        pass

    def get_winner(self):
        """ 
        Kazanan tarafı bulan method.
        Bu method'dan hangi tipte bir sonuç dömesi gerektiğini
        anlamak için test case'leri inceleyiniz.
        """
        return None

    def __str__(self):
        """ 
        Zinciri test case'lerdeki gibi string'e 
        dönüştürmeniz gerekmektedir.
        """
        return " -> "

    # değiştirilebilir alan bitişi
  
    chain = Chain()
    links = [Link(5, 90), Link(7, 80), Link(4, 70),
    Link(4, 80), Link(9, 90), Link(4, 50)]
    chain.add_links(links)
    chain.hang(5)

    







   
    