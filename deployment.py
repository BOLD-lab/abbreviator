from abbreviate import sentence_shortener

class Deployment:

    def __init__(self, base_directory, context):
        print("Initialising My Deployment")

    def request(self, data):
        print("Processing request for My Deployment")

        return {
            "original": data['long'],
            "short" : sentence_shortener(data['long'])
        }