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

def test_demo1():
    assert 1 == 1


def test_demo2():
    assert 2 == 2

