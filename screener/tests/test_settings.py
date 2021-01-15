from unittest import TestCase

from click.testing import CliRunner

from ..__main__ import cli
from ..src.common.config import *

runner = CliRunner()
config = Config(True)


class Test(TestCase):
    # test output
    def test_update(self):
        result = runner.invoke(cli, ['settings', 'update'], obj=config)
        self.assertEqual(result.exit_code, 0)
        self.assertEqual('Specify optionals for updating. Use --help for see optionals.\n', result.output)

    # test conf value
    def test_update_value(self):
        with open(config.path) as f:
            data1 = load(f.read(), Loader=Loader)

        result = runner.invoke(cli, ['settings', 'update', '--imgur', (True, False)[data1[conf_key_imgur]]], obj=config)
        self.assertEqual(result.exit_code, 0)

        with open(config.path) as f:
            data2 = load(f.read(), Loader=Loader)

        self.assertNotEqual(data1[conf_key_imgur], data2[conf_key_imgur])
