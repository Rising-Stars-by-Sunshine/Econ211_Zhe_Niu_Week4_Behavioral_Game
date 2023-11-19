
from otree.api import *
c = cu

doc = '\nThis bargaining game involves 2 players. Each demands for a portion of some\navailable amount. If the sum of demands is no larger than the available\namount, both players get demanded portions. Otherwise, both get nothing.\n'
class C(BaseConstants):
    NAME_IN_URL = 'bargaining'
    PLAYERS_PER_GROUP = 2
    NUM_ROUNDS = 2
    AMOUNT_SHARED = cu(100)
    INSTRUCTIONS_TEMPLATE = 'bargaining/instructions.html'
class Subsession(BaseSubsession):
    pass
class Group(BaseGroup):
    total_requests = models.CurrencyField()
def set_payoffs(group: Group):
    players = group.get_players()
    group.total_requests = sum([p.request for p in players])
    if group.total_requests <= C.AMOUNT_SHARED:
        for p in players:
            p.payoff = p.request
    else:
        for p in players:
            p.payoff = cu(0)
def my_function(group: Group):
    pass
class Player(BasePlayer):
    request = models.CurrencyField(doc='Amount requested by this player', label='Please enter an amount from 0 to 100', max=C.AMOUNT_SHARED, min=0)
def other_player(player: Player):
    group = player.group
    return player.get_others_in_group()[0]
class Introduction(Page):
    form_model = 'player'
class Request(Page):
    form_model = 'player'
    form_fields = ['request']
class ResultsWaitPage(WaitPage):
    after_all_players_arrive = set_payoffs
class Results(Page):
    form_model = 'player'
    @staticmethod
    def vars_for_template(player: Player):
        return dict(other_player_request=other_player(player).request)
page_sequence = [Introduction, Request, ResultsWaitPage, Results]