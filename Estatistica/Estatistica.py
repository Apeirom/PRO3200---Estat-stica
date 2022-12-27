## PRO3200 - Estatística (2022.2)

Tabela = [[15, 18, 17, 20 ,19],[19, 20, 16, 21, 19],[24, 27, 23, 20, 21]]
Tabela2 = [[24, 27, 23, 20, 21],[19, 20, 16, 21, 19],[15, 18, 17, 20 ,19]]
##Tabela3 = [[14,11,15,18,14,16,11,12,15,17,18,21],[12,10,15,11,11,14,11,12,14,15,16,17]]
##Tabela4 = [[80,72,65,78,85],[75,70,60,72,78]]
Tabela5 = [[8.5, 4.0, 5.0, 6.5, 7.0, 3.5, 9.0, 8.0, 7.5, 5.0],[8.0, 4.5, 6.0, 6.0, 7.0, 4.0, 8.5, 8.5, 7.0, 5.0]]
def X_barrado(fileira):
  n = len(fileira)
  soma = 0
  for i in fileira:
    soma += i
  return soma/n
def S_quadrado(fileira):
  n = len(fileira)
  media = X_barrado(fileira)
  soma = 0
  for i in range(n):
    soma += (fileira[i]-media)**2
  return soma/(n-1)
def CriaFileiraD(fileira1,fileira2):
  n = len(fileira1)
  fileiraD = []
  for i in range(n):
    fileiraD.append(fileira1[i]-fileira2[i])
def Xd_barrado(fileira1,fileira2):## fileira1>fileira2
  return X_barrado(fileira1)-X_barrado(fileira2)
def t_calc(fileira1,fileira2,valor_zero):
  n = len(fileira1)
  fileiraD = CriaFileiraD(fileira1,fileira2)
  xd = X_barrado()
  sd = S_quadrado()
  tcalc = (xd-valor_zero)/(sd/n)**(1/2)
  return tcalc
def Infos_tabela(Tabela):
  for i in range(len(Tabela)):
    for j in range(i+1,len(Tabela)):
      print("---infos de",i+1,"com",j+1,"---")
      print("Xd_barrado =",Xd_barrado(Tabela[i],Tabela[j]))
      print("Sd_quadrado =",Sd_quadrado(Tabela[i],Tabela[j]))
      print("t_calculado =",t_calc(Tabela[i],Tabela[j],0))
      print()
Infos_tabela(Tabela5)