from datetime import datetime, timedelta

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


def test_overdue_ignores_completed():
    board = TaskBoard()
    task = board.add("old task")
    task.created_at = datetime.now() - timedelta(days=30)
    board.complete("old task")
    assert board.overdue() == []


def test_add_bulk_collects_errors():
    board = TaskBoard()
    errors = board.add_bulk(["ok task", "   "])
    assert errors == ["title must not be empty"]
    assert board.stats()["total"] == 1
