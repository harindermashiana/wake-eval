from agenticlearning.budget import estimate_tokens


def test_estimate_tokens():
    assert estimate_tokens("") == 0
    assert estimate_tokens("Hello, world!") == 3
    assert estimate_tokens("This is a test.") == 3
