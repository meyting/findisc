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
    clickstream = models.StringField(blank=True)
    risky_share_end = models.FloatField()


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

class risk_tool(Page):
    form_model = 'player'
    form_fields = ['risky_share_end','clickstream']

    @staticmethod
    def js_vars(player):
        return dict(
            risky_share_start=0.1,      # 0.0 - 1.0
            draws=0,                  # 0 - 1000
            y_axis='draws',                # 'draws' | 'bins' | 'fixed'
            y_axis_fixed_value=30        # 0 - 1000
        )




page_sequence = [
                risk_tool_intro_de,
                risk_tool_payment_de,
                risk_tool,
                ]
