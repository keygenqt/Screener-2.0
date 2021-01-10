from unittest import TestCase
from click.testing import CliRunner

from ..app.db import initdb


class Test(TestCase):
    def test_initdb1(self):
        runner = CliRunner()
        result = runner.invoke(initdb, ['test'])
        self.assertEqual(result.exit_code, 0)
        self.assertEqual(result.output, 'Hello test!\n')

    def test_initdb2(self):
        runner = CliRunner()
        result = runner.invoke(initdb, ['--count=2', 'test'])
        print(result.runner)
        print(result.output)
        self.assertEqual(result.exit_code, 0)
        self.assertEqual(result.output, 'Hello test!\nHello test!\n')
