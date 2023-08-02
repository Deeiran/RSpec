from lib.gratitudes import * 
'''
Given multiple gratitudes
we can see a nice list of them
'''

def test_multiple_gratitudes():
    gratitudes = Gratitudes()
    gratitudes.add("my cat")
    gratitudes.add("the sun")
    gratitudes.add("my friends")
    result = gratitudes.format()
    assert result == "I am greatful for: my cat, the sun, and my friends."

"""
wehn we add a grattitude
it is added to the list
"""
def test_add_gratitude():
    gratitudes = Gratitudes()
    gratitudes.add("my cat")
    assert gratitudes.list == ["my cat"]