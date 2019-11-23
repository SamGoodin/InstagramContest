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
        self.maybe = {}
        self.contestants = []
        print("InstagramValidityCheck.State : Initialized")

    def runCheck(self):
        print("InstagramValidityCheck.Process : Begin comment validation")
        while self.data.cell_value(self.counter, 2) != "":
            print("InstagramValidityCheck.Process : Validating comment " + str(self.counter - 5))
            comment = self.data.cell_value(self.counter, 5)

            # tag check
            symbol_count = 0
            print("InstagramValidityCheck.Process : Counting tagged profiles in comment " + str(self.counter - 5))
            for letter in comment:
                if letter == '@':
                    symbol_count += 1
            username = self.data.cell_value(self.counter, 2)
            if symbol_count >= 3:
                self.comments[username] = comment
                print("InstagramValidityCheck.Process : Comment " + str(self.counter - 5) + " validated")
            elif symbol_count > 0:
                # may have tagged in different comments
                if username in self.maybe.keys():
                    var = self.maybe[username]
                    var[0] += symbol_count
                    var[1].append(comment)
                    if var[0] >= 3:
                        self.comments[username] = var[1]
                        print("InstagramValidityCheck.Process : Comment " + str(self.counter - 5) + " validated")
                else:
                    self.maybe[username] = [symbol_count, [comment]]
                    print("InstagramValidityCheck.Process : Comment " + str(self.counter - 5) + " needs more validation")

            self.counter += 1

        for commenter in self.comments:
            user_data = self.instaApi.username_info(commenter)['user']
            followers = user_data['follower_count']
            if followers > 100:
                self.contestants.append(commenter)

        print("InstagramValidityCheck.Process : Validity check complete")

    def getContestants(self):
        print("InstagramValidityCheck.Process : Exporting contestants")
        return self.contestants
