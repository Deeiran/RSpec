class GrammarStats:
    def __init__(self):
        self.total_checked = 0
        self.correct_grammar = 0
  
    def check(self, text):
        if text == "":
            raise Exception("No Text Message Given")
        result = text[0].isupper() and text[-1] in [".","!","?"]
        self.total_checked += 1
        if result:
            self.correct_grammar += 1
        return result

    def percentage_good(self):
        if self.total_checked == 0:
            return 0
        else:
            return round(((self.correct_grammar/self.total_checked) * 100),2)
        