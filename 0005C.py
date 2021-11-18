class SimpleCommunicator(AbstractCommunicator):
    def __init__(self, channel : AbstractChannel):
    self._channel = channel

    def get_channel(self) -> str:
        return self._channel
        