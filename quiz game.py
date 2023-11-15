print ("Welcome to my HRKLD quizzes :) " )

playing = input("Do you want to play?")

if playing.lower() != "yes":
    quit()

print("Okay! Let's play :) ")
score = 0

print('Please use the below names to type in the correct answers! ')

print(' Thai Bao, Khanh Ly, Tuong Vy, Lan Anh, Thang Lol, Ti Be, Quan' )

answer = input("Ai dam nhat? ")
if answer.lower() == "ti be":
    print('chinh xac!')
    score += 1
else:
    print("Incorrect!")

answer = input("Ai la nguoi mien nam gia? ")
if answer.lower() == "khanh ly":
    print('ban qua tham doc!')
    score += 1
else:
    print("Incorrect!")


answer = input("Ai ngu nhat? ")
if answer.lower() == "thang lol":
    print('vi no xung dang, 9 xac!')
    score += 1
else:
    print("Incorrect!")


answer = input("Ai rizz gioi nhat? ")
if answer.lower() == "quan":
    print('con ai vao day nua!')
    score += 1
else:
    print("Incorrect!")


answer = input("Ai la racing boi? ")
if answer.lower() == "thai bao":
    print('dan choi ^^!')
    score += 1
else:
    print("Incorrect!")


answer = input("Ai xao lol nhat? ")
if answer.lower() == "thang lol":
    print('cau nay qa de kkk!')
    score += 1
else:
    print("Incorrect!")


answer = input("Ai co nhieu cho' nhat? ")
if answer.lower() == "tuong vy":
    print('9 xax, ko bt co bao nhiu con nua!')
    score += 1
else:
    print("Incorrect!")



answer = input("Ai co bo ma hay xao lol nhat? ")
if answer.lower() == "lan anh":
    print('9 xac!')
    score += 1
else:
    print("Incorrect!")

answer = input("Ban co muon di dalat ko? ")
if answer.lower() == "co":
    print('deo di thi nghi choi!')
    score += 1
else:
    print("Incorrect!")

print("Ban duoc " + str(score)+ " cau dung!")

print("Ban la thanh vien Vip cua HRKLD toi " + str((score/9)*100) + "%.")

print('Cam on ban vi da hoan thanh quizzes, chuc ban mot ngay tot lanh ^^')










