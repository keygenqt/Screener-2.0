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
        result = runner.invoke(cli, ['settings', 'update', '--imgur', False], obj=config)
        self.assertEqual(result.exit_code, 0)

        with open(config.path.absolute()) as f:
            self.data = load(f.read(), Loader=Loader)
            f.close()

        self.assertEqual(False, self.data[conf_key_imgur])
