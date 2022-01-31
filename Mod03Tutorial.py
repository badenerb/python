#Baden Erb
#Mod 03 Tutorial

import sys
import random

lyrics_string=("Quisiera:Ayer:cambiarle:conocí:el:un:final"
               ":cielo:al:sin:cuento|Las:sol|Y:barras:un:y"
               ":hombre:los:sin:tragos:suelo|Un:han:santo:"
               "sido:en:testigo|De:prision|Y:el:una:dolor:"
               "canción:que:triste:me:sin:causaste:dueño|Y:"
               "y:conocí:to':tus:lo:ojos:que:negros|Y:hiciste"
               ":ahora:conmigo|Un:sí:infeliz:que:en:no:el:"
               "puedo:amor,:vivir:que:sin:aun:ellos:no:yo|"
               "Le:te:pido:supera|Que:al:ahora:cielo:camina"
               ":solo:solo:un:sin:deseo|Que:nadie:en:por:tus"
               ":todas:ojos:las:yo:aceras|Preguntándole:pueda"
               ":a:vivir|He:Dios:recorrido:si:el:en:mundo:verdad"
               ":entero|te:el:vengo:amor:a:existe|:decir|")

#make the list from the string
lyrics = lyrics_string.split(':')

song1=[]
song2=[]
song3=[]
song4=[]

#One loop to split this into two strings
for i in range(0,len(lyrics),2):
    song1.append(lyrics[i])
    song2.append(lyrics[i+1])

#Print the songs
song1_print = ' '.join(song1)
song1_print = song1_print.replace('|','\n')
print(song1_print.strip())

print('\n')
song2_print = ' '.join(song2)
song2_print = song2_print.replace('|','\n')
print(song2_print.strip())

#Find common words in the songs
for j in range(0,len(song1),1):
    try:
        if song1[j] in song2:
            if song1[j] not in song3:
                song3.append(song1[j])
    except:
        continue

#Print the words
print('\n\nWords that are in both songs: ')

for k in range(len(song3)):
    print(song3[k])

input('\nPress enter to close program')
