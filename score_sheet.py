def score_sheet_edition(score):
    
    try:
        with open("score.txt", "a+") as f:
            f.seek(0)
            score_history=f.readlines()[1:]
            print(score_history)
            score_={}
            score_list=[]
            for element in score_history:
                score_list.append([element.split()[0][0:-1],element.split()[1]])
                
            score_list.sort(key = lambda x: float(x[1]), reverse=True)
            f.close()

            if len(score_list)<10 or score>float(score_list[-1][1]):
                print("You are one of top 10 players")
                print("What is your name ?")
                player_name=input()

                score_list.append([player_name,score])
                score_list.sort(key = lambda x: float(x[1]), reverse=True)
                with open("score.txt","w+") as f:
                    f.write("Top 10 players\n")
                    nb_score=min(len(score_list),10)
                    print("********")
                    print(score_list)
                    print("********")
                    for i in range(nb_score):
                        f.write(f"{score_list[i][0]}: {score_list[i][1]}\n")
            f.close()
            return score_list



    except FileNotFoundError:
        print("No file yet, creating one...")
        with open("score.txt", "w") as f:
            f.write("Top 10 players\n")    # if file does not exist you create a header
            print("You are one of top 10 players")
            print("What is your name ?")
            player_name=input()
            f.write(f"{player_name}: {score}")
            f.close()
        return [[f"{player_name}:",score]]


