import time
def print_colored_text(text, color_name)
    colors = ("red","blue","green","purple","yellow")
    color_code = colors.get(color_name.lower())
    print("f(color_code)(text)")
    
    print ("Alarm!" 'red')


while True:
    snooze = input ("Snooze? yes/no: ")

    if snooze == "yes":
        print ("Sleep 5 more minutes" 'blue')
        time.sleep(2)
        print ("Alarm!")
    elif snooze == "no":
        break
    else:
        print ("Invalid Response!")

print ("Take a shower!")

while True:
    brush_teeth = input ("brush teeth? yes/no: ")
    if brush_teeth == "yes":
        print ("get dressed")
        break
    elif brush_teeth == "no":
        print ("brushteeth")
        break
    else:
        print ("Invalid Response!")
        
while True:
    cold_enough = input ("Cold enough to wear pants? yes/no: ")
    if cold_enough == "yes":
        print ("Put pants on")
        break
    elif cold_enough == "no":
        print ("Put shorts on")
        break
    else:
        print ("Invalid Response!")

while True:
    shoes = input ("addidas? yes/no: ")
    if shoes == "yes":
        print ("grab ultra boosts")
        break
    elif shoes == "no":
        print ("grab Nike")
        break
    else:
        print ("Invalid Response!")

while True:
    eat_breakfast = input ("Eat breakfast? yes/no: ")
    if eat_breakfast == "yes":
        print ("eat and go to the door")
        break
    elif eat_breakfast == "no":
        print ("go to the door")
    else:
        print ("Invalid Response!")
        while True:
            wait_for_bus = input ("wait inside? yes/no: ")
            if wait_for_bus == "yes":
                print ("stand inside the door")
                break
            elif wait_for_bus == "no":
                print ("stand on the porch")
            else:
                print ("Invalid Response!")
