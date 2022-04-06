"""
Movie ordering service:
Console chatbot to order movies at a certain time.
By Tushig Biliguun
"""
#while rebook so if user wants to rebook, it restarts the whole program
rebook = 'yes'
while rebook=='yes':
    #Dictionaries with the movies and times
    movies = ('Toy Story', 'Cars', 'Frozen')
    times = ('10:00', '14:00', '19:00')
    
    time_choice = None
    movie_choice = None
    
    #Dictionary with the customer's order
    seats = (([1,6], [], []), ([], [], []), ([], [], []))
    
    #Program start
    print("Welcome to Tushig's Movie Ordering Bot")
    
    name = input('Please enter your name: ')
    phone_number = input("Please enter your phone number: ")
    
    #Print movies
    print ()
    print ('Todays Movies')
    for index, movie in enumerate(movies):
        print (f"{index + 1}. {movie}")
    
    #Add a blank line
    print()
    
    #Select movie
    #validate movie choice
    while movie_choice == None:
        movie_choice = input('Please, enter the movie code: ')
        match movie_choice:
            case '1':
                movie_choice = int(movie_choice)
                print('You have selected Toy Story, now please select a time')
            case '2':
                movie_choice = int(movie_choice)
                print('You have selected Cars, now please select a time')
            case '3':
                movie_choice = int(movie_choice)
                print('You have selected Frozen, now please select a time')
            case _:
                movie_choice = None
                print("Please input a valid movie code")
    
    #Print times
    print ()
    print('Movie times')
    for index, time in enumerate(times):
        print (f"{index + 1}. {time}")
    
    #Add a blank line
    print()
    #Select time choices
    while time_choice == None:
        time_choice = input('Please, enter the movie code: ')
        match time_choice:
            case '1':
                time_choice = int(time_choice)
                print('You have selected 10:00, now please select a seat')
            case '2':
                time_choice = int(time_choice)
                print('You have selected 14:00, now please select a seat')
            case '3':
                time_choice = int(time_choice)
                print('You have selected 19:00, now please select a seat')
            case _:
                time_choice = None
                print("Please input a valid time slot code")
    
    #pick seats 1-10
    seats_choices = ''
    
    #print seat options 1-10
    print()
    print('Pick your seat')
    for seat in range(1, 11):
        if seat in seats[movie_choice-1][time_choice-1]:
            seats_choices = seats_choices + ' XX'
        else:
            seats_choices = seats_choices + f" {seat}"
    print (seats_choices)
    
    #choose seat from 1-10
    seat_choice = None
    while seat_choice not in range(1, 11):
        try:
            seat_choice = int(input("Please select the seat you want: "))
        except:
            print("Please enter a valid seat number")
            continue
        if seat_choice not in range(1, 11) or seat_choice in seats[movie_choice-1][time_choice-1]:
            print("Seat not available, choose a different seat")
            seat_choice = None
        else:
            seats[movie_choice-1][time_choice-1].append(seat_choice)
            print(f"Seat {seat_choice} booked")
        
    
    #print order information
    print(f"Name: {name}, Phone: {phone_number}, Movie: {movies[movie_choice]}, Time: {times[time_choice]}")
    
    #Cancel seat order
    def repeal_seats(movie_choice, time_choice, seats, seat_choice):
        seats[movie_choice-1][time_choice-1].remove(seat_choice)
        print("Your order has been canceled")
    
    correct = None
    #Check if information is correct
    while correct not in ('yes', 'no'):
        correct = (input("Is the above information correct? ")).lower()
        if correct == 'yes':
            print('Thank you for your order.')
        elif correct == 'no':
            repeal_seats(movie_choice, time_choice, seats, seat_choice)
    
    rebook = None
    #ask user if they want to rebook
    while  rebook not in ('yes', 'no'):
        rebook = (input("Would you like to rebook your order? ")).lower()
        if rebook == 'yes':
            print('Okay, rebooking process starting: ')
            continue
        elif rebook == 'no':
            print("Thank you, choose us again!")
