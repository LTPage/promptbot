#import hikari
import lightbulb
import random
import pandas as pd
character_list = pd.read_csv('characters.csv')
import discordtoken
token = discordtoken.token 
#first_line = pd.read_csv('first_Line.csv')
#token = token.txt 


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

sentences = ["She found it amongst her mother's possessions.",
"He had enjoyed ten years of being totally irresponsible.",
"In hindsight, she shouldn't have bought the red one.",
"His father had always said it would be the death of him.",
"Why should I get away with it?",
"No one expected her to be the first.",
"There was something soothing about nights like this.",
"She knew he was in love with her; that's what made it so easy.",
"It was lucky no one ever asked why he'd done it; he wasn't sure he had an answer.",
"It's true my husband's death was tragic. It's also true that it was necessary.",
"There was something off about him.",
"Somehow, amidst all this darkness, there is still hope.",
"If you had asked him a year ago if he'd ever thought he'd be on the run from the Aurors, he'd have thought you were mad -  and now here he was, running like his arse was on fire.",
"They were definitely just friends.",
"So, a witch, a werewolf, and an accountant walk into a bar - and no, it's not a joke: it was Tuesday.",
"What are you doing here?",
"First of all, how dare you?",
"He hadn't actually expected it to work.",
"It only took a moment.",
"It's a long story, but what you need to know now is that I didn't get arrested.",
"Don't you dare touch it!",
"What you are going to do is— calmly— open the door and say good morning.", 
"She had no idea she was about to experience the longest day in living record.", 
"What do you mean he got out?", 
"If she asked one more time, he was going to lose it.",
"He had one more chance to tell the truth before she found out, regardless of what he wanted."
]


bot = lightbulb.BotApp(
    token=token, 
    #default_enabled_guilds=(996189253786677308)
    )

#@bot.listen(hikari.GuildMessageCreateEvent)
#async def print_message(event):
    #print(event.content)

#@bot.listen(hikari.StartedEvent)
#async def startMessage(event):
    #print('Bot has started!')

@bot.command
@lightbulb.command('ping', 'ping pong', hidden=True)
@lightbulb.implements(lightbulb.SlashCommand)
async def ping(ctx):
    await ctx.respond("Pong!")




@bot.command
@lightbulb.command('prompt', 'generate prompt')
@lightbulb.implements(lightbulb.SlashCommandGroup)
async def prompt(ctx):
    pass


@prompt.child
@lightbulb.option('number', 'number of characters', type=int)
@lightbulb.command('character', 'prompt characters')
@lightbulb.implements(lightbulb.SlashSubCommand)
async def character_prompt(ctx):
    chosen_char = []
    if ctx.options.number > 6:
        await ctx.respond("Too many characters! Try a number less than 5. You can always add more yourself!")
    else: 
        while len(chosen_char) < ctx.options.number:
            char = random.choice(characters)
            if char not in chosen_char:
                chosen_char.append(char)
            else:
                pass
     
        await ctx.respond("Your characters are: " + ", ".join(chosen_char))

@prompt.child
@lightbulb.command('sentence', 'prompt a starting sentence')
@lightbulb.implements(lightbulb.SlashSubCommand)
async def sentence_prompt(ctx):
    await ctx.respond(f'Your sentence is: \n > *"{random.choice(sentences)}"*')



#@bot.command
#@lightbulb.command('prompt', 'prompt a character')
#async def prompt(ctx):
#    response = random.choice(characters)
#    await ctx.send(response)

bot.run() 