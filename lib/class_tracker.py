class Tracker():
    def __init__(self):
        self._track_list = []
   
    def add(self,track):
        for old_track in self._track_list:
            if track == old_track:
                raise Exception("This track is alreday added in the list")
        self._track_list.append(track)
        
    def tracker_list(self):
        return self._track_list