class SMSChannel(AbstractChannel):
    def get_channel_message(self) -> str:
        return "(via SMS)"

class SMSCommunicator(AbstractCommunicator):
    def __init__(self):
        self._channel = SMSChannel()
    
    def get_channel(self) -> AbstractChannel:
        return self._channel
        