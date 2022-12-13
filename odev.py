#!/usr/bin/env python
# coding: utf-8

# In[8]:


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
        print("----------------------")
        
        for link in range(len(self.__links)):
                print(self.__links[link])
        print("----------------------")
        if(link_index !=0 and link_index!=len(self.__links)):
      
            #finds weakest links' index for left
            print("first if executed")
            temp = 0
            i = 0
            while(i < link_index):
                if(self.__links[i].strength <= self.__links[temp].strength):
                    temp = i
                i += 1
                
            #print(self.__links[temp])
            
            #removes weakeast link and other links
            j = temp
            while(j > -1):
                self.__links[j] = None
                j = j - 1
            
            temp = link_index+1
            i = link_index+1
            while(i < len(self.__links)):
                if(self.__links[i].strength <= self.__links[temp].strength):
                    temp = i
                i +=1


            j = temp
            while(j < len(self.__links)):
                self.__links[j] = None
                j = j + 1
            updatedList = [i for i in self.__links if i != None]
            self.__links = updatedList
                
        elif(link_index == 0):
            print("first elif executed")
            temp = link_index+1
            i = link_index+1
            while(i < len(self.__links)):
               if(self.__links[i].strength <= self.__links[temp].strength):
                   temp = i
                   print(temp)
               i +=1

            print("weakest")
            print(self.__links[temp])
            j = temp
            while(j < len(self.__links)):
                self.__links[j] = None
                j = j + 1
            updatedList = [i for i in self.__links if i != None]
            self.__links = updatedList
            
        elif(link_index==len(self.__links)):
            print("sec elif executed")
            temp = 0
            i = 0
            while(i < link_index):
                if(self.__links[i].strength <= self.__links[temp].strength):
                    temp = i
                i += 1
                
            #print(self.__links[temp])
            
            #removes weakeast link and other links
            j = temp
            while(j > -1):
                self.__links[j] = None
                j = j - 1
            updatedList = [i for i in self.__links if i != None]
            self.__links = updatedList
            
        print("----------------------")

        for link2 in range(len(self.__links)):
              print("updated list")
              print(self.__links[link2])
            
        print("----------------------")



    
        

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


# In[9]:


test_results = []

# test case 1
print("case 1 ")
chain = Chain()
links = [Link(5, 90), Link(7, 80), Link(4, 70),
         Link(4, 80), Link(9, 90), Link(4, 50)]
chain.add_links(links)
test_results.append(str(chain) == "<S:5, P:90> -> <S:7, P:80> -> <S:4, P:70> -> <S:4, P:80> -> <S:9, P:90> -> <S:4, P:50>")
chain.hang(5)
test_results.append(str(chain) == "<S:9, P:90> -> <S:4, P:50>")
winner = chain.get_winner()
test_results.append(winner == Winner.LEFT)


# test case 2
print("case 2")
chain = Chain()
links = [Link(5, 90), Link(7, 80), Link(4, 70),
         Link(5, 80), Link(9, 90), Link(4, 50)]
chain.add_links(links)
test_results.append(str(chain) == "<S:5, P:90> -> <S:7, P:80> -> <S:4, P:70> -> <S:5, P:80> -> <S:9, P:90> -> <S:4, P:50>")
chain.hang(2)
test_results.append(str(chain) == "<S:7, P:80> -> <S:4, P:70> -> <S:5, P:80> -> <S:9, P:90>")
winner = chain.get_winner()
test_results.append(winner == Winner.RIGHT)

# test case 3
print("case 3")
chain = Chain()
links = [Link(3, 90), Link(3, 80), Link(4, 90), Link(5, 80),
         Link(4, 70), Link(4, 80), Link(5, 90), Link(3, 50)]
chain.add_links(links)
test_results.append(str(chain) == "<S:3, P:90> -> <S:3, P:80> -> <S:4, P:90> -> <S:5, P:80> -> <S:4, P:70> -> <S:4, P:80> -> <S:5, P:90> -> <S:3, P:50>")
chain.hang(4)
test_results.append(str(chain) == "<S:4, P:90> -> <S:5, P:80> -> <S:4, P:70> -> <S:4, P:80> -> <S:5, P:90>")
winner = chain.get_winner()
test_results.append(winner == Winner.TIE)

# test case 4
print("case 4")
chain = Chain()
links = [Link(3, 90), Link(5, 80), Link(4, 90), Link(5, 80),
         Link(4, 70), Link(4, 80), Link(3, 90), Link(9, 50)]
chain.add_links(links)
test_results.append(str(
    chain) == "<S:3, P:90> -> <S:5, P:80> -> <S:4, P:90> -> <S:5, P:80> -> <S:4, P:70> -> <S:4, P:80> -> <S:3, P:90> -> <S:9, P:50>")
chain.hang(0)
test_results.append(str(
    chain) == "<S:3, P:90> -> <S:5, P:80> -> <S:4, P:90> -> <S:5, P:80> -> <S:4, P:70> -> <S:4, P:80>")
winner = chain.get_winner()
test_results.append(winner == Winner.RIGHT)

# score
score = 100 * sum(test_results) / len(test_results)
print(f"Notunuz: {score}")

