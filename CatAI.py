from CatMisc import CatState as _CatState
# cannot import Cat class to use for type annotations
# because of circulair import error


class CatBehaviour:
    def __init__(self, cat) -> None:
        self.cat = cat

    def decision(self):
        print(self.cat)

