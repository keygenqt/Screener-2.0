from pathlib import Path

import click
from yaml import load, Loader

conf_name = 'screener'

default = """### Screener Configuration
---

# Folder path for save screenshot
save: {}/{}

# Cloud credentials path to file
credentials: /path/to/file/credentials.json
    
# Upload screenshot to Imgur
imgur: true
""".format(Path.home(), conf_name)


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
            print(default, file=open(p.absolute(), 'w'))

        # check path
        with open(p.absolute(), 'rb') as f:
            self.data = load(f.read(), Loader=Loader)

    def get(self, name):

        if name == 'imgur':
            if 'imgur' in self.data and isinstance(self.data[name], bool):
                return self.data[name]
            else:
                return False

        if name == 'credentials':
            if 'credentials' in self.data:
                return self.data[name]
            else:
                return ''

        if name == 'save':
            if 'save' in self.data and Path(self.data[name]).is_dir():
                return self.data[name]
            else:
                Path(self.data[name]).mkdir(parents=True, exist_ok=True)
                return self.data[name]
