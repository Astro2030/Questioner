all_Questions = []


class Questions():
    '''Initialize class variables the questions model needs once it starts'''

    def __init__(self, createdOn, createdBy, meetup, topic):

        self.createdOn = createdOn
        self.createdBy = createdBy
        self.meetup = meetup
        self.topic = topic

    def create_question(self):
        question_payload = {

            "createdOn": self.createdOn,
            "createdBy": self.createdBy,
            "meetup": self.meetup,
            "topic": self.topic,

        }
        all_Questions.append(question_payload)
        return question_payload