def listGeneratorUsingCycle (max_value : int) -> list:
    new_list = [] #Создание нового списка
    for new_list_element in range(max_value):
        new_list.add(new_list_element) #Заполнение списка новыми элементами
    return new_list