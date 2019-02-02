""" Tests for model controllers """
import pytest
from boo.controllers import TaskController


@pytest.mark.usefixtures("session")
class TestTaskController:
    all_tasks = lambda s: TaskController.model.query.all()

    def test_no_tasks(self):
        assert len(self.all_tasks()) is 0

    def test_create_task(self):
        assert len(self.all_tasks()) is 0

        task = TaskController.create(name="test_task")
        assert task.id is 1

        assert len(self.all_tasks()) is 1
