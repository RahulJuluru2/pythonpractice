from src.example.main import hello

def test_hello():
    assert hello("World") == "Hello, World!"
    assert hello("Alice") == "Hello, Alice!"
