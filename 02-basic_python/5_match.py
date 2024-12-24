# 模糊匹配
scoreOne = 'A'


# match 和 case 是 Python 3.10 及以后版本中引入的结构模式匹配的关键字。
def match_grade(score):
    match score:
        case 'A':
            print("You are perfect")
        case 'B':
            print("You are a good")
        case 'C':
            print("You Need to work hard")
        case _:
            print("Sorry you are not good")


if __name__ == '__main__':
    match_grade(scoreOne)
