import pytest

from src.util import removeDuplicates


def test_removeDuplicates_1():
    listWithDuplicates = ["dogs", "camel", "sparrow", "dogs", "emu", "penguin",
                          "dogs", "camel"]
    uniqueList = ["dogs", "camel", "sparrow", "emu", "penguin"]
    assert removeDuplicates(listWithDuplicates) == uniqueList


def test_removeDuplicates_2():
    listWithDuplicates = ["dogs", "camel", "sparrow", "emu", "penguin"]
    uniqueList = ["dogs", "camel", "sparrow", "emu", "penguin"]
    assert removeDuplicates(listWithDuplicates) == uniqueList
