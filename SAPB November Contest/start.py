import sys
from InstagramHandler import InstagramDataCheck, InstagramValidityCheck
from WinHandler import WinHandler

sys.stdout = open('log.txt', 'w')
print("Output.Process : Generating output log file")

igD = InstagramDataCheck()
igData = igD.getData()
ig = InstagramValidityCheck(igData)
ig.runCheck()
igContestants = ig.getContestants()

w = WinHandler(igContestants)
instaWinners = w.getInstagramWinners()

for winner in instaWinners:
    print("Instagram Winner! : " + str(winner))

print("Output.Process : Closing output log file")
sys.stdout.close()