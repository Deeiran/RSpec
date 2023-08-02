class Gratitudes():
    def __init__(self):     
        self.list = []
    
    def add(self, gratitude):
        self.list.append(gratitude)

    def format(self):
            gratitudes_string = ""
            for gratitude in self.list[:-1]:
                gratitudes_string += gratitude + ", "
            gratitudes_string += f"and {self.list[-1]}"
            return f"I am greatful for: {gratitudes_string}."