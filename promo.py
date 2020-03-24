
def tab_sportsbet_promo(odds1, odds2):
    max_tab_double = 40
    bet_win = max_tab_double/(odds2-1)
    bet_lose = bet_win*odds2/odds1
    max_loss = bet_win*odds2 - bet_win - bet_lose
    max_win = bet_win*odds2*2 - bet_win - bet_lose
    print('potential tab bonus = ' + str(round(bet_win*(odds2-1), 2)))
    print('$' + str(round(bet_win, 2)) + ' on ' + str(round(odds2, 2)) + ' | $' + str(round(bet_lose, 2)) + ' on ' + str(odds1))
    print('max loss = ' + str(round(max_loss, 2)))
    print('max win = ' + str(round(max_win, 2)))
    print('potential percent return = ' + str(round(-max_win/max_loss, 2)) + '%')
    
    return max_loss

tab_sportsbet_promo(3.9, 2.34)


def sportsbet_pointsbet_promo(p_odds, s_odds):
    max_sportsbet = 250
    max_pointsbet = 150
    
    bet_p = max_pointsbet
    bet_s = bet_p*p_odds/s_odds
    if bet_s > max_sportsbet:
        bet_s = max_sportsbet
        bet_p = bet_s*s_odds/p_odds
    max_loss = bet_p*p_odds - bet_p - bet_s
    max_win = bet_p*p_odds*2 - bet_p - bet_p
    
    print('$' + str(round(bet_p, 2)) + ' on ' + str(round(p_odds, 2)) + '(p) | $' + str(round(bet_s, 2)) + ' on ' + str(s_odds) + '(s)')
    print('max loss = ' + str(round(max_loss, 2)))
    print('max win = ' + str(round(max_win, 2)))
    print('potential return multiple = ' + str(round(-max_win/max_loss, 2)) + 'x')
    
    return round(-max_win/max_loss, 2)

# pointsbet odds - sportsbet odds
# if same -> bigger odds on the left
#sportsbet_pointsbet_promo(3.5, 1.30)