def score_sheet_edition(score):
    score_file=open("score.txt","w+")
    data=score_file.read() # read whole file
    print("You are one of top 10 players")
    print("What is your name ?")
    player_name=input()
    score_file.write(f"{player_name}: {score}")



