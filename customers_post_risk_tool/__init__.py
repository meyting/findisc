from otree.api import *


doc = """
Your app description
"""


class C(BaseConstants):
    NAME_IN_URL = 'c3'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1
    budget = 1000

class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    accept = models.BooleanField(blank=False,)


# PAGES

class risk_tool_accept_de(Page):
    pass
#    form_model = 'player'
#    form_fields = ['accept']	

class end_de(Page):
    pass

page_sequence = [
    risk_tool_accept_de,
    end_de
    
                 ]
