from webex_bot.models.command import Command
from webex_bot.models.response import Response


class gpt(Command):
    
        def __init__(self):
            super().__init__()
            
        def execute(self, message, attachement_actions, activity):
            return("Hello World!")