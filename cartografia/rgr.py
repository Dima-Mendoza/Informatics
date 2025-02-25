def one_one_two():
    a,b,c,i,n = 0

    for i in range(1,20):
        if (a + b == 2 * c):
            n += 1

def one_two_tree():
    n[10] = {0}
    min = 0;
    for i in range(len(n)):
        if abs(n[i]) <= min:
            n[i] = 0


def one_tree_four():
    n[20] = {0}
    sum = 0
    try:
        user_inp1 = int(input("Enter a first number: "))
        user_inp2 = int(input("Enter a second number: "))
        for i in range(user_inp1, user_inp2):
            sum += n[i]

    except e as err:
        print(err)


