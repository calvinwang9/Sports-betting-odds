# calculates bonus cash turnover
# set bonus bet = to bonus cash available
# print cash bet to display how much cash needed to bet on other side
# print cash profit
def turnover(odds1, odds2):
    bonus_bet = 100
    bonus_payoff = odds1 * bonus_bet - bonus_bet
    cash_bet = bonus_payoff/odds2
    profit = bonus_payoff - cash_bet
    bonus_turnover = profit/bonus_bet
    print(str(bonus_bet) + ' bonus bet -> $' + str(round(cash_bet, 2)) + ' cash')
    print('profit = ' + str(profit))
    return bonus_turnover

#def turnover(odds1, odds2):
#    return (odds1 - 1) * (odds2 - 1) / odds2

print(turnover(8, 1.15))




