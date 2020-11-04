def pig_latin(s):
    temp = ''
    first_char = True
    return_word = ''
    count = 0
    punc = ''
    
    for i in s:
        if first_char == True:     #checking if i is the first character of a word and
            temp += i              #keeping it seperate to be added later
            first_char = False
            count += 1
        
        else:
            if i.isalpha():          #all other alphabetic characters added to the return string
                return_word += i
                count += 1
                
            elif not i.isalpha() and not i.isspace(): #punctuation characters kept seperate to be added later
                punc += i
                count += 1
                
            elif i.isspace(): #when a space is encountered the pig-latin word is put together:              
                return_word = return_word + temp + 'ay' + punc #putting the first character at the end + 'ay' 
                return_word += ' ' #have to add the space because it hasn't been added yet/      + punctuation
                temp = ''    #resetting variables and counters
                first_char = True
                count += 1
                punc = ''
               
        if count == len(s): #when the end of the string is reached the pig-latin word is put together:
            if not i.isalpha() and not i.isspace(): #have to check if the last charcter is punctuation
                return_word += i                    #or else you could end up with a '!ay' situation
            
            else: #if the last character isn't punctuation, the word gets put together as normal:
                return_word = return_word + temp + 'ay' + punc
                
          
    return return_word


            
print(pig_latin('What the Fuck this program isnt working Hello Pussies, I am Matt'))        



    


        