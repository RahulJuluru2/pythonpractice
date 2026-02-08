LAB_TOPICS = {
    "loops": {
        "label": "Loops",
        "examples": [
            {
                "title": "For Loop Sum",
                "code": "\n".join(
                    [
                        "numbers = [1, 2, 3, 4, 5]",
                        "total = 0",
                        "for value in numbers:",
                        "    total += value",
                        "print('sum', total)",
                    ]
                ),
            },
            {
                "title": "While Countdown",
                "code": "\n".join(
                    [
                        "count = 3",
                        "while count > 0:",
                        "    print('tick', count)",
                        "    count -= 1",
                        "print('done')",
                    ]
                ),
            },
            {
                "title": "Enumerate + Continue",
                "code": "\n".join(
                    [
                        "items = ['a', 'b', 'skip', 'c']",
                        "for idx, item in enumerate(items):",
                        "    if item == 'skip':",
                        "        continue",
                        "    print(idx, item)",
                    ]
                ),
            },
        ],
        "prompts": [
            "Rewrite one loop using a while loop.",
            "Add a condition that skips values > 3.",
            "Compute a running total and print it each iteration.",
        ],
    },
    "functions": {
        "label": "Functions",
        "examples": [
            {
                "title": "Defaults + Keyword-Only",
                "code": "\n".join(
                    [
                        "def greet(name, *, punctuation='!'):",
                        "    return f'Hello, {name}{punctuation}'",
                        "",
                        "print(greet('Python'))",
                        "print(greet('Coders', punctuation='?'))",
                    ]
                ),
            },
            {
                "title": "Higher-Order",
                "code": "\n".join(
                    [
                        "def apply_twice(func, value):",
                        "    return func(func(value))",
                        "",
                        "print(apply_twice(lambda x: x * 2, 5))",
                    ]
                ),
            },
            {
                "title": "Closure",
                "code": "\n".join(
                    [
                        "def make_multiplier(factor):",
                        "    def multiply(value):",
                        "        return value * factor",
                        "    return multiply",
                        "",
                        "triple = make_multiplier(3)",
                        "print(triple(7))",
                    ]
                ),
            },
        ],
        "prompts": [
            "Add type hints and default values.",
            "Write a function that returns another function.",
            "Use positional-only or keyword-only parameters.",
        ],
    },
    "classes": {
        "label": "Classes",
        "examples": [
            {
                "title": "Simple Counter",
                "code": "\n".join(
                    [
                        "class Counter:",
                        "    def __init__(self, start=0):",
                        "        self.value = start",
                        "",
                        "    def increment(self, step=1):",
                        "        self.value += step",
                        "        return self.value",
                        "",
                        "counter = Counter()",
                        "print(counter.increment())",
                        "print(counter.increment(3))",
                    ]
                ),
            },
            {
                "title": "Class Method",
                "code": "\n".join(
                    [
                        "class User:",
                        "    def __init__(self, name):",
                        "        self.name = name",
                        "",
                        "    @classmethod",
                        "    def from_email(cls, email):",
                        "        return cls(email.split('@')[0])",
                        "",
                        "print(User.from_email('ava@example.com').name)",
                    ]
                ),
            },
            {
                "title": "Dunder Methods",
                "code": "\n".join(
                    [
                        "class Point:",
                        "    def __init__(self, x, y):",
                        "        self.x = x",
                        "        self.y = y",
                        "",
                        "    def __repr__(self):",
                        "        return f'Point({self.x}, {self.y})'",
                        "",
                        "print(Point(3, 4))",
                    ]
                ),
            },
        ],
        "prompts": [
            "Add a reset method that sets the counter to zero.",
            "Make Counter support len(counter) using __len__.",
            "Add a __repr__ that shows the current value.",
        ],
    },
    "comprehensions": {
        "label": "Comprehensions",
        "examples": [
            {
                "title": "List + Filter",
                "code": "\n".join(
                    [
                        "data = [1, 2, 3, 4, 5, 6]",
                        "squares = [n * n for n in data if n % 2 == 0]",
                        "print(squares)",
                    ]
                ),
            },
            {
                "title": "Dict Comprehension",
                "code": "\n".join(
                    [
                        "data = [1, 2, 3, 4]",
                        "lookup = {n: n * n for n in data}",
                        "print(lookup)",
                    ]
                ),
            },
            {
                "title": "Nested Comprehension",
                "code": "\n".join(
                    [
                        "pairs = [(i, j) for i in range(2) for j in range(3)]",
                        "print(pairs)",
                    ]
                ),
            },
        ],
        "prompts": [
            "Create a dict comprehension that maps values to cubes.",
            "Use a nested comprehension to make a 3x3 matrix.",
            "Convert pairs into a set of formatted strings.",
        ],
    },
    "generators": {
        "label": "Generators",
        "examples": [
            {
                "title": "Basic Generator",
                "code": "\n".join(
                    [
                        "def countdown(n):",
                        "    while n > 0:",
                        "        yield n",
                        "        n -= 1",
                        "",
                        "print(list(countdown(5)))",
                    ]
                ),
            },
            {
                "title": "Generator Expression",
                "code": "\n".join(
                    [
                        "nums = (i * i for i in range(6))",
                        "print(sum(nums))",
                    ]
                ),
            },
            {
                "title": "Yield From",
                "code": "\n".join(
                    [
                        "def odds():",
                        "    yield from [1, 3, 5]",
                        "",
                        "print(list(odds()))",
                    ]
                ),
            },
        ],
        "prompts": [
            "Turn countdown into an infinite generator with a caller limit.",
            "Write a generator that yields squares until they exceed 100.",
            "Use yield from to compose generators.",
        ],
    },
    "decorators": {
        "label": "Decorators",
        "examples": [
            {
                "title": "Timing Decorator",
                "code": "\n".join(
                    [
                        "import time",
                        "",
                        "def timer(fn):",
                        "    def wrapper(*args, **kwargs):",
                        "        start = time.time()",
                        "        result = fn(*args, **kwargs)",
                        "        elapsed = (time.time() - start) * 1000",
                        "        print(f'{fn.__name__} took {elapsed:.2f}ms')",
                        "        return result",
                        "    return wrapper",
                        "",
                        "@timer",
                        "def work(x):",
                        "    total = 0",
                        "    for i in range(x):",
                        "        total += i * i",
                        "    return total",
                        "",
                        "print(work(2000))",
                    ]
                ),
            },
            {
                "title": "Decorator With Args",
                "code": "\n".join(
                    [
                        "def repeat(times):",
                        "    def decorator(fn):",
                        "        def wrapper(*args, **kwargs):",
                        "            for _ in range(times):",
                        "                result = fn(*args, **kwargs)",
                        "            return result",
                        "        return wrapper",
                        "    return decorator",
                        "",
                        "@repeat(3)",
                        "def greet(name):",
                        "    print('Hi', name)",
                        "",
                        "greet('Ada')",
                    ]
                ),
            },
            {
                "title": "Class Decorator",
                "code": "\n".join(
                    [
                        "def tag(cls):",
                        "    cls.tag = 'ready'",
                        "    return cls",
                        "",
                        "@tag",
                        "class Job:",
                        "    pass",
                        "",
                        "print(Job.tag)",
                    ]
                ),
            },
        ],
        "prompts": [
            "Preserve wrapped metadata with functools.wraps.",
            "Write a decorator that retries a function 3 times on error.",
            "Measure runtime and return value size.",
        ],
    },
    "context_managers": {
        "label": "Context Managers",
        "examples": [
            {
                "title": "Contextlib",
                "code": "\n".join(
                    [
                        "from contextlib import contextmanager",
                        "",
                        "@contextmanager",
                        "def session(name):",
                        "    print('start', name)",
                        "    try:",
                        "        yield {'name': name}",
                        "    finally:",
                        "        print('end', name)",
                        "",
                        "with session('alpha') as ctx:",
                        "    print('inside', ctx['name'])",
                    ]
                ),
            },
            {
                "title": "Custom Class",
                "code": "\n".join(
                    [
                        "class Printer:",
                        "    def __enter__(self):",
                        "        print('enter')",
                        "        return self",
                        "",
                        "    def __exit__(self, exc_type, exc, tb):",
                        "        print('exit')",
                        "",
                        "with Printer():",
                        "    print('work')",
                    ]
                ),
            },
            {
                "title": "Suppress Errors",
                "code": "\n".join(
                    [
                        "from contextlib import suppress",
                        "",
                        "with suppress(ZeroDivisionError):",
                        "    print(1 / 0)",
                        "print('still running')",
                    ]
                ),
            },
        ],
        "prompts": [
            "Add error handling that prints exceptions before re-raising.",
            "Create a context manager that times a block.",
            "Chain two context managers together in one with.",
        ],
    },
    "data_classes": {
        "label": "Data Classes",
        "examples": [
            {
                "title": "Basic Dataclass",
                "code": "\n".join(
                    [
                        "from dataclasses import dataclass",
                        "",
                        "@dataclass",
                        "class Player:",
                        "    name: str",
                        "    score: int = 0",
                        "",
                        "print(Player('Ava', 10))",
                    ]
                ),
            },
            {
                "title": "Default Factory",
                "code": "\n".join(
                    [
                        "from dataclasses import dataclass, field",
                        "",
                        "@dataclass",
                        "class Team:",
                        "    name: str",
                        "    members: list[str] = field(default_factory=list)",
                        "",
                        "team = Team('Stars')",
                        "team.members.append('Ira')",
                        "print(team)",
                    ]
                ),
            },
            {
                "title": "Post Init",
                "code": "\n".join(
                    [
                        "from dataclasses import dataclass",
                        "",
                        "@dataclass",
                        "class Range:",
                        "    start: int",
                        "    end: int",
                        "",
                        "    def __post_init__(self):",
                        "        if self.start >= self.end:",
                        "            raise ValueError('start < end')",
                        "",
                        "print(Range(1, 3))",
                    ]
                ),
            },
        ],
        "prompts": [
            "Add ordering and compare two players.",
            "Make score computed from tags length.",
            "Add a __post_init__ validation.",
        ],
    },
    "iterators": {
        "label": "Iterators",
        "examples": [
            {
                "title": "Iterator Class",
                "code": "\n".join(
                    [
                        "class EvenNumbers:",
                        "    def __init__(self, limit):",
                        "        self.limit = limit",
                        "        self.current = 0",
                        "",
                        "    def __iter__(self):",
                        "        return self",
                        "",
                        "    def __next__(self):",
                        "        if self.current > self.limit:",
                        "            raise StopIteration",
                        "        value = self.current",
                        "        self.current += 2",
                        "        return value",
                        "",
                        "print(list(EvenNumbers(10)))",
                    ]
                ),
            },
            {
                "title": "Iter + Next",
                "code": "\n".join(
                    [
                        "items = iter(['a', 'b', 'c'])",
                        "print(next(items))",
                        "print(next(items))",
                    ]
                ),
            },
            {
                "title": "Custom Iterable",
                "code": "\n".join(
                    [
                        "class Countdown:",
                        "    def __init__(self, start):",
                        "        self.start = start",
                        "",
                        "    def __iter__(self):",
                        "        for i in range(self.start, 0, -1):",
                        "            yield i",
                        "",
                        "print(list(Countdown(4)))",
                    ]
                ),
            },
        ],
        "prompts": [
            "Make the iterator restartable by returning a new iterator.",
            "Support iteration over only odd numbers.",
            "Add a take(n) helper that returns a list.",
        ],
    },
    "error_handling": {
        "label": "Error Handling",
        "examples": [
            {
                "title": "Try / Except / Finally",
                "code": "\n".join(
                    [
                        "def safe_divide(a, b):",
                        "    try:",
                        "        return a / b",
                        "    except ZeroDivisionError as exc:",
                        "        print('error', exc)",
                        "        return None",
                        "    finally:",
                        "        print('done')",
                        "",
                        "print(safe_divide(10, 2))",
                        "print(safe_divide(10, 0))",
                    ]
                ),
            },
            {
                "title": "Raise Custom",
                "code": "\n".join(
                    [
                        "class InvalidAge(ValueError):",
                        "    pass",
                        "",
                        "def set_age(age):",
                        "    if age < 0:",
                        "        raise InvalidAge('age must be positive')",
                        "    return age",
                        "",
                        "print(set_age(5))",
                    ]
                ),
            },
            {
                "title": "Try / Else",
                "code": "\n".join(
                    [
                        "def parse_int(text):",
                        "    try:",
                        "        value = int(text)",
                        "    except ValueError:",
                        "        print('bad input')",
                        "    else:",
                        "        print('parsed', value)",
                        "",
                        "parse_int('3')",
                        "parse_int('x')",
                    ]
                ),
            },
        ],
        "prompts": [
            "Raise a custom exception for invalid input.",
            "Log errors with stack traces.",
            "Use else to handle the success path cleanly.",
        ],
    },
    "typing_protocols": {
        "label": "Typing Protocols",
        "examples": [
            {
                "title": "Simple Protocol",
                "code": "\n".join(
                    [
                        "from typing import Protocol",
                        "",
                        "class Writer(Protocol):",
                        "    def write(self, message: str) -> None: ...",
                        "",
                        "class Console:",
                        "    def write(self, message: str) -> None:",
                        "        print(message)",
                        "",
                        "def report(writer: Writer, msg: str) -> None:",
                        "    writer.write(msg)",
                        "",
                        "report(Console(), 'Protocol ready')",
                    ]
                ),
            },
            {
                "title": "Runtime Check",
                "code": "\n".join(
                    [
                        "from typing import Protocol, runtime_checkable",
                        "",
                        "@runtime_checkable",
                        "class HasLen(Protocol):",
                        "    def __len__(self) -> int: ...",
                        "",
                        "print(isinstance([1, 2], HasLen))",
                    ]
                ),
            },
            {
                "title": "Multiple Methods",
                "code": "\n".join(
                    [
                        "from typing import Protocol",
                        "",
                        "class ReaderWriter(Protocol):",
                        "    def read(self) -> str: ...",
                        "    def write(self, message: str) -> None: ...",
                        "",
                        "class Buffer:",
                        "    def __init__(self):",
                        "        self.data = ''",
                        "",
                        "    def read(self) -> str:",
                        "        return self.data",
                        "",
                        "    def write(self, message: str) -> None:",
                        "        self.data = message",
                        "",
                        "buf = Buffer()",
                        "buf.write('ok')",
                        "print(buf.read())",
                    ]
                ),
            },
        ],
        "prompts": [
            "Add a second protocol with read/write methods.",
            "Implement the protocol with a file-like object.",
            "Use runtime_checkable to validate at runtime.",
        ],
    },
    "async_await": {
        "label": "Async / Await",
        "examples": [
            {
                "title": "Gather Tasks",
                "code": "\n".join(
                    [
                        "import asyncio",
                        "",
                        "async def fetch(value, delay):",
                        "    await asyncio.sleep(delay)",
                        "    return f'done {value}'",
                        "",
                        "async def main():",
                        "    results = await asyncio.gather(",
                        "        fetch('A', 0.2),",
                        "        fetch('B', 0.1),",
                        "    )",
                        "    print(results)",
                        "",
                        "asyncio.run(main())",
                    ]
                ),
            },
            {
                "title": "Await Loop",
                "code": "\n".join(
                    [
                        "import asyncio",
                        "",
                        "async def main():",
                        "    for i in range(3):",
                        "        await asyncio.sleep(0.05)",
                        "        print('tick', i)",
                        "",
                        "asyncio.run(main())",
                    ]
                ),
            },
            {
                "title": "Wait For",
                "code": "\n".join(
                    [
                        "import asyncio",
                        "",
                        "async def slow():",
                        "    await asyncio.sleep(1)",
                        "    return 'done'",
                        "",
                        "async def main():",
                        "    try:",
                        "        result = await asyncio.wait_for(slow(), timeout=0.2)",
                        "        print(result)",
                        "    except asyncio.TimeoutError:",
                        "        print('timed out')",
                        "",
                        "asyncio.run(main())",
                    ]
                ),
            },
        ],
        "prompts": [
            "Add a timeout to each fetch using asyncio.wait_for.",
            "Limit concurrency with a semaphore.",
            "Gather results as they complete with asyncio.as_completed.",
        ],
    },
    "asyncio_streams": {
        "label": "Asyncio Streams",
        "examples": [
            {
                "title": "Echo Server",
                "code": "\n".join(
                    [
                        "import asyncio",
                        "",
                        "async def handle_echo(reader, writer):",
                        "    data = await reader.readline()",
                        "    writer.write(data)",
                        "    await writer.drain()",
                        "    writer.close()",
                        "    await writer.wait_closed()",
                        "",
                        "async def main():",
                        "    server = await asyncio.start_server(handle_echo, '127.0.0.1', 0)",
                        "    host, port = server.sockets[0].getsockname()",
                        "",
                        "    reader, writer = await asyncio.open_connection(host, port)",
                        "    writer.write(b'ping\n')",
                        "    await writer.drain()",
                        "    response = await reader.readline()",
                        "    print(response.decode().strip())",
                        "    writer.close()",
                        "    await writer.wait_closed()",
                        "",
                        "    server.close()",
                        "    await server.wait_closed()",
                        "",
                        "asyncio.run(main())",
                    ]
                ),
            },
            {
                "title": "Stream Reader",
                "code": "\n".join(
                    [
                        "import asyncio",
                        "",
                        "async def main():",
                        "    reader = asyncio.StreamReader()",
                        "    reader.feed_data(b'line1\nline2\n')",
                        "    reader.feed_eof()",
                        "",
                        "    print((await reader.readline()).decode().strip())",
                        "    print((await reader.readline()).decode().strip())",
                        "",
                        "asyncio.run(main())",
                    ]
                ),
            },
            {
                "title": "Multiple Writes",
                "code": "\n".join(
                    [
                        "import asyncio",
                        "",
                        "async def handle(reader, writer):",
                        "    for _ in range(2):",
                        "        data = await reader.readline()",
                        "        writer.write(data.upper())",
                        "        await writer.drain()",
                        "    writer.close()",
                        "    await writer.wait_closed()",
                        "",
                        "async def main():",
                        "    server = await asyncio.start_server(handle, '127.0.0.1', 0)",
                        "    host, port = server.sockets[0].getsockname()",
                        "    reader, writer = await asyncio.open_connection(host, port)",
                        "    writer.write(b'hello\n')",
                        "    writer.write(b'world\n')",
                        "    await writer.drain()",
                        "    print((await reader.readline()).decode().strip())",
                        "    print((await reader.readline()).decode().strip())",
                        "    writer.close()",
                        "    await writer.wait_closed()",
                        "    server.close()",
                        "    await server.wait_closed()",
                        "",
                        "asyncio.run(main())",
                    ]
                ),
            },
        ],
        "prompts": [
            "Send multiple messages over the same connection.",
            "Echo back in uppercase before closing.",
            "Add a server-side delay and observe ordering.",
        ],
    },
    "descriptors": {
        "label": "Descriptors",
        "examples": [
            {
                "title": "Validation Descriptor",
                "code": "\n".join(
                    [
                        "class PositiveNumber:",
                        "    def __init__(self, default=0):",
                        "        self.default = default",
                        "        self.private_name = None",
                        "",
                        "    def __set_name__(self, owner, name):",
                        "        self.private_name = f'_{name}'",
                        "",
                        "    def __get__(self, instance, owner):",
                        "        if instance is None:",
                        "            return self",
                        "        return getattr(instance, self.private_name, self.default)",
                        "",
                        "    def __set__(self, instance, value):",
                        "        if value < 0:",
                        "            raise ValueError('Must be positive')",
                        "        setattr(instance, self.private_name, value)",
                        "",
                        "class Account:",
                        "    balance = PositiveNumber(0)",
                        "",
                        "acct = Account()",
                        "acct.balance = 10",
                        "print(acct.balance)",
                    ]
                ),
            },
            {
                "title": "Lazy Property",
                "code": "\n".join(
                    [
                        "class LazyValue:",
                        "    def __init__(self, factory):",
                        "        self.factory = factory",
                        "        self.private_name = None",
                        "",
                        "    def __set_name__(self, owner, name):",
                        "        self.private_name = f'_{name}'",
                        "",
                        "    def __get__(self, instance, owner):",
                        "        if instance is None:",
                        "            return self",
                        "        if not hasattr(instance, self.private_name):",
                        "            setattr(instance, self.private_name, self.factory())",
                        "        return getattr(instance, self.private_name)",
                        "",
                        "class Config:",
                        "    token = LazyValue(lambda: 'secret')",
                        "",
                        "cfg = Config()",
                        "print(cfg.token)",
                    ]
                ),
            },
            {
                "title": "Read-Only",
                "code": "\n".join(
                    [
                        "class ReadOnly:",
                        "    def __init__(self, value):",
                        "        self.value = value",
                        "",
                        "    def __get__(self, instance, owner):",
                        "        return self.value",
                        "",
                        "class App:",
                        "    name = ReadOnly('lab')",
                        "",
                        "print(App().name)",
                    ]
                ),
            },
        ],
        "prompts": [
            "Make the descriptor log every set operation.",
            "Add a descriptor that enforces a max length on strings.",
            "Use one descriptor for multiple fields on a class.",
        ],
    },
    "descriptor_set_name": {
        "label": "Descriptor __set_name__",
        "examples": [
            {
                "title": "Type Enforced",
                "code": "\n".join(
                    [
                        "class StringField:",
                        "    def __set_name__(self, owner, name):",
                        "        self.public_name = name",
                        "        self.private_name = f'_{name}'",
                        "",
                        "    def __get__(self, instance, owner):",
                        "        if instance is None:",
                        "            return self",
                        "        return getattr(instance, self.private_name, '')",
                        "",
                        "    def __set__(self, instance, value):",
                        "        if not isinstance(value, str):",
                        "            raise TypeError(f'{self.public_name} must be a string')",
                        "        setattr(instance, self.private_name, value.strip())",
                        "",
                        "class Book:",
                        "    title = StringField()",
                        "    author = StringField()",
                        "",
                        "book = Book()",
                        "book.title = '  Clean Code  '",
                        "book.author = 'Robert C. Martin'",
                        "print(book.title, '-', book.author)",
                    ]
                ),
            },
            {
                "title": "Default Value",
                "code": "\n".join(
                    [
                        "class DefaultField:",
                        "    def __init__(self, default):",
                        "        self.default = default",
                        "",
                        "    def __set_name__(self, owner, name):",
                        "        self.private_name = f'_{name}'",
                        "",
                        "    def __get__(self, instance, owner):",
                        "        return getattr(instance, self.private_name, self.default)",
                        "",
                        "    def __set__(self, instance, value):",
                        "        setattr(instance, self.private_name, value)",
                        "",
                        "class Settings:",
                        "    mode = DefaultField('dev')",
                        "",
                        "print(Settings().mode)",
                    ]
                ),
            },
            {
                "title": "Track Fields",
                "code": "\n".join(
                    [
                        "class Field:",
                        "    def __set_name__(self, owner, name):",
                        "        fields = getattr(owner, '_fields', [])",
                        "        owner._fields = fields + [name]",
                        "",
                        "class Model:",
                        "    name = Field()",
                        "    age = Field()",
                        "",
                        "print(Model._fields)",
                    ]
                ),
            },
        ],
        "prompts": [
            "Allow a default value and show it when unset.",
            "Track all field names on the owner class.",
            "Add type conversion from bytes to str.",
        ],
    },
    "metaclasses": {
        "label": "Metaclasses",
        "examples": [
            {
                "title": "Register Classes",
                "code": "\n".join(
                    [
                        "class Tracker(type):",
                        "    registry = []",
                        "",
                        "    def __new__(mcls, name, bases, namespace):",
                        "        cls = super().__new__(mcls, name, bases, namespace)",
                        "        if name != 'Base':",
                        "            mcls.registry.append(cls)",
                        "        return cls",
                        "",
                        "class Base(metaclass=Tracker):",
                        "    pass",
                        "",
                        "class Alpha(Base):",
                        "    pass",
                        "",
                        "class Beta(Base):",
                        "    pass",
                        "",
                        "print([cls.__name__ for cls in Tracker.registry])",
                    ]
                ),
            },
            {
                "title": "Inject Attribute",
                "code": "\n".join(
                    [
                        "class AutoAttr(type):",
                        "    def __new__(mcls, name, bases, namespace):",
                        "        namespace['tag'] = 'auto'",
                        "        return super().__new__(mcls, name, bases, namespace)",
                        "",
                        "class Item(metaclass=AutoAttr):",
                        "    pass",
                        "",
                        "print(Item.tag)",
                    ]
                ),
            },
            {
                "title": "Modify Methods",
                "code": "\n".join(
                    [
                        "class UpperMethods(type):",
                        "    def __new__(mcls, name, bases, namespace):",
                        "        updated = {k.upper(): v for k, v in namespace.items()}",
                        "        return super().__new__(mcls, name, bases, updated)",
                        "",
                        "class Thing(metaclass=UpperMethods):",
                        "    def ping(self):",
                        "        return 'pong'",
                        "",
                        "print(Thing().PING())",
                    ]
                ),
            },
        ],
        "prompts": [
            "Auto-add a created_at attribute to classes.",
            "Enforce that subclasses implement a run method.",
            "Track class creation order and print it.",
        ],
    },
    "metaclass_validation": {
        "label": "Metaclass Validation",
        "examples": [
            {
                "title": "Require Method",
                "code": "\n".join(
                    [
                        "class InterfaceMeta(type):",
                        "    def __new__(mcls, name, bases, namespace):",
                        "        cls = super().__new__(mcls, name, bases, namespace)",
                        "        if name != 'Base' and 'run' not in namespace:",
                        "            raise TypeError(f'{name} must define run()')",
                        "        return cls",
                        "",
                        "class Base(metaclass=InterfaceMeta):",
                        "    pass",
                        "",
                        "class Worker(Base):",
                        "    def run(self):",
                        "        return 'working'",
                        "",
                        "print(Worker().run())",
                    ]
                ),
            },
            {
                "title": "Require Attribute",
                "code": "\n".join(
                    [
                        "class NamedMeta(type):",
                        "    def __new__(mcls, name, bases, namespace):",
                        "        cls = super().__new__(mcls, name, bases, namespace)",
                        "        if name != 'Base' and 'NAME' not in namespace:",
                        "            raise TypeError('NAME is required')",
                        "        return cls",
                        "",
                        "class Base(metaclass=NamedMeta):",
                        "    pass",
                        "",
                        "class Widget(Base):",
                        "    NAME = 'widget'",
                        "",
                        "print(Widget.NAME)",
                    ]
                ),
            },
            {
                "title": "Validate Methods",
                "code": "\n".join(
                    [
                        "class SignatureMeta(type):",
                        "    def __new__(mcls, name, bases, namespace):",
                        "        if name != 'Base':",
                        "            method = namespace.get('run')",
                        "            if not method or method.__code__.co_argcount != 1:",
                        "                raise TypeError('run(self) required')",
                        "        return super().__new__(mcls, name, bases, namespace)",
                        "",
                        "class Base(metaclass=SignatureMeta):",
                        "    pass",
                        "",
                        "class Runner(Base):",
                        "    def run(self):",
                        "        return 'ok'",
                        "",
                        "print(Runner().run())",
                    ]
                ),
            },
        ],
        "prompts": [
            "Require a name class attribute to be defined.",
            "Allow abstract base classes without validation.",
            "Collect violations and raise a single error message.",
        ],
    },
    "functools": {
        "label": "Functools",
        "examples": [
            {
                "title": "LRU Cache",
                "code": "\n".join(
                    [
                        "from functools import lru_cache",
                        "",
                        "@lru_cache(maxsize=None)",
                        "def fib(n):",
                        "    if n < 2:",
                        "        return n",
                        "    return fib(n - 1) + fib(n - 2)",
                        "",
                        "print(fib(10))",
                    ]
                ),
            },
            {
                "title": "Partial",
                "code": "\n".join(
                    [
                        "from functools import partial",
                        "",
                        "double = partial(lambda x, y: x * y, 2)",
                        "print(double(12))",
                    ]
                ),
            },
            {
                "title": "Reduce",
                "code": "\n".join(
                    [
                        "from functools import reduce",
                        "",
                        "numbers = [1, 2, 3, 4]",
                        "product = reduce(lambda a, b: a * b, numbers)",
                        "print(product)",
                    ]
                ),
            },
        ],
        "prompts": [
            "Use functools.singledispatch to overload a function.",
            "Write a decorator factory that takes a label.",
            "Use reduce to compute a product.",
        ],
    },
    "itertools": {
        "label": "Itertools",
        "examples": [
            {
                "title": "Product",
                "code": "\n".join(
                    [
                        "import itertools",
                        "",
                        "colors = ['red', 'green']",
                        "sizes = ['S', 'M']",
                        "print(list(itertools.product(colors, sizes)))",
                    ]
                ),
            },
            {
                "title": "Groupby",
                "code": "\n".join(
                    [
                        "import itertools",
                        "",
                        "data = [1, 1, 2, 2, 2, 3]",
                        "for key, group in itertools.groupby(data):",
                        "    print(key, list(group))",
                    ]
                ),
            },
            {
                "title": "Filterfalse",
                "code": "\n".join(
                    [
                        "import itertools",
                        "",
                        "numbers = [1, 2, 3, 4, 5, 6]",
                        "evens = list(itertools.filterfalse(lambda x: x % 2, numbers))",
                        "print('evens', evens)",
                    ]
                ),
            },
        ],
        "prompts": [
            "Use groupby to group consecutive values.",
            "Make a sliding window with islice.",
            "Generate permutations of length 2 from a list.",
        ],
    },
    "itertools_recipes": {
        "label": "Itertools Recipes",
        "examples": [
            {
                "title": "Chunked",
                "code": "\n".join(
                    [
                        "import itertools",
                        "",
                        "def chunked(iterable, size):",
                        "    it = iter(iterable)",
                        "    while True:",
                        "        chunk = list(itertools.islice(it, size))",
                        "        if not chunk:",
                        "            break",
                        "        yield chunk",
                        "",
                        "print(list(chunked(range(10), 3)))",
                    ]
                ),
            },
            {
                "title": "Pairwise",
                "code": "\n".join(
                    [
                        "import itertools",
                        "",
                        "def pairwise(iterable):",
                        "    a, b = itertools.tee(iterable)",
                        "    next(b, None)",
                        "    return zip(a, b)",
                        "",
                        "print(list(pairwise([1, 2, 3, 4])))",
                    ]
                ),
            },
            {
                "title": "Roundrobin",
                "code": "\n".join(
                    [
                        "import itertools",
                        "",
                        "def roundrobin(*iterables):",
                        "    iterables = [iter(it) for it in iterables]",
                        "    while iterables:",
                        "        for it in list(iterables):",
                        "            try:",
                        "                yield next(it)",
                        "            except StopIteration:",
                        "                iterables.remove(it)",
                        "",
                        "print(list(roundrobin('ABC', [1, 2], ('x', 'y', 'z'))))",
                    ]
                ),
            },
        ],
        "prompts": [
            "Make chunked yield tuples instead of lists.",
            "Implement roundrobin from the itertools docs.",
            "Build a windowed iterator with overlap size 2.",
        ],
    },
}
