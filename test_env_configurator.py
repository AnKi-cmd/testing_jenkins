import pytest
import os
from src.configurator.env_configurator import *

test = ENVConfigurator()

#вввkkdddd

def test_get_env_var_by_name():
    for variants in os.environ.keys():
        assert test.get_env_var_by_name(variants) == os.environ.get(variants)
    with pytest.raises(Exception) as err:
        test.get_env_var_by_name("nothing")
    assert "ConfiguratorKeyError" in str(err)


