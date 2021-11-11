#!/usr/bin/env python
# coding: utf-8

# In[34]:


print('ingresar el monto a invertir:')
invi=input( )
print('Ingresar interes anual:')
inta = input()
print('Mes en el que comienza (valor numerico)')
mes=input()
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


# In[73]:


#Esta funcion devuelve la ganancia acumulativa de la inversion, si las ganancias generadas en cada mes
#vuelven a ser reinvertidas
inv=invi
for m in Months:
    gan=inv*intm
    inv= inv+gan
    print(m, '$',inv)
    if m == 'December':
        months=calendar.month_name[1:mes]
        for m in months:
            print(m, '$',inv)
    
    
    
    


# In[68]:


import calendar

Months=calendar.month_name[mes:mes+12] 
for m in Months:
    print(m)
    if m == 'December':
        months=calendar.month_name[1:mes]
        for m in months:
            print(m)
   
        
    
  


# In[51]:


mes=int(mes)
type(mes)


# In[76]:


#Esta funcion devuelve la ganancia neta de cada mes si las ganancias mensuales vuelven a ser invertidas
inv=invi
for m in Months:
    gan=inv*intm
    inv=gan+inv
    print(m, '$',gan)
    if m == 'December':
        months=calendar.month_name[1:mes]
        for m in months:
            print(m, '$',gan)
   
    
    


# In[ ]:




