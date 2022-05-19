Dic = {}

while True:
    key = int(input("숫자로 key를 입력하세요 > "))
    value = str(input("문자로 value를 입력하세요 > "))
    if (key == 0) or (value == "문자열 종료"):
        break
    else:
        Dic[key] = value

# 보기 좋게 한 줄 띄울게용
print()

print(list(Dic.keys()))
print(list(Dic.values()))
print(list(Dic.items()))