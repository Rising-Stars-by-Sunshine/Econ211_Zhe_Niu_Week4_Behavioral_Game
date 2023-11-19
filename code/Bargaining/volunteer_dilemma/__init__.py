
from otree.api import *
c = cu

doc = "\nEach player decides if to free ride or to volunteer from which all will\nbenefit.\nSee: Diekmann, A. (1985). Volunteer's dilemma. Journal of Conflict\nResolution, 605-610.\n"
class C(BaseConstants):
    NAME_IN_URL = 'volunteer_dilemma'
    PLAYERS_PER_GROUP = 3
    NUM_ROUNDS = 1
    NUM_OTHER_PLAYERS = 2
    GENERAL_BENEFIT = cu(100)
    VOLUNTEER_COST = cu(40)
    INSTRUCTIONS_TEMPLATE = 'volunteer_dilemma/instructions.html'
class Subsession(BaseSubsession):
    pass
class Group(BaseGroup):
    num_volunteers = models.IntegerField()
def set_payoffs(group: Group):
    players = group.get_players()
    group.num_volunteers = sum([p.volunteer for p in players])
    if group.num_volunteers > 0:
        baseline_amount = C.GENERAL_BENEFIT
    else:
        baseline_amount = cu(0)
    for p in players:
        p.payoff = baseline_amount
        if p.volunteer:
            p.payoff -= C.VOLUNTEER_COST
class Player(BasePlayer):
    volunteer = models.BooleanField(doc='Whether player volunteers', label='Do you wish to volunteer')
class Introduction(Page):
    form_model = 'player'
class Decision(Page):
    form_model = 'player'
    form_fields = ['volunteer']
class ResultsWaitPage(WaitPage):
    after_all_players_arrive = set_payoffs
class Results(Page):
    form_model = 'player'
page_sequence = [Introduction, Decision, ResultsWaitPage, Results]