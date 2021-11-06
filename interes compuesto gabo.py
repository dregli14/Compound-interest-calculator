#!/usr/bin/env python
# coding: utf-8

# In[63]:


print('ingresar el monto a invertir:')
invi=input( )
print('Ingresar interes anual:')
inta = input()
invi=int(invi)
inta=float(inta)
intacor= inta/100
intm= intacor/12
ganm= invi * intm
reta=invi * intacor
rett=reta+invi
retm=(rett/12)
print('Inversion inicial: $', invi)
print('Interes anual:', '%',inta) 
print('Interes mensual:  %', intm)
print('Ganancia mensual:','$',ganm)
print('Retorno anual: $',reta)
print('Retorno total: $', rett)
print('retorno mensual: $', retm)


# In[64]:


#Esta funcion devuelve la ganancia acumulativa de la inversion, si las ganancias generadas en cada mes
#vuelven a ser reinvertidas
inv=invi
for compl in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11,12]:
    gan=inv*intm
    inv= inv+gan
    
    
    
    print(inv)
    


# In[65]:


#Esta funcion devuelve la ganancia neta de cada mes si las ganancias mensuales vuelven a ser invertidas
inv=invi
for compl in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11,12]:
    gan=inv*intm
    inv=gan+inv
  
   
    
    
    print('$',gan)


# In[ ]:




