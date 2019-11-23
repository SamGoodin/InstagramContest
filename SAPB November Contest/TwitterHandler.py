import twitter


class TwitterDataCheck:

    def __init__(self):
        self.api = twitter.Api(consumer_key="mQRkTTEZHUY7pKiOjHeQAy8Tc",
                          consumer_secret="tGnQ3MIgbCSR3pNeez9fBb7HhIaTBssvyZ10l5oHr1q5mpBwWK ",
                          access_token_key="2823590626-ZEOYpLpEhbgzHV3EQ9WXBrKYMvagZoZdgQC3DN4",
                          access_token_secret="6NdZtFEBElsI5yUw8knWbZgrptUzvB98WsFjDBHwxvRwl ")
        print("TwitterDataCheck.State : Initialized")

    # so we don't have to instantiate the api again
    def getApi(self):
        return self.api

    def getData(self):
        self.retweeters = self.api.GetRetweeters(1191775631467524096)
        return None


class TwitterValidityCheck:

    def __init__(self, twitterData, api):
        self.data = twitterData
        self.api = api
        self.contestants = []
        print("TwitterValidityCheck.State : Initialized")

    def runCheck(self):
        print("TwitterValidityCheck.Process : Begin validation")

        print("TwitterValidityCheck.Process : Validity check complete")

    def getContestants(self):
        print("TwitterValidityCheck.Process : Exporting contestants")
        return self.contestants
