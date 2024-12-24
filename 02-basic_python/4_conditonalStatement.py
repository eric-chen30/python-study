# 条件判断
def age_identity(age):
    s = input("Enter your age: ")
    # 需要对输入的字符串进行类型转换才能与整数进行比较
    age = int(s)
    if 0 < age < 18:
        print("You are a child.")
    elif 18 < age < 45:
        print("You are a teenager.")
    else:
        print("You ara an old man")


if __name__ == '__main__':
    age_identity(66)
