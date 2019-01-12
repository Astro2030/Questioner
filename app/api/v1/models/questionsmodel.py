all_Questions = []


class Questions():
    '''Initialize class variables the questions model needs once it starts'''

    def __init__(self):
        pass

    def create_question(self, createdOn, createdBy, meetup, topic, upvotes, downvotes):
        question_payload = {
            "question_id": len(all_Questions)+1,
            "createdOn": createdOn,
            "createdBy": createdBy,
            "meetup": meetup,
            "topic": topic,
            "upvotes": upvotes,
            "downvotes": downvotes

        }
        all_Questions.append(question_payload)
        return question_payload

    def upvote(self, question_id, vote):
        '''Vote a question'''

        question = [
            question for question in all_Questions if question['question_id'] == question_id
        ]
        if not question:
            return "Question does not exist", 400
        if vote == "+":
            action = "upvoted"
            new_upvotes = question[0]["upvotes"]+1
            new_downvotes = question[0]["downvotes"]
        elif vote == "-":
            action = "downvoted"
            new_upvotes = question[0]["upvotes"]
            new_downvotes = question[0]["downvotes"]+1

        question_payload = {
            "question_id":  question[0]['question_id'],
            "createdOn": question[0]['createdOn'],
            "createdBy": question[0]['createdBy'],
            "meetup": question[0]['meetup'],
            "topic": question[0]['topic'],
            "upvotes": new_upvotes,
            "downvotes": new_downvotes

        }

        for i, question in enumerate(all_Questions):
            if question['question_id'] == question_id:
                all_Questions[i] = question_payload

        return {"Message": 'You {} question {} successfully'.format(action, question_id)}, 200
