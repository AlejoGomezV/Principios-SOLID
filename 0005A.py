from abc import ABC
from typing import final


class AbstractChannel(ABC):
    def get_channel_message(self) -> str:
        pass


class AbstractCommunicator(ABC):
    def get_channel(self) -> AbstractChannel:
        pass

    @final
    def communicate(self, conversation: AbstractConversation):
        print(*conversation.do_conversation(), self.get_channel().get_channel_message(), sep = '\n')
        