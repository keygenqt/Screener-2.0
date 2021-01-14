from pathlib import Path

import click
from yaml import Loader
from yaml import load

conf_name = 'screener'

default = """### Screener Configuration
---

# Folder path for save screenshot
save: {}

# Cloud credentials path to file
credentials: {}
    
# Upload screenshot to Imgur
imgur: {}
"""

conf_key_save = 'save'
conf_key_credentials = 'credentials'
conf_key_imgur = 'imgur'

conf_default_save = '{}/{}'.format(Path.home(), conf_name)
conf_default_credentials = '/path/to/file/credentials.json'
conf_default_imgur = 'true'


class Config:
    def __init__(self, dev=False):
        # dev - path info project yml conf
        if not dev:
            home = str(Path.home())
        else:
            home = str(Path(__file__).cwd())

        # check path
        p = Path('{}/.{}.yml'.format(home, conf_name))
        if not p.is_file():
            p = Path('{}/{}.yml'.format(home, conf_name))
        if not p.is_file():
            click.echo(click.style("\nAdded default config. {}\nPlease configure the application.\n".format(p.absolute()), fg="yellow"))
            print(default.format(
                conf_default_save,
                conf_default_credentials,
                conf_default_imgur
            ), file=open(p.absolute(), 'w'))

        self.path = p

        with open(p.absolute(), 'rb') as f:
            self.data = load(f.read(), Loader=Loader)

    def get(self, name):

        if name == conf_key_imgur:
            if conf_key_imgur in self.data and isinstance(self.data[name], bool):
                return self.data[name]
            else:
                return False

        if name == conf_key_credentials:
            if conf_key_credentials in self.data:
                return self.data[name]
            else:
                return ''

        if name == conf_key_save:
            if conf_key_save in self.data and Path(self.data[name]).is_dir():
                return self.data[name]
            else:
                Path(self.data[name]).mkdir(parents=True, exist_ok=True)
                return self.data[name]

    def update(self, name, value):
        self.data[name] = value
        print(default.format(
            self.data[conf_key_save],
            self.data[conf_key_credentials],
            str(self.data[conf_key_imgur]).lower(),
        ), file=open(self.path.absolute(), 'w'))

    def reload(self):
        with open(self.path.absolute(), 'rb') as f:
            self.data = load(f.read(), Loader=Loader)
