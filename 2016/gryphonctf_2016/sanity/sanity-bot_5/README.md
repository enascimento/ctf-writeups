# GryphonCTF_2016: Sanity bot

**Category:** Sanity
**Points:** 5
**Description:**

>Talk to Red Bot on Discord Chat. He is lonely.
Creator - Kelvin Neo (@deathline75)

## Write-up
A simple sanity question. Just inputting `!help` to the discord bot returns

    Red - A multifunction Discord bot by Twentysix

    GCTF:
      flag       Prints a flag to you
    General:
      userinfo   Shows users's informations
      lmgtfy     Creates a lmgtfy link
      urban      Urban Dictionary search
      roll       Rolls random number (between 1 and user choice)
      8          Ask 8 ball a question
      rps        Play rock paper scissors
      serverinfo Shows server's informations
      choose     Chooses between multiple choices.
      poll       Starts/stops a poll
      flip       Flips a coin... or a user.
      stopwatch  Starts/stops stopwatch
    Mod:
      names      Show previous names/nicknames of a user
    Owner:
      version    Shows Red's current version
      info       Shows info about Red
      set        Changes Red's global settings.
      contact    Sends message to the owner
      uptime     Shows Red's uptime
    Trivia:
      trivia     Start a trivia session with the specified list
    ​No Category:
      help       Shows this message.

    Type !help command for more info on a command.
    You can also type !help category for more info on a category

How nice, `!flag` gives us the flag,

Therefore, the flag is `GCTF{r3d_b07_15_fr13ndly}`.
