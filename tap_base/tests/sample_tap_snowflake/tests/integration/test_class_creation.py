"""Test class creation."""

from tap_base.tests.sample_tap_snowflake.tap import SampleTapSnowflake


def test_tap_class():
    """Test class creation."""
    _ = SampleTapSnowflake(config=None, state=None)
