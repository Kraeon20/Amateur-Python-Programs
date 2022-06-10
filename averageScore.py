firstScore = float(input("WHAT WAS YOUR FIRST SCORE:\n"))
secondScore = float(input("WHAT WAS YOUR SECOND SCORE:\n"))
thirdScore = float(input("WHAT WAS YOUR THIRD SCORE:\n"))
totalScore = (firstScore + secondScore + thirdScore)
averageScore = totalScore / 3
print("YOUR AVERAGE SCORE WAS", format(averageScore, ",.1f"))
if averageScore >= 95:
    print("CONGRATULATION!")
else:
    print("THERE'S MORE ROOM FOR IMPROVEMENT!")