class SimpleConversation(AbstractConversation):
    def __init__(self, bird1: Bird, bird2: Bird):
        self.bird1 = bird1
        self.bird2 = bird2

    def do_conversation(self) -> list:
        sentence1 = f"{self.bird1.name}: {self.bird1.do_sound()}, hello {self.bird2.name}"
        sentence2 = f"{self.bird2.name}: {self.bird2.do_sound()}, hello {self.bird1.name}"
        return [sentence1, sentence2]
        