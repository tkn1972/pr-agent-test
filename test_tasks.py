from tasks import PRIORITY_HIGH, TaskBoard


def test_add_and_stats():
    board = TaskBoard()
    board.add("write tests")
    board.add("ship feature", priority=PRIORITY_HIGH)
    assert board.stats() == {"total": 2, "done": 0, "pending": 2}


def test_complete():
    board = TaskBoard()
    board.add("write tests")
    assert board.complete("write tests") is True
    assert board.stats()["done"] == 1
    assert board.complete("write tests") is False


def test_add_rejects_blank_title():
    board = TaskBoard()
    try:
        board.add("   ")
    except ValueError:
        return
    raise AssertionError("expected ValueError for blank title")
