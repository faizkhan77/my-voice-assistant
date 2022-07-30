import pyttsx3
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import datetime
import random

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voices', voices[1].id)

myvoice_assistant_name = "nami"


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour <=12:
        speak("Good morning")
    elif hour >= 12 and hour <= 17:
        speak("Good afternoon")
    elif hour >= 17 and hour <= 20:
        speak("Good evening")
    else:
        speak("Good night")

    speak(f"my name is {myvoice_assistant_name}, What is your name")
    name = input("Please enter your name: \n")
    speak(f"Hello {name} Please tell me how may i help you")


def takecommand():
    """To take microphone input from user and return it as a string"""
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said {query}")
        # speak(query)
    except Exception as e:
        # print(e)
        x = "I cannot hear you proper, please speak louder"
        speak(x)
        return "None"
    return query



if __name__ == '__main__':
    wishme()
    while True:
        query = takecommand().lower()

        """Logics for executing tasks"""

        def basiconvo():
            if 'how are you' in query:
                speak("im fine, what about you")
            elif 'who created you' in query or 'who made you' in query:
                speak("i was created by faiz khan")
            elif 'what is your name' in query:
                speak(f"my name is {myvoice_assistant_name}")
            elif 'who are you' in query:
                speak(f"I am your virtual assistant created by Faiz")
            elif 'i am fine' in query:           #W
                speak("im glad you are fine")
            elif "ok" in query or "good" in query:
                speak("is there anything else i can do for you, sir")
            elif 'can you sing' in query:         #W
                speak("no, i am a bad singer")
            elif 'how old are you' in query or 'what is your age' in query:    #W
                speak("i am 1 day old")
            elif 'how many languages' in query:
                speak("as of now i can only speak english")
            elif 'humans' in query:
                speak("yes i love humans")
            elif 'are you a robot' in query:
                speak("i am your virtual assistant")
            elif 'correct' in query or 'good' in query:
                speak("see, i knew it")
            elif 'not fine' in query:
                speak("oh, i hope you feel better, want me to play you a song")
            elif 'can you be my girlfriend' in query or 'can you be my boyfriend' in query:
                speak("sorry, i am already taken")
            elif 'love me' in query:
                speak("ofcourse i do")
            elif 'where are you from' in query:
                speak("i am from your imagination")
            elif 'is love' in query:
                speak("it is the 7th sense that destroy all other senses")
            elif 'favourite colour' in query:
                speak("my favourite color is blue because i love the sky")
            elif 'nami' in query:
                speak("yes master what can i do for you")


        basiconvo()

        def rps():
            """ROCK, PAPER AND SCISSOR GAME"""

            import random
            import colorama
            from colorama import Fore, Back, Style

            speak("You play against me for 10 rounds, the one who won the most, win the game!")
            options = ["rock", "paper", "scissor"]
            user_win = 0
            compute_win = 0
            initial_round = 1
            max_round = 10

            while initial_round <= max_round:
                pc = random.choice(options)
                print(f"Numbers of rounds: {initial_round}")
                print(Style.BRIGHT + "Enter r for rock, p for paper and s for scissor\033[39m")
                user = input("Enter here: ")
                if pc == "rock":
                    speak("rock")
                    if user == "p":
                        print(Fore.GREEN + "Computer : rock")
                        speak("you win this round")
                        user_win += 1
                        print(f"\033[39mYour score: {user_win}")
                        print(f"\033[39mcomputer score: {compute_win}\033[39m")
                    elif user == "s":
                        print(Fore.GREEN + "Computer : rock")
                        speak("you lost this round")
                        compute_win += 1
                        print(f"\033[39mYour score: {user_win}")
                        print(f"\033[39mcomputer score: {compute_win}\033[39m")
                    elif user == "r":
                        print(Fore.GREEN + "Computer : rock")
                        speak("Its a tie")
                    else:
                        speak("Invalid input")
                    initial_round += 1


                elif pc == "paper":
                    speak("paper")
                    if user == "s":
                        print(Fore.GREEN + "Computer : paper")
                        print(Fore.GREEN + "Computer : rock")
                        speak("you win this round")
                        user_win += 1
                        print(f"\033[39mYour score: {user_win}")
                        print(f"\033[39mcomputer score: {compute_win}\033[39m")
                    elif user == "r":
                        print(Fore.GREEN + "Computer : paper")
                        speak("you lost this round")
                        compute_win += 1
                        print(f"\033[39mYour score: {user_win}")
                        print(f"\033[39mcomputer score: {compute_win}\033[39m")
                    elif user == "p":
                        print(Fore.GREEN + "Computer : paper")
                        speak("Its a tie")
                    else:
                        speak("Invalid input")
                    initial_round += 1


                elif pc == "scissor":
                    speak("scissor")
                    if user == "r":
                        print(Fore.GREEN + "Computer : scissor")
                        print(Fore.GREEN + "Computer : rock")
                        speak("you win this round")
                        user_win += 1
                        print(f"\033[39mYour score: {user_win}")
                        print(f"\033[39mcomputer score: {compute_win}\033[39m")
                    elif user == "p":
                        print(Fore.GREEN + "Computer : scissor")
                        speak("you lost this round")
                        compute_win += 1
                        print(f"\033[39mYour score: {user_win}")
                        print(f"\033[39mcomputer score: {compute_win}\033[39m")
                    elif user == "s":
                        print(Fore.GREEN + "Computer : scissor")
                        speak("Its a tie")
                    else:
                        speak("Invalid input")
                    initial_round += 1

            if user_win > compute_win:
                speak("CONGRATULATION YOU WIN THE GAME!!")
            elif compute_win > user_win:
                speak("SORRY YOU LOSE THE GAME!!")
            else:
                speak("THE GAME ENDED IN A TIE!")

        if 'wikipedia' in query:
            speak("searching wikipedia...")
            query = query.replace("wikipedia", "")
            result = wikipedia.summary(query, sentences=1)
            speak("According to wikipedia")
            print(result)
            speak(result)

        elif 'play rock paper scissor' in query:
            speak("ok lets play rock, paper and scissors")
            rps()

        elif 'open youtube' in query:
            speak("opening youtube")
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            speak("opening google")
            webbrowser.open("google.com")
        elif 'open github' in query:
            speak("opening github")
            webbrowser.open("github.com")

        elif 'play music' in query:
            music_dir = 'c:\\Users\\hp\\PycharmProjects\\VoiceAssistant\\mymusics'
            songs = os.listdir(music_dir)
            print(songs)
            random = os.startfile(os.path.join(music_dir, songs[1]))

        elif 'the time' in query:
            strtime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {strtime}")


        elif 'go to sleep' in query:
            speak("Ok then, i am going to sleep, bye")
            quit()








