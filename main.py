# IMPORTS #
from tkinter import *
from random import randint,choice
from time import time

# CONSTANT #
sentence_bank = [("He set out for a short walk, but now all he could see were mangroves and water were for miles. "
                  "They looked up at the sky and saw a million stars. "
                  "Improve your goldfish's physical fitness by getting him a bicycle."
                  "I want a giraffe, but I'm a turtle eating waffles."),
                 ("He was the type of guy who liked Christmas lights on his house in the middle of July."
                  "He embraced his new life as an eggplant. "
                  "It was the best sandcastle he had ever seen. "
                  "They improved dramatically once the lead singer left. "),
                 ("She let the balloon float up into the air with her hopes and dreams. "
                  "The urgent care center was flooded with patients after the news of a new deadly virus was made public. "
                  "Orchards seemed like a frivolous crop when so many people needed food. "
                  "She folded her handkerchief neatly. ")]

used_sentence = sentence_bank.pop(randint(0,2))

correct = 0
type_speed = 0
start_time = 0
end_time = 0
seconds = end_time-start_time

# FUNCTIONS #

def start_game():
    global start_time
    start_time = time()
    print(start_time)

def results():
    global correct
    global accuracy
    global end_time
    global type_speed
    global seconds

    #END TIME
    end_time = time()

    #Calc correct answer
    user_text = user_entry.get().split(' ')
    sentence = used_sentence.split(' ')
    for word in user_text:
        for answer in sentence:
            if word == answer:
                correct += 1

    # # Calc typing speed
    seconds = round((end_time - start_time),2)
    type_speed = round((correct / (seconds/60)),2)
    time_taken.config(text=f"TIME TAKEN: {seconds} s")
    correct_word.config(text=f"CPM: {type_speed}")
    print(correct)

def reset():
    global used_sentence
    used_sentence = choice(sentence_bank)
    text_label.config(text=f'{used_sentence}')



# --------------------------------------------------- UI -------------------------------------------------------------#

window = Tk()
window.geometry('1200x600')
window.title("Typing Speed Test")
window.configure(bg='black', padx=100,pady=25)

#Label
title_label = Label(text='TYPING SPEED TEST',  font=("Arial",55, 'bold'),pady=25,bg='black', fg='red')
title_label.grid(row=0,column=1)
text_label = Label(text=f"{used_sentence}", font=("Arial",12, 'bold'), wraplength=400,padx=50,pady=25)
text_label.grid(row=1,column=1)


time_taken = Label(text=f'TIME TAKEN: {seconds} ', font=("Arial",10, 'bold'))
time_taken.grid(row=4,column=0)
correct_word = Label(text=f'CPM: {type_speed} ', font=("Arial",10, 'bold'))
correct_word.grid(row=4,column=2)
num_correct = Label(text="NUM WORDS CORRECT: 0",font=("Arial",10, 'bold'))
num_correct.grid(row=4,column=1)

# Entry
user_entry = Entry(width=100)
user_entry.grid(row=2,column=1,pady=25)

# Button
start_btn =  Button(text='START',font=("Arial",12, 'bold'), command=start_game )
start_btn.grid(row=3,column=0, pady=25)
reset_btn = Button(text='RESET',font=("Arial",12, 'bold'),command=reset)
reset_btn.grid(row=3,column=1,  pady=25)
result_btn = Button(text='RESULT', font=("Arial",12, 'bold'), command=results)
result_btn.grid(row=3,column=2,  pady=25)


window.mainloop()