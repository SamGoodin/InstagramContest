import random


class WinHandler:

    def __init__(self, instaContestants):
        self.instaContestants = instaContestants
        self.instaWinners = []
        self.waitlistWinners = []
        self.winningNums = []
        print("WinHandler.State : Initialized")

    def getInstagramWinners(self, numberOfWinners=25, numberOfWaitlist=10):
        print("WinHandler.Process : Selecting " + str(numberOfWinners) + " random winners from Instagram")
        winNum = random.randint(0, len(self.instaContestants))
        for x in range(numberOfWinners):
            while winNum in self.winningNums:
                winNum = random.randint(0, len(self.instaContestants))
            self.instaWinners.append(self.instaContestants[winNum])
            self.winningNums.append(winNum)
        print("WinHandler.Process : Random winners from Instagram selected")
        print("WinHandler.Process : Selecting " + str(numberOfWaitlist) + " random backup winners from Instagram")
        for x in range(numberOfWaitlist):
            while winNum in self.winningNums:
                winNum = random.randint(0, len(self.instaContestants))
            self.waitlistWinners.append(self.instaContestants[winNum])
            self.winningNums.append(winNum)
        print("WinHandler.Process : Random backup winners from Instagram selected")
        print("WinHandler.Process : Double checking to make sure no one won twice")
        self.doubleCheckWinners()
        print("WinHandler.Process : Double check complete")
        print("WinHandler.Process : Exporting Instagram winners")
        return self.instaWinners, self.waitlistWinners

    def doubleCheckWinners(self):
        totalWinners = self.waitlistWinners + self.instaWinners
        for winner in totalWinners:
            count = 0
            for x in range(len(totalWinners)):
                if totalWinners[x] == winner:
                    count += 1
            if count > 1:
                print("!!!!!!!!!!WinHandler.WinError : Account " + winner + " won twice!!!!!!!!!!")
