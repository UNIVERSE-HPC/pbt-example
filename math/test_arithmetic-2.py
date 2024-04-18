import pytest
from arithmetic import add


@pytest.mark.parametrize(
    'n1, n2, expected',
    [
        (1, 2, 3),
        (5, 8, 13),
        (-4, 5, 1)
    ]
)
def test_add(n1, n2, expected):
    assert add(n1, n2) == expected
