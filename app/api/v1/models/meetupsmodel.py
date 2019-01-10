import datetime
all_meetups = []
all_rsvps = []


class Meetups():
    '''Initialize class variables the meetups model needs once it starts'''

    def __init__(self):
        pass

    def create_meetup(self, meetup_id, location, topic):
        meetup = {"meetup_id": meetup_id,
                  "createdOn": datetime.datetime.now().strftime("%y-%m-%d-%H-%M"),
                  "location": location,
                  "topic": topic
                  }
        all_meetups.append(meetup)
        return meetup

    def get_all_meetups(self):
        return all_meetups

    def get_one_meetup(self, meetup_id):
        '''Get one meetup'''
        meetup_available = [
            meetup for meetup in all_meetups if meetup['meetup_id'] == meetup_id]
        return meetup_available

    def create_rsvp(self, meetup_id, status):
        rsvp_details = {
            "id": len(all_rsvps)+1,
            "createdOn": datetime.datetime.now().strftime("%y-%m-%d-%H-%M"),
            "meetup": meetup_id,
            "status": status
        }

        all_rsvps.append(rsvp_details)

        return rsvp_details