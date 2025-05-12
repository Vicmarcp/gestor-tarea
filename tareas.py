def agregar_tarea(lista, tarea):
    lista.append(tarea)
    return lista

def listar_tareas(lista):
    for i, t in enumerate(lista, 1):
        print(f"{i}. {t}")

def eliminar_tarea(lista, indice):
    if 1 <= indice <= len(lista):
        lista.pop(indice-1)
        return lista
    else:
        print("Índice inválido.")
        return lista
