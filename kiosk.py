drinks =["아아","라떼","아샷추"]
price = [1500,2000,2500]
sum = 0



while 1:
    menu = int(input("1)아아 2) 라떼 3) 아샷추 4) 주문종료: "))
    if menu == 1:
        print(f"아아 주문 가격은 {price[0]}원")
        sum += [price[0]]
    elif menu == 2:
        print(f"라떼 주문 가격은 {price[1]}원")
        sum += [price[1]]
    elif menu == 3:
        print(f"아샷추 주문 가격은 {price[2]}원")
        sum += [price[2]]
    else:
        print("주문을 종료 합니다")
        break

print(f"총 주문 가격은{sum}입니다")

