import math
class DiaryEntry():
    def __init__(self, title, contents):
        if title == "" or contents == "":
            raise Exception("Diary entries must have a title or contents")
        self.title = title
        self.contents = contents
        self.read_so_far = 0

    def format(self):
        return f"{self.title}: {self.contents}"

    def count_words(self):
        words = self.format().split()
        return len(words)
    
    def reading_time(self, wpm):
        if wpm == 0:
            raise Exception("cannot calculate the time with zero words")
        content_words_count = len(self.contents.split())
        return math.ceil(content_words_count/wpm)
      
    # def reading_chunk(self, wpm, minutes):
    #     number_of_words_can_read = wpm * minutes
    #     words = self.contents.split()
    #     if len(words) <= self.read_so_far:
    #         self.read_so_far = 0
    #     chunk_start = self.read_so_far
    #     chunk_end = self.read_so_far + number_of_words_can_read
    #     chunk_words = words[chunk_start:chunk_end]
    #     self.read_so_far = chunk_end
    #     print (chunk_words)
    #     return " ".join(chunk_words)
    

    def reading_chunk(self,wpm,minutes):
        words_can_be_read = wpm * minutes
        words = self.contents.split()
        if len(words) <= self.read_so_far:
            self.read_so_far = 0
        chunk_words =  words[self.read_so_far:self.read_so_far + words_can_be_read]
        self.read_so_far += words_can_be_read
        return (" ".join(chunk_words))


        # Parameters
        #   wpm: an integer representing the number of words the user can read
        #        per minute
        #   minutes: an integer representing the number of minutes the user has
        #            to read
        # Returns:
        #   string: a chunk of the contents that the user could read in the
        #           given number of minutes
        #
        # If called again, `reading_chunk` should return the next chunk,
        # skipping what has already been read, until the contents is fully read.
        # The next call after that should restart from the beginning.
        pass