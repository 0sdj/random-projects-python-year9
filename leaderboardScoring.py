players = {
    "charlie": 0,
    "sigmoid": 0,
    "lukai": 0
}

def scoring():
    print(players)
    print("[SYSTEM] Active players and score matrix loaded...")
    pluzorhuzz = str(input("[INPUT] Select operation >> [1] Decrement Score | [2] Increment Score : "))
    playerchoice = str(input("[TARGET] Enter player ID : "))
    ptschoice = int(input("[VALUE] Inject point value : "))
    if pluzorhuzz == "2":
        players[playerchoice] = players[playerchoice] + ptschoice
    elif pluzorhuzz == "1":
        players[playerchoice] = players[playerchoice] - ptschoice
menuchoice = 0


def mainmenu():
    menuchoice = int(input(
        "=== SCOREBOARD TERMINAL v1.0 ===\n"
        "[1] Display Leaderboard\n"
        "[2] Modify Player Score\n"
        "[3] Terminate Session\n"
        ">> "
    ))
    if menuchoice == 2:
        scoring()
    if menuchoice == 1:
        print(players)
    elif menuchoice == 3:
        print("[SYSTEM] Session terminated. Goodbye.")


while menuchoice != 3:
    mainmenu()