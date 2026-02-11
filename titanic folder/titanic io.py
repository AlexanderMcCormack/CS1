

def First_rows(file):
    with open('titanic.csv', 'r') as file:
        num_rows = 0
        for line in file:
            row = line.strip().split(',')
            print(row)
            num_rows +=1
            if num_rows == 11:
                break 

def survival_rate(file):
    survivors = 0 
    total_people = 0
    male_survival = 0 
    female_survival = 0

    for line in file:
        row = line.strip().split(',')
        total_people += 1

        if row[1] == "1":
            survivors +=1
        if row [5] == "male":
            male_survival +=1
        if row[5] == "female":
            female_survival +=1

    MSR = (male_survival/total_people) * 100
    FSR = (female_survival/total_people) * 100

    survival_percent = (survivors/total_people) * 100
    file.write (f'survival_percent: {survival_percent}')
    file.write (f'MSR: {MSR}')
    file.write (f'FMR: {FSR}')
 
def average_age(file):

    total_people = 0
    total_age = 0
    survivors = 0 
    age_survivors = 0
    non_survivors = 0
    age_non_survivors = 0
    youngest = 0
    oldest = 0
    with open('titanic.csv', 'r')as file:
        next(file)

        for line in file:
            row = line.strip().split(',')
            
            if row[6] =='':
                continue
            age = row[6]
            total_people += 1
            total_age += float(row[6]) 

            if row[1] == "1":
                survivors += 1
                age_survivors += float(row[6])
            else:
                non_survivors += 1
                age_non_survivors += float(row[6])
            if youngest == 0 or age < youngest:
                youngest = age
            if oldest == 0 or age > oldest:
                oldest = age
    
    average_age = total_age/total_people
    average_survivors = age_survivors/survivors
    average_nonsurvivor = age_non_survivors/non_survivors
    file.write(f'average_age: {average_age}')
    file.write(f'average_survivors: {average_survivors}')
    file.write(f'average_nonsurvivor: {average_nonsurvivor}')
    file.write(f'youngest: {youngest}')
    file.write(f'oldest: {oldest}')

def class_based_analysis(file):
    file.seek(0)
    first_class_survivors = 0
    first_class_total = 0
    first_class_fare = 0
    
    second_class_survivors = 0
    second_class_total = 0
    second_class_fare = 0
    
    third_class_survivors = 0
    third_class_total = 0
    third_class_fare = 0
    
    with open('titanic.csv', 'r') as file:
        next(file)  
        
        for line in file:
            row = line.strip().split(',')
            
            pclass = row[2]  
            survived = row[1] 
            fare = row[10]
            
            if fare == '':
                continue
            
            if pclass == "1":
                first_class_total += 1
                try:
                    first_class_fare += float(fare)
                except ValueError:
                    pass
                if survived == "1":
                    first_class_survivors += 1
                
            elif pclass == "2":
                second_class_total += 1
                try:
                    second_class_fare += float(fare)
                except ValueError:
                    pass
                if survived == "1":
                    second_class_survivors += 1
                
            elif pclass == "3":
                third_class_total += 1
                try:
                    third_class_fare += float(fare)
                except ValueError:
                        pass
                if survived == "1":
                        third_class_survivors += 1
    
    
    first_class_survival_rate = (first_class_survivors / first_class_total)*100
    second_class_survival_rate = (second_class_survivors / second_class_total)*100
    third_class_survival_rate = (third_class_survivors / third_class_total)*100
    
    first_class_avg_fare = first_class_fare / first_class_total
    second_class_avg_fare = second_class_fare / second_class_total
    third_class_avg_fare = third_class_fare / third_class_total
    
    file.write(f'First Class Survival Rate: {first_class_survival_rate:.2f}%')
    file.write(f'First Class Average Fare: ${first_class_avg_fare:.2f}')
    file.write(f'First Class Passengers: {first_class_total}')
    file.write()
    file.write(f'Second Class Survival Rate: {second_class_survival_rate:.2f}%')
    file.write(f'Second Class Average Fare: ${second_class_avg_fare:.2f}')
    file.write(f'Second Class Passengers: {second_class_total}')
    file.write()
    file.write(f'Third Class Survival Rate: {third_class_survival_rate:.2f}%')
    file.write(f'Third Class Average Fare: ${third_class_avg_fare:.2f}')
    file.write(f'Third Class Passengers: {third_class_total}')
    file.write()
    
    if first_class_survival_rate > second_class_survival_rate and first_class_survival_rate > third_class_survival_rate:
        file.write(f'Best Survival Chances: First Class ({first_class_survival_rate:.2f}%)')
    elif second_class_survival_rate > third_class_survival_rate:
        file.write(f'Best Survival Chances: Second Class ({second_class_survival_rate:.2f}%)')
    else:
        file.write(f'Best Survival Chances: Third Class ({third_class_survival_rate:.2f}%)')


def main():
    print('what information do you need, 1. first 10 rows of the manifest, 2. survival rate of passengers, 3. average age of passengers, 4. class based analysis')
    with open('titanic.csv', 'r') as file:
        options = input()
        if options == '1':
            First_rows(file)
        elif options == "2": 
            survival_rate(file)
        elif options == '3':
            average_age(file)
        elif options == '4':
            class_based_analysis(file)

            '''except FileNotFoundError:
            print("Error: 'titanic.csv' file not found.")'''

main() 