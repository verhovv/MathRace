import random


class TaskGenerator:
    def __init__(self, task_count: int):
        self.task_count = task_count
        self.i = 0

    def __next__(self):
        if self.i < self.task_count:
            self.i += 1

            return TaskGenerator.generate_task()

        raise StopIteration

    def __iter__(self):
        return self

    @staticmethod
    def generate_task() -> tuple[str, float | int]:
        generator_func = random.choice([
            TaskGenerator._generate_plus_task,
            TaskGenerator._generate_minus_task,
            TaskGenerator._generate_mul_task,
            TaskGenerator._generate_div_task,
        ])

        return generator_func()

    @staticmethod
    def _generate_plus_task(__min: int = 1, __max: int = 100) -> tuple[str, int]:
        a = random.randint(__min, __max)
        b = random.randint(__min, __max)

        task = f'$${a} + {b}$$'
        answer = a + b

        return task, answer

    @staticmethod
    def _generate_minus_task(__min: int = 1, __max: int = 100) -> tuple[str, int]:
        a = random.randint(__min, __max)
        b = random.randint(__min, __max)

        task = f'$${a} - {b}$$'
        answer = a - b

        return task, answer

    @staticmethod
    def _generate_mul_task(__min: int = 1, __max: int = 50) -> tuple[str, int]:
        a = random.randint(__min, __max)
        b = random.randint(__min, __max)

        task = f'$${a} * {b}$$'
        answer = a * b

        return task, answer

    @staticmethod
    def _generate_div_task(__min: int = 1, __max: int = 30) -> tuple[str, int]:
        a = random.randint(__min, __max)
        b = random.randint(__min, __max)

        task = f'$${"{"}{a * b}\\over{b}{"}"}$$'
        answer = a

        return task, answer
