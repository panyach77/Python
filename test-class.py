try:
    class one:
        def __init__(self,N1,N2):
            self.N1 = N1
            self.N2 = N2
            print("นี่คือค่าของ {} {} ".format(self.N1,self.N2))
    class check:
        def __init__(self,_number):
            self._number = _number
            print("หมายเลขฉลากของคุณ = {} ".format(self._number))
    sa = one("5",6)
    da = check(5)
except Exception as e:
    print(e)