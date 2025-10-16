def remove_elements(input_list):
    indices_a_borrar = [5, 4, 0] 
    for indice in indices_a_borrar:
        if len(input_list) > indice:
            del input_list[indice]
    return input_list
def add_elements(input_list):
    input_list.insert(0, 'Pink')
    input_list.append('Yellow')
    return input_list
def is_empty(input_list):
    return not input_list 
def check_lists(list1, list2):
    if len(list1) < 3 or len(list2) < 3:
        return False
    return list1[2] == list2[2]
def list_of_lists(list_of_lists_input):
    if len(list_of_lists_input) < 3:
        return [] 
    list1_modificada = list_of_lists_input[0][:2]
    
    list2_modificada = list_of_lists_input[1][1:4]
    
    list3_modificada = list_of_lists_input[2][-2:]
    
    return [list1_modificada, list2_modificada, list3_modificada]
def ejecutar_tp6():
    print("Ejecución del Trabajo Práctico 6: Listas")
    print("\n1. Función remove_elements (Borra 1ro, 5to, 6to)")
    lista_original_1 = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
    lista_modificada_1 = remove_elements(lista_original_1.copy())
    print(f"   Lista original: {lista_original_1}")
    print(f"   Lista resultante: {lista_modificada_1}")
    print("\n2. Función add_elements (Añade 'Pink' al inicio y 'Yellow' al final)")
    lista_original_2 = ['Red', 'Green', 'White', 'Black']
    lista_modificada_2 = add_elements(lista_original_2.copy())
    print(f"   Lista original: {lista_original_2}")
    print(f"   Lista resultante: {lista_modificada_2}")
    print("\n3. Función is_empty (Verifica si está vacía)")
    print(f"   Lista [1, 2, 3]: {is_empty([1, 2, 3])}")
    print(f"   Lista [ ]: {is_empty([])}")
    print("\n4. Función check_lists (Compara el 3er elemento)")
    l4_a = ['Black', 'Pink', 'Yellow', 'Red', 'Green', 'White']
    l4_b = ['Red', 'Green', 'Yellow', 'White', 'Black', 'Pink']
    print(f"   'Yellow' vs 'Yellow': {check_lists(l4_a, l4_b)}") 
    l4_c = ['Black', 'Pink', 'Green', 'White']
    l4_d = ['Red', 'Green', 'Yellow', 'Black', 'Pink']
    print(f"   'Green' vs 'Yellow': {check_lists(l4_c, l4_d)}")
    l4_e = [1, 2]
    l4_f = [1, 2, 3]
    print(f"   Lista corta vs Lista larga: {check_lists(l4_e, l4_f)}") 
    print("\n5. Función list_of_lists (Modifica listas internas por slicing)")
    lista_de_listas_original = [[1, 2, 3], [4, 5, 6, 7, 8], [9, 10, 11, 12]]
    lista_de_listas_modificada = list_of_lists(lista_de_listas_original)
    print(f"   Original: {lista_de_listas_original}")
    print(f"   Resultado: {lista_de_listas_modificada}")
    print("Ejecución finalizada")
if name == "main":
    ejecutar_tp6()
