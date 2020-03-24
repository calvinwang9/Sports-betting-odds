# Sports betting odds
This project revolves sports betting strategies such as matched betting and promo arbitraging, which I developed an interest in and wrote a program to help automate parts of the process. Using an api to grab the best odds from various Australian bookmakers (the-odds-api.com), I calculate the turnover rate, market margin, and promotion return multiplier (bookmaker specific).

main -> sportsbetting.py

## Turnover
Calculates a risk-free profit in turning over bonus bets into withdrawable cash, represented as a percentage of the bonus bet. While most games average 40-60%, I calculated the highest turnover percentage achievable with the different odds across bookmakers for each upcoming game to get an average 80%+ turnover, as well as calculating how much cash to bet on one side given a fixed bonus bet on the other. Note that bonus bet turnovers only work on sports with two-way markets (no draws), for example NBA, AFL, NRL.

## Margin
Calculates the market margin or edge taken by bookmakers on every game. Assuming an equal split of the margin between either side, we can adjust the bookmaker odds to find a rough estimate of the actual percentage odds for either side to win or lose. Bookmakers average around a 5% margin individually, and due to odds discrepencies the market margin is often smaller. A negative margin indicates there can be an arbitrage profit to be made. Using actual percentage odds, we can thus calculate an EV of betting on one side expressed as a percentage of the bet size.

## Promo
Calculates the maximum loss and/or return multiplier for bookmaker specific promotions that represent a profitable opportunity with positive EV. This involves placing a bet on both sides that would result in the same loss no matter which side won, but when a promotion on either bookmaker occurs, we can achieve a significant profit represented as a return multiple of the maximum loss. This also takes into account the limits of these promotions and attempts to maximise the profits with minimal potential loss. 

