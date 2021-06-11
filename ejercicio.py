def is_multiplo(n, m):
    if n%m == 0:
        return True
    return False


def is_multiplo_de_3(n):
    return is_multiplo(n, 3)

def is_multiplo_de_5(n):
    return is_multiplo(n, 5)

def decide_to_print(i):
    is_m_3 = is_multiplo_de_3(i)
    is_m_5 = is_multiplo_de_5(i)

    if is_m_3 == is_m_5:
        if is_m_3 == True:
            print('bizzfuzz')
        else:
            print(i)
    else:
        if is_m_3 == True:
            print('bizz')
        else:
            print('fuzz')
def main():
    for i in range(20):
        decide_to_print(i)
            
main()