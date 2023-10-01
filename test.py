import random
#import list
import pandas as pd
character_list = pd.read_csv('characters.csv')

#print(character_list.head)


characters = ['Any Death Eater',
'Any Founder',
'Any Gryffindor',
'Any Hogwarts Ghost',
'Any Hufflepuff',
'Any Ministry Employee',
'Any Muggle',
'Any Order Member',
'Any Professor',
'Any Quidditch Player',
'Any Ravenclaw',
'Any Slytherin',
'Albus Severus Potter',
'Hugo Weasley',
'James Sirius Potter',
'Lily Luna Potter',
'Rose Weasley',
'Scorpius Malfoy',
'Teddy Lupin',
'Victoire Weasley',
'Andromeda Tonks',
'Arthur Weasley',
'Barty Crouch Jr',
'Bellatrix Lestrange',
'Cornelius Fudge',
'Dolores Umbridge',
'Dorcas Meadowes',
'Fenrir Greyback',
'James Potter',
'Regulus Black',
'Kingsley Shacklebolt',
'Lily Evans Potter',
'Lucius Malfoy',
'Marlene McKinnon',
'Mary MacDonald',
'Molly Weasley',
'Narcissa Malfoy',
'Peter Pettigrew',
'Petunia Dursley',
'Rabastan Lestrange',
'Remus Lupin',
'Rita Skeeter',
'Rodolphus Lestrange',
'Rubeus Hagrid',
'Severus Snape',
'Sirius Black',
'Ted Tonks',
'Tom Riddle/Voldemort',
'Vernon Dursley',
'Walburga Black',
'Alicia Spinnet',
'Angelina Johnson',
'Bill Weasley',
'Cedric Diggory',
'Charlie Weasley',
'Cho Chang',
'Colin Creevey',
'Cormac McLaggen',
'Daphne Greengrass',
'Dean Thomas',
'Draco Malfoy',
'Dudley Dursley',
'Fleur Delacour',
'Fred Weasley',
'George Weasley',
'Ginny Weasley',
'Gregory Goyle',
'Hannah Abbott',
'Harry Potter',
'Hermione Granger',
'Katie Bell',
'Lavender Brown',
'Lee Jordan',
'Luna Lovegood',
'Marcus Flint',
'Marietta Edgecombe',
'Neville Longbottom',
'Nymphadora Tonks',
'Oliver Wood',
'Padma Patil',
'Pansy Parkinson',
'Percy Weasley',
'Romilda Vane',
'Ron Weasley',
'Seamus Finnegan',
'Susan Bones',
'Viktor Krum',
'Vincent Crabbe']

def generator(num):
    chosen_char = []
    while len(chosen_char) < num:
        char = random.choice(characters)
        if char not in chosen_char:
            chosen_char.append(char)
        else:
            pass
    return "Your characters are: " + ", ".join(chosen_char)
    # chosen_char

#rslt_df = dataframe[(dataframe['Age'] == 21) &
          #dataframe['Stream'].isin(options)]
#df = df.sample(n=3)
#col_list = df.Courses.values.tolist()
#rslt_df = dataframe.loc[(dataframe['Age'] == 21) &
              #dataframe['Stream'].isin(options)]

def pdgenerator(number, gender, era):
    gender_filter = (character_list['Canon Sex'] == gender) | (character_list['Canon Sex'] == 'Any')
    era_filter = (character_list['Generation'] == era) | (character_list['Generation'] == 'Any')
    filtered_char = character_list[gender_filter & era_filter]
    random_char_list = filtered_char.sample(n=number)
    #filtered_char = character_list.loc[(character_list['Canon Sex'] == gender) & 
        #character_list['Generation'] == 'era']
    print("Your characters are: " + ", ".join(random_char_list['Name'].tolist()))
    #print(random_char_list['Name'])
    #print(filtered_char.head)
    #selected = filtered_char.sample(n=num)
    #chosen_chars = selected.name.values.tolist()
    #return "Your characters are: " + ", ".join(chosen_chars)




#def generator():
    #chosen_char = []
    #for i in range(num):
        #chosen_char.append(random.choice(list))
    #return chosen_char

print(generator(2))
#pdgenerator(3, 'Male', 'Main Series')
#print(pdgenerator(2, 'Male', 'Main Series'))
