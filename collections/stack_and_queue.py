def create_stack():
    return []


def is_empty(stack):
    return len(stack) == 0


def push(stack, item):
    stack.append(item)


def pop(stack):
    if not is_empty(stack):
        return stack.pop()
    else:
        print("Стек порожній")


def peek(stack):
    if not is_empty(stack):
        return stack[-1]
    else:
        print("Стек порожній")


stack = create_stack()
push(stack, "a")
push(stack, "b")
push(stack, "c")


print(peek(stack))
print(pop(stack))

print(stack)

print("-------------------------")


from collections import deque

queue = deque()

queue.append("a")
queue.append("b")
queue.append("c")

print("Черга після додавання елементів:", list(queue))

print("Видалений елемент:", queue.popleft())

print("Черга після видалення елемента:", list(queue))

print("Перший елемент у черзі:", queue[0])

print("Чи черга порожня:", len(queue) == 0)

print("Розмір черги:", len(queue))

print("-------------------------")


d = deque()

d.append("middle")
d.append("last")
d.appendleft("first")

print("Черга після додавання елементів:", list(d))

print("Видалений останній елемент:", d.pop())

print("Видалений перший елемент:", d.popleft())

print("Черга після видалення елементів:", list(d))

print("-------------------------")

d = deque(maxlen=5)
for i in range(10):
    d.append(i)

print(d)

print("-------------------------")

tasks = [
    {"type": "fast", "name": "Помити посуд"},
    {"type": "slow", "name": "Подивитись серіал"},
    {"type": "fast", "name": "Вигуляти собаку"},
    {"type": "slow", "name": "Почитати книгу"},
]

task_queue = deque()

for task in tasks:
    if task["type"] == "fast":
        task_queue.appendleft(task)
        print(f"Додано швидке завдання: {task['name']}")
    else:
        task_queue.append(task)
        print(f"Додано повільне завдання: {task['name']}")

while task_queue:
    task = task_queue.popleft()
    print(f"Виконується завдання: {task['name']}")
