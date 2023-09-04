from gpt import gpt

from webex_bot.webex_bot import WebexBot


# Create a Bot Object
bot = WebexBot(teams_bot_token=('M2FlYjViNzQtODBhZC00NzRmLThmYTQtZTkwOTM5YWZkMDc2ODljOWMxYTYtYmEx_PC75_47fe537e-27d1-4e32-b2dc-2c26e4aa4fa0'))

#clear defaults
bot.commands.clear()

# Add new commands for the bot to listen out for.
bot.add_command(gpt())

#set new default
bot.help_command = gpt()

# Call `run` for the bot to wait for incoming messages.
bot.run()