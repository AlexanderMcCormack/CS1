import time
print ("Alarm!")                                                  #display Alarm!
while True:                                                       #forever loop
    snooze = input ("Snooze? yes/no: ")                           #stores user response in variable snooze

    if snooze == "yes":                                           #if user snoozes
        print ("Sleep 5 more minutes")                            #display message 
        time.sleep(2)                                             #waits 2 seconds
        print ("Alarm!")                                          #display message 
    elif snooze == "no":                                          #if user does not snooze
        break                                                     #end loop
    else:                                                         #if user responds anything else
        print ("Invalid Response!")                               #display message

print ("Take a shower!")                                          #display message 

while True:                                                       #forever loop
    brush_teeth = input ("brush teeth? yes/no: ")                 #stores user response in variable brush teeth
    if brush_teeth == "yes":                                      #if user brushes teeth
        print ("get dressed")                                     #display message
        break                                                     #end loop
    elif brush_teeth == "no":                                     #if user does not brush teeth
        print ("brushteeth")                                      #display message 
        break                                                     #end loop
    else:                                                         #if user responds anything else
        print ("Invalid Response!")                               #display message  
        
while True:                                                       #forever loop
    cold_enough = input ("Cold enough to wear pants? yes/no: ")   #stores user response in variable cold enough
    if cold_enough == "yes":                                      #if user could enough
        print ("Put pants on")                                    #display message 
        break                                                     #end loop
    elif cold_enough == "no":                                     #if user is not cold enough
        print ("Put shorts on")                                   #display message 
        break                                                     #end loop
    else:                                                         #if user responds anything else
        print ("Invalid Response!")                               #display message 

while True:                                                       #forever loop
    shoes = input ("addidas? yes/no: ")                           #stores user response in variable shoes
    if shoes == "yes":                                            #if user wants addidas 
        print ("grab ultra boosts")                               #display message 
        break                                                     #end loop
    elif shoes == "no":                                           #is user does not want addidas 
        print ("grab Nike")                                       #display message
        break                                                     #end loop
    else:                                                         #if user responds anything else 
        print ("Invalid Response!")                               #display message 

while True:                                                       #forever loop
    eat_breakfast = input ("Eat breakfast? yes/no: ")             #stores user response in variable eat breakfast
    if eat_breakfast == "yes":                                    #if user wants breakfast
        print ("eat and go to the door")                          #display message 
        break                                                     #ends loop
    elif eat_breakfast == "no":                                   #if user does not want breakfast
        print ("go to the door")                                  #display message 
    else:                                                         #if user responds anything else
        print ("Invalid Response!")                               #display message 
        while True:                                               #forever loop
            wait_for_bus = input ("wait inside? yes/no: ")        #stores user response in variable wait for bus
            if wait_for_bus == "yes":                             #if user wants to wait inside 
                print ("stand inside the door")                   #display message 
                break                                             #end loop 
            elif wait_for_bus == "no":                            #if user does no want to wait inside 
                print ("stand on the porch")                      #display message 
            else:                                                 #if user respondes anything else
                print ("Invalid Response!")                       #display message 
