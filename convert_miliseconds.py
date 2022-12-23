###  This program converts milliseconds into hours, minutes, and seconds ###
def time_count(mili_saniye):
    yazici = ""
    saat = saniye = dakika = 0
    if mili_saniye >= 3600000:
        saat = mili_saniye // 3600000
        mili_saniye = mili_saniye % 3600000
        yazici = str(saat) + " hour/s " 

    if mili_saniye >= 60000:
        dakika = mili_saniye // 60000
        mili_saniye = mili_saniye % 60000
        yazici = yazici + str(dakika) + " minute/s "

    if mili_saniye >= 1000: 
        saniye = mili_saniye // 1000
        yazici = yazici + str(saniye) + " second/s "
    
    # print(yazici)
    return yazici



while True:
   # Kullanıcıdan bir numara isteyin
    user_input = input("Please enter the milliseconds (should be greater than zero) : ")
    # Kullanıcı "exit" girerse programdan çıkar
    if user_input.lower() == "exit":
        print("Exiting the program... Good Bye")
        break
    # Kullanıcı girişi geçerli bir sayı değilse, bir hata mesajı gösterin ve tekrar giriş isteyin
    if not user_input.isdigit():
        print("Not Valid Input !!!")
        continue
    # Kullanıcı girişini bir tam sayıya dönüştürün
    
    # Sayı geçerli aralıkta değilse, bir hata mesajı gösterin ve tekrar giriş isteyin
    if int(user_input) < 1 :
        print("Not Valid Input !!!")
        continue
    if int(user_input) < 1000:
        print(f"just {user_input} miliseconds/s")
    else:    
        mili_saniye = int(user_input)
        print(time_count(mili_saniye))