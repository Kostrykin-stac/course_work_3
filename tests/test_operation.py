import pytest
from src.operation import masking_card


@pytest.fixture
def test_masking_card():
    result = masking_card("Maestro 1234567890123456")
    assert result == "Maestro 1234 56** **** 3456"


def test_masking_card_1():
    result = masking_card("Счет 12345678901234567890")
    assert result == "Счет 1234 56** **** 7890"


def test_masking_invalid_card_info():
    result = masking_card("Invalid Card Info")
    assert result == "Uncorrected card_info"


def test_masking_empty_input():
    result = masking_card("")
    assert result == ""
