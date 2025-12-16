import string
import random
import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

@pytest.fixture()
def before_after():
    print('Before test')
    yield
    print("\nAfter test")

def test_demo1():
    assert 1 == 1


def test_demo2(before_after):
    assert 2 == 2
