import webbrowser; from os import system
whodev = 'Developed, and maintained by sftmlgwastaken, www.sftmlg.xyz'
inputString = f'{whodev}\nEnter only numbers, because it will break otherwise \n[1] All | [2] Site only | [3] Search Exact Phrase :> \n[0] Exit \n->>'
ssite = 'What site to search?--------------->'
sfile = 'What file type are you searching?-->'
stext = 'What file type are you searching?-->'
sengine = 'https://google.com/search?q='
#this is a script to search google.com effectively

def so(opt):
    while True:
            if opt == 1:
                site = input(f'{ssite}')
                file = input(f'{sfile}')
                text = input(f'{stext}')
                system('cls')
                webbrowser.open(f'{sengine}site:{site}%20filetype:{file}%20"{text}"', new=2)
                system('cls')
            if opt == 2:
                site = input('What site to search?              >')
                webbrowser.open(f'{sengine}site:{site}', new=2)
            if opt==3:
                phrase = input('What phrase are you searching for >')
                webbrowser.open(f'{sengine}"{phrase}"', new=2)
            if opt==0: return 'exit'
so(int(input(f'{inputString}')))
