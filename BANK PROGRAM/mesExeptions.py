class CustomErrorChoise(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

class CustomErrorNegativeAmont(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

class CustomErrorLessMoney(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)
