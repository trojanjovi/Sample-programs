import time


def main():
    print("""         ______ ____ __  ___ ______ ____     _  __                
        /_  __//  _//  |/  // ____// __ \   | |/ /                
         / /   / / / /|_/ // __/  / /_/ /   |   /                 
        / /  _/ / / /  / // /___ / _, _/   /   |                  
       /_/  /___//_/  /_//_____//_/ |_|   /_/|_|   
         >>Timer: minsan code, madalas sya
   ____  _____  ____   ____  _       __ ___   ______ ______ __  __
  / ___//_  __// __ \ / __ \| |     / //   | /_  __// ____// / / /
  \__ \  / /  / / / // /_/ /| | /| / // /| |  / /  / /    / /_/ / 
 ___/ / / /  / /_/ // ____/ | |/ |/ // ___ | / /  / /___ / __  /  
/____/ /_/   \____//_/      |__/|__//_/  |_|/_/   \____//_/ /_/   
                         >>Stop na. watchla kang pag-asa don                                                                                                          
1: Timer                                  2: Stopwatch                                          
clock used for measuring                  counts upwards from zero
specific time intervals.                  for measuring time intervals.

""")
    
    x=input("Choose your fighter:")
    if x=="1": #if input is 1 timer function is executed
        timer()
    elif x=="2":#if input is 2 stopwatch function is executed
        stopwatch()
    else:
        print("Thank you!")
        
                
def convert_time(sec): #converts seconds into minutes
  mins = sec // 60
  sec = sec % 60
  hours = mins // 60
  mins = mins % 60
  #prints the results
  print("Time Lapsed = {0}:{1}:{2}".format(int(hours),int(mins),sec)) 

def stopwatch(): #stopwatch program
    print("""   _____ ______ ____   ____  _       __ ___   ______ ______ __  __
  / ___//_  __// __ \ / __ \| |     / //   | /_  __// ____// / / /
  \__ \  / /  / / / // /_/ /| | /| / // /| |  / /  / /    / /_/ / 
 ___/ / / /  / /_/ // ____/ | |/ |/ // ___ | / /  / /___ / __  /  
/____/ /_/   \____//_/      |__/|__//_/  |_|/_/   \____//_/ /_/
""")
    z=input("Enter any key to continue and x to go back: ")#ask if he wants to continue
    if z == "x": #if "x" is chosen it will return back to the main function
        main()
    else: # continues program
        print ("")

    input("Press Enter to start") #prompts the user to start stopwatch
    start = time.time()
    input("Press Enter to stop \n") #prompts the user to end the stopwatch
    end = time.time()
    time_lapsed = end - start #the start time and end time will be subtracted 
    convert_time(time_lapsed) #prints time lapsed
    stopwatch()



def timer(): #timer program 
    print("""  ______ ____ __  ___ ______ ____     
 /_  __//  _//  |/  // ____// __ \    
  / /   / / / /|_/ // __/  / /_/ /    
 / /  _/ / / /  / // /___ / _, _/     
/_/  /___//_/  /_//_____//_/ |_|
""") 
    z=input("Enter any key to continue and x to go back: ") #ask if he wants to continue
    if z == "x": #if "x" is chosen it will return back to the main function
        main()
    else:
        print ("") #continues program
     
    # Ask for how long the timer will be
    try:
        Min1 =int(input("Enter How Many Minutes: "))
        assert Min1 <= 60 #asserts what should be the input
    except ValueError: #prompts the user to enter valid input
        print("Please Input numbers only \n")
        return timer() #return back to the timer function
    except: #if input is wrong, prompts user to enter new input
        while Min1 > 60:
            print("Please Input up to 60 Minutes only") 
            Min1 = int(input("Enter How Minutes: "))

        # Ask for how long the timer will be
    try:
        Sec1 =int(input("Enter How Many Seconds: "))
        assert Sec1 <= 60 #asserts what should be the input
    except ValueError: #prompts the user to enter valid input
        print("Please Input numbers only \n")
        return timer()
    except: #if input is wrong, prompts user to enter new input
        while Sec1 > 60:
            print("Please Input up to 60 Seconds only") 
            Sec1 = int(input("Enter How Seconds: "))            

        # Variables to keep track and display
    Min=int(0)
    Sec=int(0)
        
        # Begin Process
    start = input("Press Any Key To Start: ") # prompts the user to start
    while True:
        Sec += 1
        #prints state every second
        print(str(Min) + " Mins " + str(Sec) + " Sec ") 
        time.sleep(1)
        if Sec == 60: #if seconds reached 60 it reverts back to 0
            Sec = 0
            Min += 1 #if seconds reached 60 it is equal to 1 minute
            print(str(Min) + " Minute") 
                
        elif(Min==Min1) and (Sec==Sec1):
            break # If time is reached loop process will end
            
    print("Times up!") #the time is up
    timer() #restarts timer function
    
main() #runs the program
