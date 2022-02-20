from mycroft import MycroftSkill, intent_file_handler


class Janet(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('janet.intent')
    def handle_janet(self, message):
        self.speak_dialog('janet')


def create_skill():
    return Janet()

