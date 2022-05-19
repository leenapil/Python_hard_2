List = []

# 첫 번째 반복문
for a in range(1,16):
    a = int(input("1부터 15까지 중에서 정수를 입력해주세요 > "))
    if a == 0 or a > 15:
        print(" -- 정수 범위에 맞게 다시 입력해주세요 -- ")
    while True:
        if 0 < a < 16:
            List.append(a)
        break
print(List)

# 두 번째 반복문
for a in List[:]:
    if a % 2 == 0:
        List.remove(a)
print("2의 배수를 삭제합니다")
print(List)

# 세 번째 반복문
for a in List[:]:
    if a % 3 == 0:
        List.remove(a)
print("3의 배수를 삭제합니다")
print(List)

# 보기 좋게 한 줄 띄울게용
print()

# 마지막 조건
List.pop(0)
print('숫자 "1" 제거:', List)

List.insert(0,2)
List.insert(1,3)
print('숫자 "2,3" 삽입:', List)

List.sort()
print("최종 소수 리스트:", List)