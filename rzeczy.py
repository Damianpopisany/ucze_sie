
class Dupa1(object):

    def jeden(self):
        selector = input("Wpisz 1 lub 2\n")
        print(selector)
        if selector == 1:
            print("wpisales 1")
        else:
            print("wpisales 2")
        return selector

    def dwa(self, numer):
        print("To jest func dwa, w poprzedniej funkcji wpisales: {}".format(numer))


if __name__ == '__main__':
     # print(Dupa1().jeden())

    Dupa1().dwa(Dupa1().jeden())
