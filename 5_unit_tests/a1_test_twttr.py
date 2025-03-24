from a1_twttr import convert
import pytest

def test_convert():
    assert convert("twitter") == "twttr"

def test_convert_upper():
    assert convert ("APPA") == "PP"

