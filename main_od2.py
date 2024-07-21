# Реализация Стека с помощью списка
class Stack:
    def __init__(self):
        # Инициализируем пустой список для хранения элементов стека
        self.stack = []

    def push(self, item):
        # Добавляем элемент в конец списка (на вершину стека)
        self.stack.append(item)

    def pop(self):
        # Удаляем и возвращаем последний элемент списка (верхушку стека)
        if not self.is_empty():
            return self.stack.pop()
        else:
            raise IndexError("Попытка извлечь элемент из пустого стека")

    def peek(self):
        # Возвращаем последний элемент списка (верхушку стека), но не удаляем его
        if not self.is_empty():
            return self.stack[-1]
        else:
            raise IndexError("попытку получить первый элемент из стека, когда она пуста")

    def is_empty(self):
        # Проверяем, пуст ли стек
        return len(self.stack) == 0

    def size(self):
        # Возвращаем количество элементов в стеке
        return len(self.stack)

# Пример использования стека
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
print(stack.pop())  # Выведет 3
print(stack.peek())  # Выведет 2
print(stack.size())  # Выведет 2

print('-------------------------------------------------------------')

# Реализация очереди
class Queue:
    def __init__(self):
        # Инициализируем пустой список для хранения элементов очереди
        self.queue = []

    def enqueue(self, item):
        # Добавляем элемент в конец списка (в конец очереди)
        self.queue.append(item)

    def dequeue(self):
        # Удаляем и возвращаем первый элемент списка (начало очереди)
        if not self.is_empty():
            return self.queue.pop(0)
        else:
            raise IndexError("Попытка извлечь элемент из пустой очереди")

    def peek(self):
        # Возвращаем первый элемент списка (начало очереди), но не удаляем его
        if not self.is_empty():
            return self.queue[0]
        else:
            raise IndexError("Попытку получить первый элемент из очереди, когда она пуста")

    def is_empty(self):
        # Проверяем, пуста ли очередь
        return len(self.queue) == 0

    def size(self):
        # Возвращаем количество элементов в очереди
        return len(self.queue)

# Пример использования очереди
queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
print(queue.dequeue())  # Выведет 1
print(queue.peek())  # Выведет 2
print(queue.size())  # Выведет 2
