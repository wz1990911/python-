str = input("请输入要反串的字符串")
def print_1(x):
    if x == -1 :
        return " "
    else:
        return str[x]+print_1(x-1)
a = print_1(len(str)-1)
print(a)
