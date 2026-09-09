# This is day 1 deliverable as per Claude
'''
build the Task/TaskQueue classes cold, with no reference open, satisfying:
Task is a @dataclass(order=True) with priority: int, name: str = field(compare=False)
TaskQueue wraps heapq, supports push(task) and pop() returning highest-priority (lowest number) task first
Two tasks with equal priority don't crash on push
repr(task_queue) prints something readable, not <TaskQueue object at 0x7f...>
'''

from dataclasses import dataclass, field
import heapq
from itertools import count

@dataclass(order=True)
class Task:
    priority: int
    name: str = field(compare=False)

class TaskQueue:
    def __init__(self):
        self.queue = []
        self.counter = count()

    def __repr__(self):
        if len(self.queue) > 0:
            task = self.queue[0][2]
            return "TaskQueue({} tasks, next = Task(priority={}, name='{}'))".format(len(self.queue), task.priority, task.name)
        return "TaskQueue(0 task, empty)"

    def push(self, task: Task):
        heapq.heappush(self.queue, (task.priority, next(self.counter), task))

    def pop(self):
        if not self.queue:
            raise IndexError('Pop from an empty queue')
        return heapq.heappop(self.queue)[2]

    def peek(self):
        if len(self.queue) > 0:
            return self.queue[0][2]
        raise IndexError('Queue Empty')

    def __len__(self):
        return len(self.queue)

        
q_test = TaskQueue()
for p, n in [(3, 'c'), (1, 'a'), (2, 'b')]:
    q_test.push(Task(p, n))
assert q_test.pop().name == 'a'
assert q_test.pop().name == 'b'
assert q_test.pop().name == 'c'

q_empty = TaskQueue()
try:
    q_empty.pop()
    assert False, "expected IndexError"
except IndexError:
    pass

q_tie = TaskQueue()
q_tie.push(Task(5, 'x'))
q_tie.push(Task(5, 'y'))
first = q_tie.pop()
second = q_tie.pop()
assert {first.name, second.name} == {'x', 'y'}

q_peek = TaskQueue()
q_peek.push(Task(1, 'z'))
assert q_peek.peek().name == 'z'
assert len(q_peek) == 1