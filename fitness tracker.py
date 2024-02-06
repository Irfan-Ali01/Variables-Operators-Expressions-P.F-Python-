steps=[]
distance=[]
for i in range(7):
    if i==0:
        print()
        print('Monday')
        print()
    if i==1:
        print()
        print('Tuesday')
        print()
    if i==2:
        print()
        print('Wedneday')
        print()
    if i==3:
        print()
        print('Thursday')
        print()
    if i==4:
        print()
        print('Friday')
        print()
    if i==5:
        print()
        print('Saturday')
        print()
    if i==6:
        print()
        print('Sunday')
        print()
    daily_steps=int(input('Enter Your Daily steps; '))
    steps.append(daily_steps)
    distance_walked=int(input('Enter Distance You Walked; '))
    distance.append(distance_walked)
    calories_burned=int(input('Calories Burned; '))
total_steps=sum(steps)
average_steps=total_steps/7
total_distance=sum(distance)
average_distance=total_distance/7
monthly_distance=(average_distance*4)+2
print()
print ('Average Steps Per Week; ',int(average_steps))
print('Total Distance Covered in a Month; ',int(monthly_distance))