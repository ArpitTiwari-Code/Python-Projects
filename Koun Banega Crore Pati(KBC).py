"""
   KBC (Koun Banega Crore Pati)
"""
question=["1.Which one of the following river flows between Vindhyan and Satpura ranges?", "2. The Central Rice Research Station is situated in?","  3. Who among the following wrote Sanskrit grammar?"," 4.Which among the following headstreams meets the Ganges in last?","5. The metal whose salts are sensitive to light is?"]
Answer=["Narmada",' Cuttack','Panini', 'Bhagirathi'," Silver"]
print("choose correct option")
Price_money=0
for i in question:          #FOR 1st QUESTION
    if i=="1.Which one of the following river flows between Vindhyan and Satpura ranges?":
        print("First Question On Your Screen")
        print(i)
        print("Ganga\nYamuna\nNarmada\nKaveri")              #OPT FOR FIRST QUES
        a=input("Enter your answer (Case Sensitive)")
        if a=="Narmada":
            print("CORRECT ANSWER\nYOU WON 2000 RUPEES" )
            Price_money+=2000
            print("Total money won till now",Price_money)
        else:
            print("WRONG ANSWER\nYOU ARE OUT OF HOTSEAT")
            print("YOU HAVE LOST ALL YOU CASH PRIZE")
            Price_money=0 
            break
        print()
            
    if i=="2. The Central Rice Research Station is situated in?":               #FOR 2nd QUESTION
        print("Second Question On Your Screen")
        print(i)
        print("Chennai\nCuttack\nBangalore\nQuilon")                             #OPT FOR 2nd  QUES
        a=input("Enter your answer (Case Sensitive)")
        if a=="Cuttack":
            print("CORRECT ANSWER\nYOU WON 5000 RUPEES" )
            Price_money+=5000  
            print(" Total money won till now",Price_money)
        else:
            print("WRONG ANSWER\nYOU ARE OUT OF HOTSEAT")
            print("YOU HAVE LOST ALL YOU CASH PRIZE")
            Price_money-= Price_money
            break
        print()
    if i=="  3. Who among the following wrote Sanskrit grammar?":                   #FOR 3rd QUESTION 
        print("Third Question On Your Screen")
        print(i)
        print("Kalidasa\nCharak\nPanini\nAryabhatt")                             #OPT FOR 3rd  QUES
        a=input("Enter your answer (Case Sensitive)")
        if a=='Panini':
            print(" CORRECT ANSWER\nYOU WON 10000 RUPEES" )
            Price_money+=10000  
            print("Total money won till now",Price_money)
        else:
            print("WRONG ANSWER\nYOU ARE OUT OF HOTSEAT")
            print("YOU HAVE LOST ALL YOU CASH PRIZE")
            Price_money-= Price_money
            break
        print()
    if i==" 4.Which among the following headstreams meets the Ganges in last?":             #FOR 4th QUESTION 
        print(" Fourth Question On Your Screen")
        print(i)
        print(" Alaknanda\nPindar\nMandakini\nBhagirathi")                           #OPT FOR 4th   QUES
        a=input("Enter your answer (Case Sensitive)")
        if a=='Bhagirathi':
            print(" CORRECT ANSWER\nYOU WON 20000 RUPEES" )
            Price_money+=20000
            print(" Total money won till now",Price_money)
        else:
            print("WRONG ANSWER\nYOU ARE OUT OF HOTSEAT")
            print("YOU HAVE LOST ALL YOU CASH PRIZE")
            Price_money-= Price_money
            break
        print()
    if i=="5. The metal whose salts are sensitive to light is?":                                  #FOR 5th QUESTION 
        print(" HOT Question On Your Screen")
        print(i)
        print(" Zinc\nSilver\nCopper\nAluminum")                                #OPT FOR 5th QUES
        a=input("Enter your answer (Case Sensitive)")
        if a=="Silver":
            print("CORRECT ANSWER\n YOU WON 20000 RUPEES" )
            Price_money+=20000
        else:
            print("WRONG ANSWER\nYOU ARE OUT OF HOTSEAT")
            print("YOU HAVE LOST ALL YOU CASH PRIZE")
            Price_money-= Price_money
print()
print("Total price money",Price_money)
    
if  Price_money==57000:
    print("                                              YOU ARE THE WINNER OF THIS SEASON ON OF                       ")
    print("                                                        KOUN BANEGA CROREPATI(KBC)                                               ")
        
