

def comeback_calc(odds1, odds2):
    bet_win = 50 # fixed $50 bet on favoured team
    win_payoff = bet_win*odds2 - bet_win
    bet_lose = bet_win/(odds1-1)
    print('$' + str(bet_win) + ' on ' + str(odds2) + ' = ' + str(round(bet_lose, 2)) + ' on ' + str(odds1))
    print('when favoured team wins -> $' + str(round(win_payoff - bet_lose, 2)))
    print('when favoured team loses -> $' + str(bet_lose*(odds1-1) - bet_win))
    print('when favoured team leads by 10 and loses -> $' + str(bet_win) + ' in bonus, minus $' + str(bet_lose*(odds1-1) - bet_win))
    return round(win_payoff - bet_lose, 2)
    
comeback_calc(1.16, 6.5)

#50*(x-1) - 50/(y-1)