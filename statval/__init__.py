from otree.api import *

import pandas as pd
import random
import numpy as np

df = pd.read_excel('_static/global/profiles.xlsx', keep_default_na=False, engine='openpyxl')
df["gender"] = df["gender"].astype(str)
df["nationality"] = df["nationality"].astype(str)
df["religion"] = df["religion"].astype(str)
df["uni"] = df["uni"].astype(str)
df["profession"] = df["profession"].astype(str)
df["intro"] = df["intro"].astype(str)
df["age"] = df["age"].astype(int)
#df["riskgroup"] = df["riskgroup"].astype(int)
#df["riskgroup_text"] = df["riskgroup_text"].astype(str)
df["prolificid"] = df["prolificid"].astype(str)
df["income"] = df["income"].astype(str)
df["party"] = df["party"].astype(str)
df["occupation_text"] = df["occupation_text"].astype(str)


choices = pd.read_excel('_static/global/choices.xlsx', engine = 'openpyxl') # can also index sheet by name or fetch all sheets
countries = choices['country'][0:197].tolist()
years = choices['Jahr'][0:101].tolist()
years = [int(year) for year in years]
nationalities = choices['nationality'][0:199].tolist()


class C(BaseConstants):
    NAME_IN_URL = 'statval'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 10
    bonus = cu(2)
    fixedfee = cu(1)
    numberselections = 5
    Auszahlungsfaktor = 100
    budget = 10000
    budget_string = "10.000"
    Anlagehorizont = 5
    groupybudget = cu(1)


class Subsession(BaseSubsession):
    pass


def creating_session(subsession: Subsession):
    global df  # tell Python to use the top-level df
    import itertools
    variant = itertools.cycle(['a']) 
    groups = itertools.cycle(['circle', 'triangle',])
    if subsession.round_number == 1:
        df = df.copy()
        rng = np.random.default_rng(42)
        def reset_pool():
            return df.sample(frac=1, random_state=rng.integers(1e9)).reset_index(drop=True)

        # initialize the pool of "unused" profiles
        available = reset_pool()
        for p in subsession.get_players():
            if 'variant' in subsession.session.config:
                p.participant.variant = subsession.session.config['variant']
            else:
                p.participant.variant = next(variant)
            p.participant.group = next(groups)
            profiles = []

            # if not enough left for a full 10, reset
            if len(available) < 10:
                available = reset_pool()

            # draw 2 from each core category
            def draw_from(cat_mask_func, n=2):
                nonlocal available
                subset = available[cat_mask_func(available)]  # compute mask on available
                if len(subset) < n:
                    available = reset_pool()
                    subset = available[cat_mask_func(available)]
                chosen = subset.sample(n=n, random_state=rng.integers(1e9))
                available = available.drop(chosen.index)
                return chosen

            black_male   = draw_from(lambda df: (df.gender=="male") & (df.race=="Black or African American"))
            black_female = draw_from(lambda df: (df.gender=="female") & (df.race=="Black or African American"))
            white_male   = draw_from(lambda df: (df.gender=="male") & (df.race=="White"))
            white_female = draw_from(lambda df: (df.gender=="female") & (df.race=="White"))

            # now draw 2 random from what's left
            if len(available) < 2:
                available = reset_pool()
            random_two = available.sample(n=2, random_state=rng.integers(1e9))
            available = available.drop(random_two.index)

            # shuffle the 10 profiles
            selected_profiles_df = pd.concat([
                black_male, black_female, white_male, white_female, random_two
            ]).sample(frac=1, random_state=rng.integers(1e9))

            p.participant.profiles = selected_profiles_df.to_dict(orient="records")
            for i, profile in enumerate(p.participant.profiles,1):
                print(f"Profile {i}: {profile['gender']},{profile['race']}")



class Group(BaseGroup):
    pass

class Player(BasePlayer):
    consent = models.BooleanField()
    riskgroup_example = models.IntegerField(blank=True)
    evaluation = models.IntegerField(blank=True, min=-50, max=50, verbose_name="""""")
#    evaluation_certainty = models.IntegerField(blank=True,
#                                               choices=[[1, "very confident"],
#                                                        [2, "rather confident"],
#                                                        [3, "rather not confident"], 
#                                                        [4, "not at all confident"]],
#                                        verbose_name="""""")
    prolific_id = models.StringField()
    screener = models.StringField()
#    groupy = models.FloatField()


    offer = models.CharField()
    age = models.IntegerField(verbose_name='How old are you?')
    gender = models.CharField(initial=None,
                              choices=['female', 'male', 'non-binary'],
                              verbose_name='What is your gender?',
                              widget=widgets.RadioSelect())
    nationality = models.CharField(initial=None,
                                    choices=nationalities,
                                    verbose_name='What is your nationality? <br> <i>(In case you have multiple nationalities, indicate the one you identify with the most.)</i>')

    education_uni =  models.CharField(initial=None,
                                      verbose_name='What is your highest level of education?',
                                      choices=['Bachelor', 'Master', 'PhD', 'None', 'Other'],)
    fieldofstudy = models.CharField(initial=None,
                                    blank = True,
                                    verbose_name='What do you study?',
                                    )
    income = models.CharField(initial=None,
                                    blank = True,
                                    verbose_name='What is your monthly net income?',
                                    choices = ['less than $1000', '$1000-$1999', '$2000-$2999', '$3000-$3999', 'more than $4000']
                                    )
    occupation=models.IntegerField(initial=None)
    profession = models.CharField(initial = None,
                                  blank = True,
                                  verbose_name='What is your profession?')

    religion = models.CharField(initial = None,
                                verbose_name = 'Which religious group do you identify with?',
                                choices = ['Catholic', 'Protestant', 'Orthodox',
                                           'Not religious', 'Muslim', 'Buddhist', 'Jewish',
                                           'Hindu', 'Other'],)
    party = models.CharField(initial = None,
                                verbose_name = 'Which political party would you vote for if there were elections today?',
                                choices = ['Democrats', 'Republicans', 'Independent', 'I dont vote'],)

    distract = models.CharField(initial = None,
                                verbose_name = 'Please tell us: Can we safely analyze your data, or were you distracted by any influences during the survey? <i>(Your answer to this question will have no impact on your payment.)</i>',
                                choices = [
                                    [1, 'I was very attentive and not distracted at all.'],
                                    [2, 'I was mostly attentive and barely distracted.'],
                                    [3, 'I was not very attentive and somewhat distracted.'],
                                    [4, 'I was not attentive at all and quite distracted.'],
                                    ],)
    attention_check = models.CharField(
        initial=None,
        choices=[
            ['false1', 'blue'], ['true', 'orange'], ['false2', 'red'], ['false3', 'yellow'], ['false4', 'green'], ['false5', 'black']
        ],
        label = 'It is important to us that you pay attention. Please click on the second option from the top in the following list.',
        widget=widgets.RadioSelect(),
    )
    race = models.CharField(initial = None,
                            verbose_name = "What is your race/ethnicity?",
                            choices = ["Hispanic or Latin", "Asian", "White", "Black or African American", "American Indian", "other / prefer not to answer"])
    

class consent_en(Page):
    form_model = 'player'
    form_fields = ['consent']

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1
    
    @staticmethod
    def before_next_page(player, timeout_happened):
        # player.prolific_id = player.participant.label
        player.prolific_id = player.participant.label


class start_en(Page):
    form_model = 'player'
    form_fields = ['screener']

        
    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1


class instructions_en(Page):
    @staticmethod
    def vars_for_template(player: Player):
        participant = player.participant
        return {
            'variant': participant.variant,
        }

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1
    

class intro_evaluation_en(Page):
    form_model = 'player'
    form_fields = ['evaluation', 'offer']

    @staticmethod
    def vars_for_template(player: Player):
        participant = player.participant
        print(participant.profiles)
        print(player.round_number)
        profile = participant.profiles[player.round_number-1]
        prolificid_client = profile["prolificid"]
        name = profile["name"]
        introduction = profile["intro"]
        return {
            'variant': participant.variant,
            'profile': profile,
            'name': name,
            'prolificid_client': prolificid_client,
            'introduction': introduction,
            'round_number': player.round_number,
        }
    
    
class demos_en(Page):
    form_model = 'player'
    form_fields = [#'name',
        'age', 'gender', 'profession', 'fieldofstudy', 'occupation', 'nationality', 'income', 'race',
                 'education_uni','religion', 'party', 'distract', 'attention_check']

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == C.NUM_ROUNDS
    
    
#class groupy_en(Page):
#    form_model = 'player'
#    form_fields = ['groupy']

#    @staticmethod
#    def vars_for_template(player: Player):
#        participant = player.participant
#        return {
#            'group': participant.group,
#        }

#    @staticmethod
#    def error_message(player, values):
#        if values['groupy'] is None:
#            return 'Please click on the slider to make your decision.'
#        return None
    
#    @staticmethod
#    def is_displayed(player: Player):
#        return player.round_number == C.NUM_ROUNDS
    
class end_en(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == C.NUM_ROUNDS

    @staticmethod
    def js_vars(player: Player):
        return dict(
            prolific_id= player.participant.label
        )
    
page_sequence = [
    consent_en,
    start_en,
    instructions_en,
    intro_evaluation_en,
    demos_en,
#    groupy_en,
    end_en
                   ]

