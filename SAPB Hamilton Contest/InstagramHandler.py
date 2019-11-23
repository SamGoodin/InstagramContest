import xlrd
from instagram_private_api import Client


class InstagramDataCheck:

    def __init__(self):
        self.loc = "comments.xlsx"
        print("InstagramDataCheck.State : Initialized")

    def getData(self):
        print("InstagramDataCheck.Process : Polling comment data")
        wb = xlrd.open_workbook(self.loc)
        print("InstagramDataCheck.Process : Polling complete")
        return wb.sheet_by_index(0)


class InstagramValidityCheck:

    def __init__(self, instaData):
        self.data = instaData
        self.instaApi = Client("sammy.g.spam", "vq86koli")
        self.counter = 6
        self.comments = {}
        self.contestants = []
        print("InstagramValidityCheck.State : Initialized")

    def runCheck(self):
        print("InstagramValidityCheck.Process : Begin comment validation")
        while self.data.cell_value(self.counter, 2) != "":
            print("InstagramValidityCheck.Process : Validating account for comment " + str(self.counter - 5))
            comment = self.data.cell_value(self.counter, 5)
            username = self.data.cell_value(self.counter, 2)
            if username not in self.contestants:
                # tag check (@ 1 person)
                print("InstagramValidityCheck.Process : Checking comment " + str(self.counter - 5) + " for tagged profile")
                for letter in comment:
                    if letter == '@':
                        self.contestants.append(username)
                        print("InstagramValidityCheck.Process : Comment " + str(self.counter - 5) + " validated")
                        print("InstagramValidityCheck.Process : Contestant for comment " + str(self.counter - 5) + " added")
                        """
                        if username not in self.comments.keys():
                            self.comments[username] = comment
                            print("InstagramValidityCheck.Process : Comment " + str(self.counter - 5) + " validated")
                        """
                        break
            else:
                print("InstagramValidityCheck.Process : Account for comment " + str(self.counter - 5) + " already entered")
            self.counter += 1

        """
        # filter possible fake accounts
        for commenter in self.comments:
            user_data = self.instaApi.username_info(commenter)['user']
            followers = user_data['follower_count']
            if followers > 100:
                self.contestants.append(commenter)
        """
        print("InstagramValidityCheck.Process : Validity check complete")

    def getContestants(self):
        print("InstagramValidityCheck.Process : Exporting contestants")
        return self.contestants

    def getTotalComments(self):
        return self.counter - 6
