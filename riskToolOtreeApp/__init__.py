from otree.api import *


doc = """
Your app description
"""


class C(BaseConstants):
    NAME_IN_URL = 'riskToolOtreeApp'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1
    Auszahlungsfaktor = 100
    budget = 10000
    budget_string = "10.000"
    Anlagehorizont = 10


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    finalDecisionValue = models.StringField()
    pass


# PAGES

class risk_tool_intro_de(Page):
    
    @staticmethod
    def vars_for_template(player):
        return {
            'Auszahlung': int(C.budget / C.Auszahlungsfaktor),
        }
    
class risk_tool_payment_de(Page):
    
    @staticmethod
    def vars_for_template(player):
        return {
            'Auszahlung': int(C.budget / C.Auszahlungsfaktor),
        }

class risk_tool_de(Page):
    @staticmethod
    def live_method(player, data):
        player.finalDecisionValue = str(data['final-decision-value'])
    pass





page_sequence = [
                risk_tool_intro_de,
                risk_tool_payment_de,
                risk_tool_de,
                ]
