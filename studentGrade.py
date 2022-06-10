A_SCORE = 90
B_SCORE = 80
C_SCORE = 70
D_SCORE = 60
studentScore = int(input("WHAT'S YOUR SCORE/\nSCORE: "))
if studentScore >= A_SCORE:
    print("YOUR GRADE IS A")
else:
    if studentScore >= B_SCORE:
        print("YOUR GRADE IS B")
    else:
        if studentScore >= C_SCORE:
            print("YOUR GRADE IS C")
        else:
            if studentScore >= C_SCORE:
                print("YOUR GRADE IS C")
            else: 
                if studentScore >= D_SCORE:
                    print("YOUR GRDAE IS D")
                else:
                    if studentScore < 60:
                        print("YOU REALLY NEED TO BE SERIOUS!")

