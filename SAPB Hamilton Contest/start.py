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
igCommentNum = ig.getTotalComments()

w = WinHandler(igContestants)
instaWinners, waitlistWinners = w.getInstagramWinners()

print("======================================================")
num = 1
for winner in instaWinners:
    print("Instagram Winner " + str(num) + " : " + str(winner))
    num += 1
num = 1
for winner in waitlistWinners:
    print("Backup Winner " + str(num) + " : " + str(winner))
    num += 1

print("Total Comments: " + str(igCommentNum))
print("Total Contestants: " + str(len(igContestants)))
print("======================================================")

print("Output.Process : Closing output log file")
sys.stdout.close()