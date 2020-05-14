from mycroft import MycroftSkill, intent_file_handler


class NewCalm(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('calm.new.intent')
    def handle_calm_new(self, message):
        self.speak_dialog('calm.new')


def create_skill():
    return NewCalm()

