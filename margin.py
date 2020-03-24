
def margin(odds1, odds2):
    percent_win = 1/odds2
    percent_lose = 1/odds1
    margin = percent_win+percent_lose-1
    actual_win = percent_win - 0.5*margin
    actual_lose = percent_lose - 0.5*margin
    ev = 100*(actual_win*(odds2-1) - actual_lose*1)
    
#    print('bookmaker odds to win:\t' + str(round(percent_win*100,2)) + '%')
#    print('bookmaker odds to lose:\t'+ str(round(percent_lose*100,2)) + '%')
    print('margin = ' + str(round((margin)*100, 2)) + '%')
    print('actual odds to win:\t' + str(round(actual_win*100, 2)) + '%')
    print('actual odds to lose:\t'+ str(round(actual_lose*100, 2)) + '%')
    print('EV of betting on '+str(odds2)+' odds = ' + str(round(ev, 2)) + '%')
    
    return margin

margin(4, 1.39)


    
    