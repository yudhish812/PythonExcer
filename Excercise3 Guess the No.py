
n=34
i=1
print("You have 5 guess only")
while(i<=5):
    no=int(input("Enter your guess\n"))
    if no>34:
        print("Entered higher no")
        G_left = 5 - i
        print("Guess remaining", G_left)
        i=i+1
        continue
    elif no<34:
        print("Entered lower no")
        G_left = 5 - i
        print("Guess remaining", G_left)
        i = i + 1
        continue
    else:
        print("Congratulations, You guessed correct")
        break