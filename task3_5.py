
t = 10
for i in range(t):
    user_numbers = input('Enter numbers, to exit click letter: ').split()

    def s_func(u):
        try:
            sum(map(float, u))
        except ValueError:
            exit(sum(map(float, u[:-1])))
        return sum(map(float, u))
    print(s_func(user_numbers))

