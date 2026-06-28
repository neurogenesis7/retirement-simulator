from abc import ABC, abstractmethod


class ReturnGenerator(ABC):

    @abstractmethod
    def next_return(self) -> float:
        """Return the next monthly return."""
        raise NotImplementedError
