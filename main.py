#filtering the names by category and/or gender
#(ideally) a compile function to spit out a whole prompt
 
import hikari
import lightbulb
import yuyo
import random
import pandas as pd
import list
char_list = list.characters
tropes_list = list.tropes
words_list = list.words
import discordtoken
token = discordtoken.token 

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


#checks bot is online
@bot.command
@lightbulb.command('ping', 'ping pong', hidden=True)
@lightbulb.implements(lightbulb.SlashCommand)
async def ping(ctx):
    await ctx.respond("Pong!")

#also checks bot is online, but fun!
@bot.command
@lightbulb.command('boo', 'scares bot', hidden=True)
@lightbulb.implements(lightbulb.SlashCommand)
async def boo(ctx):
    await ctx.respond("Ahhhhh! 😱")



#prompt functions:
def cz_characters(number):
    chosen_char = []
    while len(chosen_char) < number:
        char = random.choice(char_list)
        if char not in chosen_char:
            chosen_char.append(char)
        else:
            pass
    return " \n* ".join(chosen_char)

def cz_length(length_choice):
    if length_choice == 'short':
        return f"{random.randint(150, 500)} words. "
    elif length_choice == 'medium':
        return f"{random.randint(500, 900)} words. "
    elif length_choice == 'long':
        return f"{random.randint(900, 2000)} words. "
    else:
        return f"{random.randint(150, 2000)} words. "



def cz_tropes(number):
    chosen_tropes = []
    while len(chosen_tropes) < number:
        chosen_tropes.append(random.choice(tropes_list))
    return " \n* ".join(chosen_tropes)

#default 3 for CZ, update with prompting later
def cz_words():
    chosen_words = []
    for i in range(3):
        chosen_words.append(random.choice(words_list))
    return " \n* ".join(chosen_words)

@bot.command
@lightbulb.command('prompt', 'generate prompt')
@lightbulb.implements(lightbulb.SlashCommandGroup)
async def prompt(ctx):
    pass

#basic character prompt
@prompt.child
@lightbulb.option('number', 'number of characters', type=int, max_value=6, default=2)
@lightbulb.command('character', 'prompt characters')
@lightbulb.implements(lightbulb.SlashSubCommand)
async def character_prompt(ctx):
    characters = cz_characters(ctx.options.number)
    await ctx.respond("Your characters are: " + ", ".join(characters))

#sentence prompt, not for CZ
@prompt.child
@lightbulb.command('sentence', 'prompt a starting sentence')
@lightbulb.implements(lightbulb.SlashSubCommand)
async def sentence_prompt(ctx):
    await ctx.respond(f'Your sentence is: \n > *"{random.choice(sentences)}"*')

#tropes prompt, CZ
@prompt.child
@lightbulb.option('number', 'number of tropes', type=int, max_value=6, default=2)
@lightbulb.command('trope', 'generates two tropes')
@lightbulb.implements(lightbulb.SlashSubCommand)
async def trope_prompt(ctx):
    tropes = cz_tropes(ctx.options.number)
    await ctx.respond(f"Your tropes are: \n * " + tropes)


#word prompt, CZ default = 3
@prompt.child
@lightbulb.command('words', 'three randomly generated words')
@lightbulb.implements(lightbulb.SlashSubCommand)
async def word_prompt(ctx):
    chosen_words = cz_words()
    await ctx.respond("Use these words to prompt your writing: \n* " + chosen_words)



# word count bonus challenge (random number generator
# limit to short 150-500/medium 500-900/long 900-2000, then random number no rounding within those parameters)
@prompt.child
@lightbulb.option('length', 'length request', choices=['short', 'medium', 'long', 'any'])
@lightbulb.command('wc', 'set a word count limit')
@lightbulb.implements(lightbulb.SlashSubCommand)
async def length_prompt(ctx):
    length = cz_length(ctx.options.length)
    await ctx.respond("Write a fic with exactly " + length)


# CZ prompt. Needs: user, short/med/long (optional), maybe filtering?
# signup includes: UN, 2 characters, 2 tropes, 3 words 
@bot.command
@lightbulb.option('user', 'who is this prompt for?', type=str)
@lightbulb.option('length', 'bonus length request', choices=['short', 'medium', 'long'], required=False)
@lightbulb.option('categories', 'characters and/or tropes', choices=['characters', 'tropes', 'both'], required=False)
@lightbulb.command('signup', 'full CZ prompt')
@lightbulb.implements(lightbulb.SlashCommand)
async def cz_prompt(ctx):
    user = ctx.options.user
    
    if ctx.options.length == None:
        length = "Your fic must be within the fest limits of 150-7000 words. "
    else:
        length = "Your fic must be *exactly* " + cz_length(ctx.options.length)

    if ctx.options.categories == 'characters':
        characters = cz_characters(2)
        tropes = "You have opted for No Tropes. "
    elif ctx.options.categories == 'tropes':
        tropes = cz_tropes(2)
        characters = "You have opted for No Characters. "
    elif ctx.options.categories == 'both':
        characters = cz_characters(2)
        tropes = cz_tropes(2)
    else:
        characters = "You have opted for No Characters. "
        tropes = "You have opted for No Tropes. "
    words = cz_words()


    await ctx.respond(f'''Hi {user}!
    Here are your selections for **Comfort Zone Fest**: 
    \n### Tropes:
    * {tropes}
    \n### Characters:
    * {characters}
    
    \n### Prompts:
    * {words}
    
    \n### Length:
    * {length}

    As a reminder, you must use at least one (1) assigned character or trope. If you opted into a word count target, your goal is to hit that word count exactly. If you have any questions, or are uncomfortable with any of the selections, please don't hesitate to let us know. Thank you, and happy writing!''')






bot.run() 