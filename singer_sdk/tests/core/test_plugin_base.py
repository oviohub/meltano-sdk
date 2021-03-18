import os
from unittest import mock

from singer_sdk.helpers.typing import IntegerType, PropertiesList, Property, StringType
from singer_sdk.plugin_base import PluginBase


class PluginTest(PluginBase):
    """Example Plugin for tests."""

    name = "plugin-test"
    config_jsonschema = PropertiesList(
        Property("prop1", StringType, required=True),
        Property("prop2", IntegerType),
    ).to_dict()


def test_get_env_var_config():
    """Test settings parsing from environment variables."""

    with mock.patch.dict(
        os.environ,
        {
            "PLUGIN_TEST_prop1": "hello",
            "PLUGIN_TEST_prop3": "not-a-tap-setting",
        },
    ):
        env_config = PluginTest.get_env_var_config()
        assert env_config["prop1"] == "hello"
        assert "prop2" not in env_config
        assert "prop3" not in env_config

    no_env_config = PluginTest.get_env_var_config()
    assert "prop1" not in no_env_config
    assert "prop2" not in no_env_config
    assert "prop3" not in no_env_config