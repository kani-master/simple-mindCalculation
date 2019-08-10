#!/usr/bin/env python3

from random import randrange
import sys
import os


def main():
      score = 0
      print("\n")
      print("    __       __    _____     ----------     __       _       _ ____    ")
      print("   /  \     /  \\   | -- |    ||      __     //\\     / \     /   ||     ")
      print("  /    \   /    \\  ||__||    ||     |__    //__\\   /   \   /    ||     ")
      print(" /      \ /      \\ |    \ [*]||________|  //    \\ /     \_/    _||_    ")
               
      r = 0
      option = input("options:\n 1) simple calculation table\n 2) random calculation\n 1 or 2 ??\n")
      if option == "1":
         xh = input("choose [0..9]: ")
         i = 0
         while xh == "":
            i += 1
            print("Enter a number or i will exit >_< ")
            xh = input("choose [0..9]: ")
            if i == 2:
               print("play with ur d**")
               sys.exit()

         while int(xh) >9 or int(xh) < 0 or xh =="":
            xh = input("choose [0..9]: ")
            r += 1
            if r == 5:
               print("you have only one try left")
            if r ==6:
               print("we are not here to play !!")
               sys.exit()
         y = 0
         x = int(xh)
      elif option == "2":
         rng = input("Enter the range of the random numbers (Exp: 9999: [0 to 9999]: ")
         while rng  == "":
               print("Enter a number!!\n")
               rng = input("Enter the range of the random numbers (Exp: 9999: [0 to 9999]: ")
         x = randrange(int(rng))
         y = randrange(int(rng))
         
      end = ""
      opt = input("Operators(* or / or % or - or + ): ")
      
      while True:
             if option == "2":
                         x = randrange(int(rng))
                         y = randrange(int(rng))
             if option == "1":
                         y += 1
             
             if end == "end":
                print ("score: ",score + 1,"/10")
                fptin = input("[ * ] Again?(y=yes, n=no): ")
                if fptin == "y" or fptin == "yes":
                   main()
             
                if fptin == "n" or fptin == "no" or fptin == "N":
                   print("shutdown\n\n\nCreated by Aymen Gani")
                   sys.exit()
                   
                
              
             
             if opt == "*":
                rst = x * y
             if opt == "/":
                rst = x / y
             if opt == "%":
                rst = x % y
             if opt == "+":
                rst = x + y
             if opt == "-":
                rst = x - y  
             print(x,opt,y,"          (< x >:exit / < ! >:help < r >:restart )")
             answer = input(" = ")
             if answer == "x":
                sys.exit()
             if answer == "r":
                main()
             while answer == "":
                print("empty answer!!\n Again!\n",x,opt,y)
                answer = input(" = ")
                if answer == "x":
                   sys.exit()
                if answer == "!":
                    print("= ",rst)
                    answer = str(rst)
             while answer != str(rst):
                 
                 if answer == "!":
                    print("= ",rst)
                    answer = str(rst)
                 print("Again!")
                 score -= 1
                 ####
                 print(x,opt,y,"          (press < x > to exit or < ! > for help)")
                 answer = input(" = ")
                 if answer == "x":
                   sys.exit()
                 if answer == "r":
                   main()
                 while answer == "":
                     print("empty answer!!\n Again!\n",x,opt,y)
                     answer = input(" = ")
             #if answer is true.    
             if int(answer) == rst:
                print("[OK]")
                score += 1
                
             if y == 9:
                end = "end"
                y = 0
                
main()          
          
          
