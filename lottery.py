while True:
    try:
        try:
            class check:
                def __init__(self,_number):
                    self._number = _number
                    print("หมายเลขฉลากของคุณ = {} ".format(self._number))
                    if not len(self._number) == 6:
                            print("\nฉลากของคุณต้องเป็นเลขฉลากจำนวน 6 หลัก")   
                    elif float(self._number) < 0:
                            print("\nฉลากของคุณต้องไม่เป็นค่าติดลบ")
                    elif not float(self._number) % 2 == 0:
                            print("\nฉลากของคุณต้องไม่เป็นค่าทศนิยม")
                def ch(self,_numm,_nun):
                    self._numm = _numm
                    self._nun = _nun
                    if self._number == str(self._numm):
                        print("\n**ถูกหวยรางวัลที่ {} **".format(self._nun))
                def ch11(self,_numm,_nunn,_T,_nun):
                    self._numm = _numm
                    self._nunn = _nunn
                    self._T = _T
                    self._nun = _nun
                    if self._number[0:3] == str(self._numm) or self._number[0:3] == str(self._nunn):
                        print("\n**รางวัลเลข{} {} ตัว**".format(self._T,self._nun))
                def ch12(self,_numm,_nunn,_T,_nun,TU):
                    self._numm = _numm
                    self._nunn = _nunn
                    self._T = _T
                    self._nun = _nun
                    self.TU = TU
                    if self._number[TU:] == str(self._numm) or self._number[TU:] == str(self._nunn):
                        print("\n**รางวัลเลข{} {} ตัว**".format(self._T,self._nun))
                def ch2(self,_numm,_nunn,_numn,_nunm,_nuu,_nun):
                    self._numm = _numm
                    self._nun = _nun
                    self._nunn = _nunn
                    self._numn = _numn
                    self._nunm = _nunm
                    self._nuu = _nuu
                    if self._number == str(self._numm) or self._number == str(self._nunn) or self._number == str(self._nuu):
                        print("\n**ถูกหวยรางวัลที่ {} **".format(self._nun))
                    elif self._number == str(self._numn) or self._number == str(self._nunm):
                        print("\n**ถูกหวยรางวัลที่ {} **".format(self._nun))
        except Exception :
            print("คุณกรอกฉลากไม่ถูกรูปแบบ")
        while True:
            num = check(str(input("\nหมายเลขฉลากหวยของคุณ : ")))
            num.ch11(287,242,"หน้า",3)
            num.ch12("002","542","ท้าย",3,-3)
            num.ch12("61","\n","ท้าย",2,-2)
            num.ch(981416,"ข้างเคียงรางวัลที่ 1")
            num.ch(981418,"ข้างเคียงรางวัลที่ 1")
            num.ch2(953174,196793,587134,201415,592830,2)
            num.ch2(777700,624057,332670,"008704",985514,3)
            num.ch2(354561,346509,701139,638824,860770,3)
            num.ch2(867974,395006,803203,116559,825525,4)
            num.ch2(171591,963290,795664,855217,731205,4)
            num.ch2(252857,905860,478821,"012535",548865,4)
            num.ch2(794810,464099,246140,949846,410184,4)
            num.ch2("013517",708562,628271,152661,339148,4)
            num.ch2("002701","007539",491727,350616,611906,4)
            num.ch2(726094,931713,327473,888563,886960,4)
            num.ch2(120820,748250,416569,481946,636432,4)
            num.ch2(956707,602393,"060636",559608,777676,4)
            num.ch2(244470,283860,868907,552378,840523,4)
            num.ch2(912063,142145,747563,360338,884582,5)
            num.ch2(527466,"098876",171253,168907,543477,5)
            num.ch2(160865,280734,486681,"098495",627407,5)
            num.ch2(188226,848784,375625,422488,192477,5)
            num.ch2(473396,"003072",304576,863042,207379,5)
            num.ch2(768400,997060,738293,567804,722926,5)
            num.ch2(398073,328893,"002433",844248,132324,5)
            num.ch2(766895,723926,714614,312844,358291,5)
            num.ch2(876791,702997,686989,473249,280005,5)
            num.ch2(789132,384652,131974,"06155",237844,5)
            num.ch2(805934,646477,249532,306316,474436,5)
            num.ch2(888002,371922,385954,540246,520471,5)
            num.ch2(106354,527947,151776,770454,"022023",5)
            num.ch2(825582,547390,457479,388003,202443,5)
            num.ch2("011425","079349","047039",587094,119518,5)
            num.ch2(564284,465815,830802,911519,337800,5) 
            num.ch2(536321,515982,947713,"023497",358481,5)
            num.ch2(409444,"011246",993451,"066480","041524",5)
            num.ch2(825074,228818,398098,242223,770868,5)
            num.ch2(548002,338442,161995,242890,796509,5)
            y=(input("\nคุณต้องการจะรันโปรแกรมต่อหรือไม่(y/n) : ")).lower()
            if not y == "y":
                if not y == "yes":
                    if not y == "n":
                        if not y == "no" :
                            print("\n\n**กรุณาเลือก y /yes / n /no เท่านั้น**\n\n")
                            while True:
                                y=(input("\nคุณต้องการจะรันโปรแกรมต่อหรือไม่(y/n) : ")).lower()
                                if y == "y" or y == "n" or y == "yes" or y == "no" :
                                    break
            if y == "no" or y == "n" :
                break
    except Exception as e:
        print("คุณต้องกรอกฉลากเป็นตัวเลขเท่านั้น")
    if y == "n" or y == "no":
        break
print("\n\n\t** จบโปรแกรม **\n\n")