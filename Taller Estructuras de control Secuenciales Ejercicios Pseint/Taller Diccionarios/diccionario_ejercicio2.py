diccionario={'Mikel': 3, 'Ane': 8, 'Amaia': 12, 'Unai': 5, 'Jon': 8, 'Ainhoa': 7,'Maite': 5}
lista=[]
for key in diccionario.values():
    if lista.count(key) == 0:
        lista.append (key)
print (lista)

