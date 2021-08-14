#library inclusion section 
import nltk
from nltk.chat.util import Chat, reflections
from tkinter import*
#import pyautogui

#creating an output window
main=Tk()
main.geometry("500x600")
main.title("Himanshu's chatbot")

#this part is extra subsetyr data for further use
'''reflections= {'i am': 'you are',
     'i was': 'you were',
     'i': 'you',
     "i'm": 'you are',
     "i'd": 'you would',
     "i've": 'you have',
     "i'll": 'you will',
     'my': 'your',
     'you are': 'I am',
     'you were': 'I was',
     "you've": 'I have',
     "you'll": 'I will',
     'your': 'my',
     'yours': 'mine',
     'you': 'me',
     'me': 'you'}'''

#This section Deals with real time reply based on Predefined Rules
set_pairs = [
    [
        r"this is|my name is (.*)",
        ["Hello %1, How are you doing today ?",]
    ],
    [
        r"hi|hey|hello",
        ["Hello", "Hey there",]
    ], 
    [
        r"what is your name?",
        ["You can call me a Himanshu ",]
    ],
    [
        r"how are you ?",
        ["I am fine, thank you! How can i help you?",]
    ],
    [
        r"I am fine, thank you",
        ["great to hear that, how can i help you?",]
    ],
    [
        r"how can i help you? ",
        ["i am looking for online guides and courses to learn data science, can you suggest?", "i am looking for data science training platforms",]
    ],
    [
        r"i'm (.*) doing good",
        ["That's great to hear","How can i help you?:)",]
    ],
    [
        r"i am looking for online guides and courses to learn data science, can you suggest?",
        ["Pluralsight is a great option to learn data science. You can check their website",]
    ],
    [
        r"thanks for the suggestion. do they have great authors and instructors?",
        ["Yes, they have the world class best authors, that is their strength;)",]
    ],
    [
        r"(.*) thank you so much, that was helpful",
        ["Iam happy to help", "No problem, you're welcome",]
    ],
    [
        r"quit",
    ["Bye, take care. See you soon :) ","It was nice talking to you. See you soon :)"]
],[
        r"Aur bhai kaisa hai,sab theek hai?",
    ["haa bhai mai bhi thik hu"]
]
]

#Defining Chat bot function
def chatbot():
        print("Hi, I'm the chatbot Himanshu built") 

chatbot()
chat = Chat(set_pairs, reflections)
print(chat)
chat.converse()
if __name__ == "__main__":
    chatbot()

#This SEction deals With Setting up the Output Window size
frame=Frame(root)
sc=Scrollbar(frame)
msgs=Listbox(Frame,width=80,height=20)
sc.pack(side=RIGHT,fill=Y)
msg.pack(side=LEFT,fill=BOTH,pady=10)
frame.pack()

#creating txt field
textF=Entry(main,font=("Verdana",20))
textF.pack(fill=X,pady=10)
btn=Button(main,text="Ask me",font=("Verdan",20),command=chatbot)
btn.pack()
main.mainloop()    
