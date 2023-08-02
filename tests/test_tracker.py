from lib.class_tracker import *
import pytest 

"""
initally, there is no tracks
return empty list 
"""
def test_intially_no_track():
    tracker = Tracker()
    assert tracker.tracker_list() == []

"""
When we add a track
that tracker added to the tracker list. 
"""
def test_add_a_track():
    tracker = Tracker()
    tracker.add("beliver")
    assert tracker.tracker_list() == ["beliver"]

"""
When we add mulitble tracks 
all tracks added to the tracker list. 
"""
def test_add_a_track():
    tracker = Tracker()
    tracker.add("beliver")
    tracker.add("don't give up")
    tracker.add("love me like you do")
    assert tracker.tracker_list() == ["beliver", "don't give up", "love me like you do"]

"""
When we add doplicate track
raise the error message "This track is alreday added in the list"
"""
def test_add_dup_track():
    tracker = Tracker()
    tracker.add("beliver")
    with pytest.raises(Exception) as err:
        tracker.add("beliver")
    assert str(err.value) == "This track is alreday added in the list"

