from otree.api import *


doc = """
Your app description
"""

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

df["q1_text"] = "No answer"
df.loc[(df["capital"]==1),"q1_text"] = "Preserving my investment capital is not important to me at all."
df.loc[(df["capital"]==2),"q1_text"] = "Preserving my investment capital is rather not important to me."
df.loc[(df["capital"]==3),"q1_text"] = "Preserving my investment capital is rather important to me."
df.loc[(df["capital"]==4),"q1_text"] = "Preserving my investment capital is very important to me."
df["q2_text"] = "No answer"
df.loc[(df["returns"]==1),"q2_text"] = "To increase my return, it is much more important to me to take risks than to get a reliable return."
df.loc[(df["returns"]==2),"q2_text"] = "To increase my return, it is somewhat more important to me to take risks than to get a reliable return."
df.loc[(df["returns"]==3),"q2_text"] = "To increase my return, it somewhat more important to me to get a reliable return than to take risks."
df.loc[(df["returns"]==4),"q2_text"] = "To increase my return, it is much more important to me to get a reliable return than to take risks."
df["q3_text"] = "No answer"
df.loc[(df["losses"]==1),"q3_text"] = "Small losses do not make me nervous at all."
df.loc[(df["losses"]==2),"q3_text"] = "Small losses do not really make me nervous."
df.loc[(df["losses"]==3),"q3_text"] = "Even the smallest losses make me somewhat nervous."
df.loc[(df["losses"]==4),"q3_text"] = "Even the smallest losses make me very nervous."
df["q4_text"] = "No answer"
df.loc[(df["risks"]==1),"q4_text"] = "Financial risks are not at all appealing."
df.loc[(df["risks"]==2),"q4_text"] = "Financial risks are rather not appealing."
df.loc[(df["risks"]==3),"q4_text"] = "Financial risks are appealing."
df.loc[(df["risks"]==4),"q4_text"] = "Financial risks are very appealing."
df["q5_text"] = "No answer"
df.loc[(df["chance"]==1),"q5_text"] = "I am not at all willing to accept the loss of my assets if it means I also have the chance to increase my gains."
df.loc[(df["chance"]==2),"q5_text"] = "I am rather not willing to accept the loss of my assets if it means I also have the chance to increase my gains."
df.loc[(df["chance"]==3),"q5_text"] = "I am rather willing to accept the loss of my assets if it means I also have the chance to increase my gains."
df.loc[(df["chance"]==4),"q5_text"] = "I am very willing to accept the loss of my assets if it means I also have the chance to increase my gains."

df["q1_short"] = "No answer"
df.loc[(df["capital"]==1),"q1_short"] = "not at all."
df.loc[(df["capital"]==2),"q1_short"] = "only a bit."
df.loc[(df["capital"]==3),"q1_short"] = "."
df.loc[(df["capital"]==4),"q1_short"] = "very much."
df["q2_short"] = "No answer"
df.loc[(df["returns"]==1),"q2_short"] = "not at all."
df.loc[(df["returns"]==2),"q2_short"] = "rather not."
df.loc[(df["returns"]==3),"q2_short"] = "."
df.loc[(df["returns"]==4),"q2_short"] = "very much."
df["q3_short"] = "No answer"
df.loc[(df["losses"]==1),"q3_short"] = "not at all."
df.loc[(df["losses"]==2),"q3_short"] = "only a bit."
df.loc[(df["losses"]==3),"q3_short"] = "."
df.loc[(df["losses"]==4),"q3_short"] = "very much."
df["q4_short"] = "No answer"
df.loc[(df["risks"]==1),"q4_short"] = "not at all."
df.loc[(df["risks"]==2),"q4_short"] = "only a bit."
df.loc[(df["risks"]==3),"q4_short"] = "."
df.loc[(df["risks"]==4),"q4_short"] = "very much."
df["q5_short"] = "No answer"
df.loc[(df["chance"]==1),"q5_short"] = "not at all."
df.loc[(df["chance"]==2),"q5_short"] = "only a bit."
df.loc[(df["chance"]==3),"q5_short"] = "."
df.loc[(df["chance"]==4),"q5_short"] = "very much."

choices = pd.read_excel('_static/global/choices.xlsx', engine = 'openpyxl') # can also index sheet by name or fetch all sheets
countries = choices['country'][0:197].tolist()
years = choices['Jahr'][0:101].tolist()
years = [int(year) for year in years]
nationalities = choices['nationality'][0:199].tolist()


class C(BaseConstants):
    NAME_IN_URL = 'proval'
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
    

class evaluation_en_3(Page):
    form_model = 'player'
    form_fields = ['evaluation', 'offer']

    @staticmethod
    def vars_for_template(player: Player):
        participant = player.participant
        print(participant.profiles)
        print(player.round_number)
        profile = participant.profiles[player.round_number-1]
        prolificid_client = profile["prolificid"]
        nationality = profile["nationality"]
        name = profile["name"]
        introduction = profile["intro"]
        religion = profile["religion"]
        profession = profile["profession"]
        gender = profile["gender"]
        income = profile["income"]
        q1_text = profile["q1_text"]
        q2_text = profile["q2_text"]
        q3_text = profile["q3_text"]
        q4_text = profile["q4_text"]
        q5_text = profile["q5_text"]
        q1_short = profile["q1_short"]
        q2_short = profile["q2_short"]
        q3_short = profile["q3_short"]
        q4_short = profile["q4_short"]
        q5_short = profile["q5_short"]
        education_uni = profile["uni"]
        occupation = profile["occupation"]
        occupation_text = profile["occupation_text"]
        fieldofstudy = profile["fieldofstudy"]
        risktoolresult = int(round(profile["riskyshare"]*100, 0))
        age = profile["age"]
        party = profile["party"]
        q1 = profile["capital"]
        q2 = profile["returns"]
        q3 = profile["losses"]
        q4 = profile["risks"]
        q5 = profile["chance"]
        return {
            'variant': participant.variant,
            'profile': profile,
            'name':name,
            'nationality': nationality,
            'profession': profession,
            'prolificid_client': prolificid_client,
            'q1_text': q1_text,
            'q2_text': q2_text,
            'q3_text': q3_text,
            'q4_text': q4_text,
            'q5_text': q5_text,
            'q1_short': q1_short,
            'q2_short': q2_short,
            'q3_short': q3_short,
            'q4_short': q4_short,
            'q5_short': q5_short,
            'gender': gender,
            'education_uni': education_uni,
            'nationality': nationality,
            'income': income,
            'religion': religion,
            'introduction': introduction,
            'occupation': occupation,
            'occupation_text': occupation_text,
            'fieldofstudy' : fieldofstudy,
            'risktoolresult': risktoolresult,
            'age': age, 
            'party': party,
            'picpath': 'profilepics/' + prolificid_client + '.png',
            'scalepath1': 'scales/scale' + str(q1) + '.png',
            'scalepath2': 'scales/scale' + str(q2) + '.png',
            'scalepath3': 'scales/scale' + str(q3) + '.png',
            'scalepath4': 'scales/scale' + str(q4) + '.png',
            'scalepath5': 'scales/scale' + str(q5) + '.png',
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
    evaluation_en_3,
    demos_en,
#    groupy_en,
    end_en
                   ]

