#Baden Erb
#Project 1

import sys, random, os, getpass, shutil, zipfile, urllib.request

#Variable Declarations

mixed = []          #(Most variables  
bad_urls = []       #are inside there
master_urls = []    #functions)

#Changes the path to the desktop

the_desktop = os.path.join('C:\\Users',getpass.getuser(),'Desktop')
os.chdir(the_desktop)

#Functions:
#Function Startup----------------------------------------------------------------------------------------------------------------------
def startup():
    if os.path.exists('.\\URLs'):
        shutil.rmtree('URLs')

    if not os.path.exists('.\\Project Files.zip'):
        print('Hey! You don''t have the files on your desktop! Get outta here!')
        input('Press enter to get outta here!')
        sys.exit()
    else:
        temp = zipfile.ZipFile('.\\Project Files.zip')
        temp.extractall()
        temp.close    
#Function 1----------------------------------------------------------------------------------------------------------------------
def option1():
    print('Processing...please be patient')
    os.chdir(os.path.join('C:\\Users',getpass.getuser(),'Desktop\\URLs\\Mixed URLs'))
    with open('Mixed URLS.txt', 'r') as e:
        for i in e:
            url = i.split('http://')
            try:
                result = urllib.request.urlopen('http://' + url[1],timeout=3).getcode()
                os.chdir(os.path.join('C:\\Users',getpass.getuser(),'Desktop\\URLs\\Bad URLs'))
                with open('Bad URLs 2.txt','a') as b:
                    b.write(i)
            except:
                os.chdir(os.path.join('C:\\Users',getpass.getuser(),'Desktop\\URLs\\Temp'))
                with open('temp.txt','a') as b:
                    b.write(i)

    #Build a list with the URLs                
    os.chdir(os.path.join('C:\\Users',getpass.getuser(),'Desktop\\URLs\\Temp'))
    with open('Temp.txt', 'r') as b:
        for i in b:
            mixed.append(i)

    os.remove('Temp.txt')
    #Iterate thru the list into Master File
    os.chdir(os.path.join('C:\\Users',getpass.getuser(),'Desktop\\URLs'))
    with open('URL Master File.txt', 'a') as b:
        for i in mixed:
            b.write(i)

    #Move the mixed URLs file
    os.chdir(os.path.join('C:\\Users',getpass.getuser(),'Desktop\\URLs\\Mixed URLs'))     
    shutil.move('Mixed URLS.txt', '..\\Mixed URLs\\Processed Mixed URLS')

    #Check for duplicates and re-write master url file
    master_urls = []
    os.chdir(os.path.join('C:\\Users',getpass.getuser(),'Desktop\\URLs'))
    with open('URL Master File.txt','r') as b:
        next(b)
        for i in b:
            master_urls.append(i)

    for i in master_urls:
        for j in bad_urls:
            if(i == j):
                master_urls.remove(i)

    os.remove('URL Master File.txt')
    with open('URL Master File.txt', 'w') as b:
        b.write('Primary Category' + '  ' +  'Secondary Category' + '  ' + 'Title' + '  ' + 'URL' + '\n')
    with open('URL Master File.txt', 'a') as b:
        for i in master_urls:
            b.write(i)
#Function 2----------------------------------------------------------------------------------------------------------------------
def option2():
    os.chdir(os.path.join('C:\\Users',getpass.getuser(),'Desktop\\URLs\\Bad URLs'))
    #Adds the Bad URLs text document lines to a list
    with open('Bad URLs.txt', 'r') as b:
        for i in b:
            bad_urls.append(i)

    master_urls = []
    os.chdir(os.path.join('C:\\Users',getpass.getuser(),'Desktop\\URLs'))
    #Adds the Master URLS text document lines to a list,
    #skipping the first line to account for the header
    with open('URL Master File.txt','r') as b:
        next(b)
        for i in b:
            master_urls.append(i)
    print('URLs are now in their lists')

    #Checks for duplicates
    for i in master_urls:
        for j in bad_urls:
            if(i == j):
                master_urls.remove(i)

    #Rewrites the URL Master File with the updated data
    os.remove('URL Master File.txt')
    with open('URL Master File.txt', 'w') as b:
        b.write('Primary Category' + '  ' +  'Secondary Category' + '  ' + 'Title' + '  ' + 'URL' + '\n')
    print('Processing...Please be patient')
    with open('URL Master File.txt', 'a') as b:
        for i in master_urls:
            b.write(i)

    #Moves the newly processed bad urls to their folder
    os.chdir(os.path.join('C:\\Users',getpass.getuser(),'Desktop\\URLs\\Bad URLs'))
    shutil.move('Bad URLS.txt', '..\\Bad URLS\\Processed Bad URLS')
#Function 3----------------------------------------------------------------------------------------------------------------------
def option3():
    url = ''
    title = ''
    searched_list = []
    #Builds the Master URL list
    master_urls = []
    os.chdir(os.path.join('C:\\Users',getpass.getuser(),'Desktop\\URLs'))
    with open('URL Master File.txt','r') as b:
        next(b)
        for i in b:
            master_urls.append(i)

    #Gets user input
    search = input('Enter all of part of a title: ').upper()
    #Searches the Master URL list
    for i in master_urls:
        temp = i.upper()
        #Finds the search and then puts them in a list if they match
        if(temp.find(search)> 0):
            split1 = i.split('\t')
            url = split1[len(split1)-1]
            title = split1[len(split1)-2]
            searched_list.append(title + '###' + url)

    #Prints the list of found searches
    searched_list.sort()
    print()
    for i in searched_list:
        t_u_split = i.split('###')
        print(t_u_split[0])
        print(t_u_split[1])
    
#CODE BODY----------------------------------------------------------------------------------------------------------------------
startup()
#The Menu
while(True):
    print('---- MAIN MENU ----\n')
    print('Please select from the following options:\n')
    sel = input('1.   Process Mixed URLs\n'+
                '2.   Process Bad URLs\n' +
                '3.   Look up URLs by Title\n' +
                '4.   Exit the program\n'+
                '\nOption#: ')
    if(sel == '1'):
        option1()
    elif(sel == '2'):
        option2()
    elif(sel == '3'):
        option3()
    elif(sel == '4'):
        break
    else:
        input('Make sure you have a valid input! Hit enter to try again.')
