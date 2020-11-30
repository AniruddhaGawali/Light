import random
from tkinter.constants import INSERT
from chatterbot import ChatBot
chatbot=ChatBot('light',
    logic_adapters=[{
        'import_path':"chatterbot.logic.BestMatch",
        # 'import_path':'chatterbot.logic.TimeLogicAdapter',
        'default_response':'I am sorry, but I do not understand.',}
        
    ]
)


def think(command,chatbox):
    chatbox.tag_config('p',justify='left',font='helvatica 13',foreground='white')#,background='orange')
    chatbox.tag_config('b',justify='left',font='helvatica 13',foreground='gold')#,background='gold')

    if command in ['How can you help','What can you do']:
        chatbox.insert(INSERT, f'YOU : {command}','p')
        chatbox.insert(INSERT, f'\n')
        chatbox.insert(INSERT,f'BOT : I can help you in your work and also can chat with.\n         Its make me happy to help you','b')
        chatbox.insert(INSERT, f'\n')

    elif command in ['Tell me a joke','Tell joke']:
        chatbox.insert(INSERT, f'YOU :{command}\n','p')
        i=random.choice((1,2,3,4,5))
        with open(f"data/joke/j{i}.txt",'r') as f:
            a= f.read()
        chatbox.insert(INSERT,f'BOT : {a}\n','b')
    
    elif 'search on wiki' in command:
        import wikipedia
        query = command.replace("search on wiki", "")
        chatbox.insert(INSERT, f'YOU :{command}\n','p')
        chatbox.insert(INSERT,f'BOT : Search on Wiki...\n','b')
        print(query)
        results = wikipedia.summary(query, sentences=5)
        chatbox.insert(INSERT,f'BOT : According to wikipedia : {results}\n','b')


    
    elif command in ['Open google']:
        chatbox.insert(INSERT, f'YOU : {command}\n','p')
        import webbrowser
        webbrowser.open_new_tab("http://www.google.com")
        chatbox.insert(INSERT,f'BOT : Opening Google on your browser\n','b')
    elif command in ['Open youtube']:
        chatbox.insert(INSERT, f'YOU : {command}\n','p')
        import webbrowser
        webbrowser.open_new_tab("http://www.youtube.com")
        chatbox.insert(INSERT,f'BOT : Opening Youtube on your browser\n','b')

    elif command in ['Open wiki','Open wikipedia']:
        chatbox.insert(INSERT, f'YOU : {command}\n','p')
        import webbrowser
        webbrowser.open_new_tab("http://www.wikipedia.com")
        chatbox.insert(INSERT,f'BOT : Opening Wiki on your browser\n','b')

    elif command in ['Open code']:
        chatbox.insert(INSERT, f'YOU : {command}\n','p')
        chatbox.insert(INSERT,f'BOT : Opening VS Code\n','b')
        import os
        os.system('code')

    elif command in ['Play music', 'Open music','Play song']:
        import os
        import tkinter.filedialog as tf
        music_dir = tf.askdirectory()
        songs = os.listdir(music_dir)    
        os.startfile(os.path.join(music_dir, songs[0]))

    elif command == '':
        chatbox.insert(INSERT, f'YOU : {command}\n','p')
        chatbox.insert(INSERT,f'BOT : You havn\'t write any thing\n','b')

    elif '+' in command:
        chatbox.insert(INSERT, f'YOU : {command}\n','p')
        l=[command[i] for i in range(0, len(command), 1)]
        try:
            chatbox.insert(INSERT,f'BOT : {command} = {int(l[0])+int(l[2])}\n','b')
        except ValueError:
            chatbox.insert(INSERT,f'BOT : {command}!!!! Please input correctly or if a sentence then dont used this symbols (+,-,*,/) \n','b')
            
    elif '-' in command:
        chatbox.insert(INSERT, f'YOU : {command}\n','p')
        l=[command[i] for i in range(0, len(command), 1)]
        try:
            chatbox.insert(INSERT,f'BOT : {command} = {int(l[0])-int(l[2])}\n','b')
        except ValueError:
            chatbox.insert(INSERT,f'BOT : {command}!!!! Please input correctly or if a sentence then don\'t used this symbols (+,-,*,/) \n','b')

    elif '*' in command:
        chatbox.insert(INSERT, f'YOU : {command}\n','p')
        l=[command[i] for i in range(0, len(command), 1)]
        try:
            chatbox.insert(INSERT,f'BOT : {command} = {int(l[0])*int(l[2])}\n','b')
        except ValueError:
            chatbox.insert(INSERT,f'BOT : {command}!!!! Please input correctly or if a sentence then don\'t used this symbols (+,-,*,/) \n','b')

    elif '/' in command:
        chatbox.insert(INSERT, f'YOU : {command}\n','p')
        l=[command[i] for i in range(0, len(command), 1)]
        try:
            chatbox.insert(INSERT,f'BOT : {command} = {int(l[0])/int(l[2])}\n','b')
        except ValueError:
            chatbox.insert(INSERT,f'BOT : {command}!!!! Please input correctly or if a sentence then don\'t used this symbols (+,-,*,/) \n','b')
               
    elif 'time' in command:
        import datetime
        now = datetime.datetime.now()
        chatbox.insert(INSERT, f'YOU : {command}\n','p')
        chatbox.insert(INSERT,f'BOT : Current time is {now.strftime("%H:%M:%S")}\n','b') 
    elif  command in ['Take notes',"Add notes",'Make notes','Open notes','Open note','Take note',"Add note",'Make note']:
        import subprocess
        subprocess.run('explorer.exe shell:appsFolder\Microsoft.MicrosoftStickyNotes_8wekyb3d8bbwe!App')
        chatbox.insert(INSERT, f'YOU : {command}\n','p')
        chatbox.insert(INSERT,f'BOT : Opening Sticky Notes','b')

    else:
        chatbox.insert(INSERT, f'YOU : {command}\n','p')
        chatbox.insert(INSERT,f'BOT : {chatbot.get_response(command)}\n','b')





def input(command,chatbox):
    c=str(command.get())
    think(c.capitalize(),chatbox)