#This program gives you 6 tries to find the number between 1 and 20. | Ten program daje 6 próbuje znaleźć liczbę między 1 a 20.

import random #import a built-in module that allows for random generation | import wbudowanego modułu umożliwiającego losowe generowanie

guesses_taken = 0 #global variable that starts at 0 | Zmienna globalna, która zaczyna się od 0

print('Hello! What is your name?') #Print command that displays the first message user sees. | Polecenie Drukuj, które wyświetli pierwszą wiadomość, którą użytkownik widzi.
myName = input() #variable that will store the users name when input | Która przechowuje nazwę użytkownika podczas wprowadzania danych

number = random.randint(1, 20) # Generates a random whole number (Integer) between 1 and 20. | Generuje losową liczbę całkowitą (Integer) pomiędzy 1 a 20.
print('Well, ' + myName + ', I am thinking of a number between 1 and 20.') #Print command that calls on user input name + message | Polecenie wydruku, które wywołuje nazwę użytkownika + wiadomość

while guesses_taken < 6: #runs while guesses_taken variable is below 6 | Podczas gdy zmienna guesses_taken jest poniżej 6, uruchamia się ten kod.
    print('Take a guess.') #printed message that displays when asking question | Wydrukowany komunikat, który pojawia się podczas zadawania pytań
    guess = input() #defines the input of guess | # Określa dane odgadnięcia
    guess = int(guess) #changes the input to an integer | Zmienia dane wejściowe na liczbę całkowitą

    guesses_taken += 1 #adds 1 guesses_taken per time this is run | dodaje 1 guesses_taken za każdym razem, gdy jest uruchomiony

    if guess < number: #runs if number guessed is lower than target number | działa, jeśli liczba zgadywana jest mniejsza niż liczba docelowa
        print('Your guess is too low.') #message that appears if ^above^ is currently true | Komunikat, który pojawia się, jeśli ^ powyżej ^ jest aktualnie prawdziwy

    if guess > number: #runs if number guesed is higher than target number | Działa, jeśli liczba podana jest wyższa niż liczba docelowa
        print('Your guess is too high.') #message that appears if ^above^ is currently true | Komunikat, który pojawia się, jeśli ^ powyżej ^ jest aktualnie prawdziwy

    if guess == number: #runs if user integer input is the same as target number | działa, jeśli wejście całkowite użytkownika jest takie samo jak numer docelowy
        break #stops the whileLoop upon guessing right number | Zatrzymuje whileLoop podczas zgadywania prawego numeru

if guess == number: #runs if user integer input is the same as target number | Działa, jeśli wejście całkowite użytkownika jest takie samo jak numer docelowy
    guesses_taken = str(guesses_taken) #converts guesses taken to a string | Konwertuje przypuszczenia na ciąg
    print('Good job, ' + myName + '! You guessed my number in ' + guesses_taken + ' guesses!') #printed message with name the user input and amount of guesses, in string format | drukowana wiadomość z nazwą użytkownika i kwota zgadywania, w formacie ciąg

if guess != number: #runs if whileLoop has ended and the guessed numbers do not match the target number | Działa, jeśli podczas Kończy się Kończy się, a zgadywane numery nie odpowiadają numerowi docelowemu
    number = str(number) #converts target number to a string | konwertuje numer docelowy na ciąg
    print('Nope. The number I was thinking of was ' + number) #displays message with the target number | Wyświetla komunikat z numerem docelowym
