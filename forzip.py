i=["สวัสดีค่ะ","21",3]
u="67"
try:
 for i,u in zip(i,u):
    print("ค่าที่หนึ่งคึอ : ", i ,"\nค่าที่สองคือ : ", u )
except Exception as e:
    print(e)