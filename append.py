try:
    Is =[]
    count = 0 
    max = 0
    n1 = int(input("นี่คือส่วนของ n1 : "))
    while True:
        n2 = int(input("นี่คือส่วนของ n2 : "))
        if n2 == n1:
                count += 1
        else:
                Is.append(count)
                count = 0
        if n2 == 0:
            break
    print(Is)
except Exception as e:
    print(e)