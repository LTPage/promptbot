#filtering the names by category and/or gender
#(ideally) a compile function to spit out a whole prompt
 
import hikari
import lightbulb
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
    default_enabled_guilds=(996189253786677308)
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


@bot.command
@lightbulb.command('prompt', 'generate prompt')
@lightbulb.implements(lightbulb.SlashCommandGroup)
async def prompt(ctx):
    pass

#basic character prompt
@prompt.child
@lightbulb.option('number', 'number of characters', type=int)
@lightbulb.command('character', 'prompt characters')
@lightbulb.implements(lightbulb.SlashSubCommand)
async def character_prompt(ctx):
    chosen_char = []
    if ctx.options.number > 6:
        await ctx.respond("Too many characters! Try a number less than 5. You can always add more yourself!")
    # I think there's actually a max limit option for numeric input
    # so this should maybe get updated at some point

    else: 
        while len(chosen_char) < ctx.options.number:
            char = random.choice(char_list)
            if char not in chosen_char:
                chosen_char.append(char)
            else:
                pass
     
        await ctx.respond("Your characters are: " + ", ".join(chosen_char))

#sentence prompt, not for CZ
@prompt.child
@lightbulb.command('sentence', 'prompt a starting sentence')
@lightbulb.implements(lightbulb.SlashSubCommand)
async def sentence_prompt(ctx):
    await ctx.respond(f'Your sentence is: \n > *"{random.choice(sentences)}"*')

#tropes prompt, CZ
@prompt.child
@lightbulb.command('trope', 'generates two tropes')
@lightbulb.implements(lightbulb.SlashSubCommand)
async def trope_prompt(ctx):
    trope1 = random.choice(tropes_list)
    trope2 = random.choice(tropes_list)
    await ctx.respond(f"Your tropes are: \n * {trope1} \n* {trope2}")

#word prompt, CZ default = 3
@prompt.child
@lightbulb.command('words', 'three randomly generated words')
@lightbulb.implements(lightbulb.SlashSubCommand)
async def word_prompt(ctx):
    chosen_words = []
    for i in range(3):
        chosen_words.append(random.choice(words_list))
    await ctx.respond("Use these words to prompt your writing: \n* " + " \n* ".join(chosen_words))

# word count bonus challenge (random number generator
# limit to short 150-500/medium 500-900/long 900-2000, then random number no rounding within those parameters)
@bot.command
@lightbulb.command('wc', 'bonus challenge! set a word count limit')
@lightbulb.implements(lightbulb.SlashCommandGroup)
async def wc(ctx):
    pass

@wc.child
@lightbulb.command('short', 'give me a short fic goal')
@lightbulb.implements(lightbulb.SlashSubCommand)
async def short_fic(ctx):
    await ctx.respond(f"Write a fic with exactly {random.randint(150, 500)} words.")



@wc.child
@lightbulb.command('medium', 'give me a medium fic goal')
@lightbulb.implements(lightbulb.SlashSubCommand)
async def med_fic(ctx):
    await ctx.respond(f"Write a fic with exactly {random.randint(500, 900)} words.")


@wc.child
@lightbulb.command('long', 'give me a long fic goal')
@lightbulb.implements(lightbulb.SlashSubCommand)
async def long_fic(ctx):
    await ctx.respond(f"Write a fic with exactly {random.randint(900, 2000)} words.")


#testing space
@prompt.child
@lightbulb.command('testcharacter', 'prompt characters')
@lightbulb.implements(lightbulb.SlashSubCommand)
async def test_character_prompt(ctx):
    pass
    #await ctx.respond(random.choice(char_list))


#@bot.command
#@lightbulb.command('prompt', 'prompt a character')
#async def prompt(ctx):
#    response = random.choice(characters)
#    await ctx.send(response)

bot.run() 