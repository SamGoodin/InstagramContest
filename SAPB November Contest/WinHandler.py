import random


class WinHandler:

    def __init__(self, instaContestants, twitterContestants=None):
        self.instaContestants = instaContestants
        self.twitterContestants = twitterContestants
        self.instaWinners = []
        self.twitterWinners = []
        self.winningNums = []
        print("WinHandler.State : Initialized")

    """
    def getTwitterWinners(self, numberOfWinners=3):
        print("WinHandler.Process : Selecting " + str(numberOfWinners) + " random winners from Twitter")
        for x in range(numberOfWinners):
            self.twitterWinners.append(self.twitterContestants[random.randint(0, len(self.twitterWinners))])
        print("WinHandler.Process : Random winners from Twitter selected")
        print("WinHandler.Process : Exporting Twitter winners")
        return self.twitterWinners
    """

    def getInstagramWinners(self, numberOfWinners=3):
        print("WinHandler.Process : Selecting " + str(numberOfWinners) + " random winners from Instagram")
        for x in range(numberOfWinners):
            winNum = random.randint(0, len(self.instaContestants))
            while winNum in self.winningNums:
                winNum = random.randint(0, len(self.instaContestants))
            self.instaWinners.append(self.instaContestants[winNum])
            self.winningNums.append(winNum)
        print("WinHandler.Process : Random winners from Instagram selected")
        print("WinHandler.Process : Exporting Instagram winners")
        return self.instaWinners
