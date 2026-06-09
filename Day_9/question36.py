def print_hollo_square(n):
    for i in range(n):
        if i == 0 or i == n-1:
            print('*' * n)
        else:
            print('*' + ' ' * (n-2) + '*')

# Example usage
size = 5
print_hollo_square(size)
