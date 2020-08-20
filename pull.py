'''
==============
  pull-lever
==============

a subsidiary script for lever
automatically generate projects and cycles for the day
'''

from termcolor import cprint
from datetime import datetime, timedelta
import lever


def pull_report(lev):
    '''prints todays report to stdout'''
    banner = '  lever pulled: ' + datetime.today().isoformat()[:10] + '  '
    cprint('='*(len(banner)), 'green')
    cprint(banner, 'green')
    cprint('='*(len(banner)), 'green')
    print('running projects and cycles: ')
    for project in lev.data:
        cprint('project: ' + project['name'], 'blue')
        for cycle in project['cycles']:
            starts = datetime.fromisoformat(cycle['starts'])
            ends = datetime.fromisoformat(cycle['ends'])
            if datetime.today() >= starts and datetime.today() <= ends:
                if cycle['state'] == 'running':
                    cprint('-> current cycle: ' + cycle['content'])
    cprint('HAVE A MEANINGFUL DAY!', 'green')


if __name__ == "__main__":
    pull_report(lever.Lever())
