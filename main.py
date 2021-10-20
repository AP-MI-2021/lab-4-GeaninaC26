def show_menu():
    print("1.Citire lista de float-uri")
    print("2.Afisarea partii intregi a tuturor numerelor din lista.")
    print("3.")
    print("4.")


def read_list_floats():
    floats_as_str=input("Dati o lista de float-uri separate prin spatiu.")
    floats_as_list_of_str=floats_as_str.split(' ')
    floats=[]
    for float_str in floats_as_list_of_str :
        floats.append(float(float_str))
    return floats


def get_integers(lst):
    """
    Determina partea intreaga a numerelor din  lista si returneaza o lista cu acestea.
    :param lst: lista de float-uri
    :return: lista formata din partile intregi ale numerelor in lista initiala
    """
    result = []
    for elem in  lst:
        result.append(int(elem))
    return result


def test_get_integers():
    assert get_integers([10.5, 12.3, 17.6]) == [10, 12, 17]
    assert get_integers([]) == []
    assert get_integers([10, 7, 3]) == [10, 7, 3]


def show_integers(lst):
    print(f'Lista cu partile intregi ale numerelor din lista {lst} este {get_integers(lst)}')



def main():
    lst = []
    while True:
        show_menu()
        option = input("Alegeti o optiune: ")
        if option == '1':
            lst = read_list_floats()
        elif option == '2':
            show_integers(lst)
        elif option == '3':
            pass
        elif option == '4':
            pass
        elif option == '5':
            pass
        elif option == 'x':
            break
        else:
            print("Optiune nevalida")


if __name__=='__main__':
    test_get_integers()
    main()