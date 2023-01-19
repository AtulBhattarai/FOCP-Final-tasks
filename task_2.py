print("Park Run Timer\n~~~~~~~~~~~~~~\n\nLet's go!\n")

#creating two empty lists
list1 = []
list2 = []

#main loop to calculate 
while True:
    try:
        main = input("> ")
        if main == "END":
            break
        else:
            a = main.split("::")
            list1.append(int(a[0]))
            list2.append(int(a[1]))
            
            # Counting total number of runners 
            number_of_runners = len(list1)

            # Average time
            avg = sum(list2)/len(list2)
            avg_minutes = int(avg//60)
            avg_seconds = int(avg%60)

            # Fastest time
            fastest_time = min(list2)
            minutes = fastest_time//60
            seconds = fastest_time%60 

            # Slowest time
            slowest_time = max(list2)
            slowest_minutes = slowest_time//60
            slowest_seconds = slowest_time%60

            minm = min(list2)
            place = list2.index(minm)



    #if user input in wrong format
    except:
        print("Error in data stream. Ignorning. Carry on.")

try:
    print(f"\nTotal Runners: {number_of_runners}")
    if avg_minutes <= 1:
        print(f"Average Time: {avg_minutes} minute, {avg_seconds} seconds")
    else:
        print(f"Average Time: {avg_minutes} minutes, {avg_seconds} seconds")

    if minutes <= 1:
        print(f"Fastest Time: {minutes} minute, {seconds} seconds")
    else:
        print(f"Fastest Time: {minutes} minutes, {seconds} seconds")

    if slowest_minutes <= 1:
        print(f"Slowest Time: {slowest_minutes} minute, {slowest_seconds} seconds")
    else:
        print(f"Slowest Time: {slowest_minutes} minutes, {slowest_seconds} seconds")

    print(f"\nBest Time Here: Runner #{list1[place]}")

    
#if user enter END in first input
except:
    print("No data found. Nothing to do. What a pity.")


