import json

import pytest
import requests
from pytest import fixture
from config import Config


def pytest_addoption(parser):
    parser.addoption(
        "--env",
        default="local",
        choices=["local", "testing", "staging"],
        help="Specify the environment in which to run the tests"
    )


@fixture(scope='session')
def env(request):
    return request.config.getoption("--env")


@pytest.fixture(scope='session')
def app_config(env):
    conf = Config(env)
    return conf

