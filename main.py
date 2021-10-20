def show_menu():
    print("1.Citire lista de float-uri")
    print("2.Afisarea partii intregi a tuturor numerelor din lista.")
    print("3.Afisarea numerelor din lista ce apartin unui interval dat de utilizator")
    print("4.Afișarea tuturor numerelor a căror parte întreagă este divizor al părții fracționare")


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


def get_num_in_interval(lst, start, end):
    """
    Afiseaza toate numerele care apartin unui interval citit de la tastatura
    :param lst: lista de float-uri, pe care se va testa proprietatea
    :param start:capatul de inceput al intervalului, dat de utilizator
    :param end:capatul de final al intervalului, dat de utilizator
    :return: o lista cu numerele in lst ce se afla in interval
    """
    result = []
    for elem in lst:
        if start < elem < end:
            result.append(elem)
    return result


def test_get_num_in_interval():
    assert get_num_in_interval([12.3, 7.5, 4.3, 8.9], 3, 8) == [7.5, 4.3]


def show_num_in_intervals(lst):
    start = float(input("Dati capatul de inceput al intervalului: "))
    end = float(input("Dati capatul final al intervalului: "))
    print(f'Numeele din {lst} ce se afla in intervalul [{start}, {end}] sunt : {get_num_in_interval(lst, start, end)}')


def get_integers_div_frac(lst):
    """
    Determina numerele din lista care au partea intreaga divizor a partii fractionare
    :param lst: lista de floaturi
    :return: lista ce contine numerele cu proprietatea ceruta
    """
    result = []
    for elem in lst:
        str_elem=str(elem)
        if '.' in str_elem:
            integer = int(str_elem.split('.')[0])
            decimals = int(str_elem.split('.')[1])
            if integer != 0 and decimals > 0:
                if decimals % integer == 0:
                    result.append(elem)
    return result


def test_integers_div_frac():
    assert get_integers_div_frac([1.5, -3.3, 8, 9.8, 3.2]) == [1.5, -3.3]
    assert get_integers_div_frac([]) == []
    assert get_integers_div_frac([1.5, -3.3, 2.4]) == [1.5, -3.3, 2.4]


def show_integers_div_frac(lst):
    print(f'Numerele din {lst} a caror parte intreaga divide partea fractionara sunt {get_integers_div_frac(lst)}')


def split(elem):
    return list(elem)

def get_word(elem):

    str_elem=str(elem)
    caracter=split(str_elem)
    result = caracter[0]
    for i in range(1,len(caracter)):
        if caracter[i] == '1':
            result = result + 'unu'
        if caracter[i] == '2':
            result = result = 'doi'
        if caracter[i] == '3':
            result = result = 'trei'
        if caracter[i] == '4':
            result = result = 'patru'
        if caracter[i] == '5':
            result = result = 'cinci'
        if caracter[i] == '6':
            result = result = 'sase'
        if caracter[i] == '7':
            result = result = 'sapte'
        if caracter[i] == '8':
            result = result = 'opt'
        if caracter[i] == '9':
            result = result = 'noua'
        if caracter[i] == '0':
            result = result = 'zero'
        if caracter[i] == '.':
            result = result = 'virgula'
        if caracter[i] == '-':
            result = result + 'minus'
        print(result)

    return result


def get_floats_into_words(lst):
    """
    Afișam listei obținute din lista inițială în care numerele sunt înlocuite cu un string format din
    cuvinte care le descriu caracter cu caracter.
    :param lst: lista de float-uri
    :return: lista de string-uri, in care fiecare element descrie elementul de pe aceeasi pozitie din lst
    """
    result =[]
    for elem in lst:
        str_elem=str(elem)
        cuvant = get_word(str_elem)
        result.append(cuvant)
    return result


def show_floats_into_words(lst):
    print(f'Lista: {get_floats_into_words(lst)}')



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
            show_num_in_intervals(lst)
        elif option == '4':
            show_integers_div_frac(lst)
        elif option == '5':
            show_floats_into_words(lst)
        elif option == 'x':
            break
        else:
            print("Optiune nevalida")


if __name__=='__main__':
    test_get_integers()
    test_get_num_in_interval()
    test_integers_div_frac()
    main()