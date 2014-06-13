from ..libs import DefaultRepository
from . import Demo

class DemoRepository(DefaultRepository):

    def __init__(self):
        self.document = Demo

