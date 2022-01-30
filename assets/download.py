f= open("list-hands.txt","w+")
for i in range(169):
     f.write("https://emoji-maker.com/assets/emojis/Hands/%d.png " % (i+1))
f.close()