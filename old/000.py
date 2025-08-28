import webbrowser
'''
this is a script to search google.com efectively
'''
def so(opt):
        if opt == 1:
            site = input('What site to search?              >')
            ftyp = input('What file type are you searching? >')
            stri =  input('What string to search?            >')
            webbrowser.open(f'http://google.com/search?q=site:{site}%20filetype:{ftyp}%20"{stri}"', new=2)
        if opt == 2:
            site = input('What site to search?              >')
            webbrowser.open(f'http://google.com/search?q=site:{site}', new=2)

so(int(input('[1] All | [2] Site only | [3] Soon...')))
