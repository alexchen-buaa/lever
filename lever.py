'''
===========================
  "lever" project manager
===========================

This is a cli tool that helps keep everyday projects in order.
All parameters are passed in str format.
Assume that the final days are within the corresponding cycles.
'''

import json
import sys
from termcolor import cprint
from datetime import datetime, timedelta


class Lever():

    """All basic operations of lever."""

    def __init__(self):
        with open('/Users/alexchen/local/toolbox/lever/database.json', 'r') as database:
            try:
                self.data = json.load(database)
            except json.decoder.JSONDecodeError:
                # except when the database is empty
                self.data = []
        assert isinstance(self.data, list)
        with open('/Users/alexchen/local/toolbox/lever/log.json', 'r') as log:
            try:
                self.log = json.load(log)
            except json.decoder.JSONDecodeError:
                # except when the log is empty
                self.log = {'log': [], 'stat': []}
        assert isinstance(self.log, dict)

    def add_log(self, event, content):
        '''automatic logging'''
        self.log['log'].append({'time': datetime.today().isoformat(),
                                'event': event,
                                'content': content})

    def add_stat(self):
        '''automatic statistics'''
        # numc = sum([len(project['cycles']) for project in self.data])
        numc, numcrun, numccom = 0, 0, 0
        tct = timedelta(0)
        for project in self.data:
            for cycle in project['cycles']:
                numc += 1
                if cycle['state'] == 'running':
                    numcrun += 1
                elif cycle['state'] == 'completed':
                    numccom += 1
                endstime = datetime.fromisoformat(cycle['ends'])
                startstime = datetime.fromisoformat(cycle['starts'])
                tct += (endstime - startstime)
        self.log['stat'].append({'time': datetime.today().isoformat(),
                                 'number of projects': len(self.data),
                                 'number of cycles': numc,
                                 'number of running cycles': numcrun,
                                 'number of completed cycles': numccom,
                                 'total cycle time': str(tct)})

    def add_project(self, namep):
        '''add a single project to the lever (unsaved)'''
        self.data.append({'name': namep, 'cycles': []})
        self.add_log('add_project', namep)

    def remove_project(self, nump):
        '''remove a single project on lever (unsaved)'''
        confirm = input('remove project ' + nump + '? [y/n]')
        if confirm == 'y':
            project = self.data.pop(int(nump) - 1)
            self.add_log('remove_project', project['name'])

    def list_project(self):
        '''list all project name'''
        print('========================')
        print('  list of all projects  ')
        print('========================')
        for i in range(len(self.data)):
            print(str(i + 1) + '. ' + self.data[i]['name'] + ', ', end='')
            print(str(len(self.data[i]['cycles'])) + ' cycles;')

    def add_cycle(self, nump):
        '''add a single cycle to the given project
        the starts and ends params are datetime in ISO 8601 format
        there are three states: running, completed and halt'''
        starts = input('starts: ')
        ends = input('ends: ')
        content = input('content: ')
        cycle = {'starts': starts,
                 'ends': ends,
                 'content': content,
                 'state': 'running'}
        self.data[int(nump) - 1]['cycles'].append(cycle)
        self.add_log('add_cycle', cycle['content'])

    def remove_cycle(self, nump, numc):
        '''remove a single cycle of the given project'''
        confirm = input('delete cycle ' + numc +
                        ' of project ' + nump + '? [y/n]')
        if confirm == 'y':
            cycle = self.data[int(nump) - 1]['cycles'].pop(int(numc) - 1)
            self.add_log('remove_cycle', cycle['content'])

    def list_cycle(self, nump):
        '''list all cycles of the give project'''
        if int(nump) > len(self.data):
            cprint('error: index does not exist', 'red')
        else:
            banner = '  list of cycles of project ' + nump + '  '
            print('=' * len(banner))
            print(banner)
            print('=' * len(banner))
            for i in range(len(self.data[int(nump) - 1]['cycles'])):
                print(str(i + 1) + '. ', end='')
                print(self.data[int(nump) - 1]['cycles'][i])

    def halt_cycle(self, nump, numc):
        '''halt a cycle of the given project'''
        if int(nump) > len(self.data):
            cprint('error: index does not exist', 'red')
        elif int(numc) > len(self.data[int(nump) - 1]):
            cprint('error: index does not exist', 'red')
        else:
            self.data[int(nump) - 1]['cycles'][int(numc) - 1]['state'] = 'halt'

    def continue_cycle(self, nump, numc):
        '''continue a cycle of the given project'''
        if int(nump) > len(self.data):
            cprint('error: index does not exist', 'red')
        elif int(numc) > len(self.data[int(nump) - 1]):
            cprint('error: index does not exist', 'red')
        else:
            run = 'running'
            self.data[int(nump) - 1]['cycles'][int(numc) - 1]['state'] = run

    def toggle_cycle(self, nump, numc):
        '''toggle a cycle's state (between running and halt)'''
        state = self.data[int(nump) - 1]['cycles'][int(numc) - 1]['state']
        if state == 'halt':
            self.continue_cycle(nump, numc)
        elif state == 'running':
            self.halt_cycle(nump, numc)

    def save(self):
        '''save changes to the database and log'''
        with open('/Users/alexchen/local/toolbox/lever/database.json', 'w') as database:
            json.dump(self.data, database)
        with open('/Users/alexchen/local/toolbox/lever/log.json', 'w') as log:
            json.dump(self.log, log)

    def reset(self):
        '''reset lever, for debugging use'''
        confirm = input('reset lever? [y/n] ')
        if confirm == 'y':
            self.data = []
            self.log = {'log': [], 'stat': []}
            self.save()

    def check_state(self):
        '''check the state of all cycles in lever'''
        print('checking states...')
        cnt = 0
        for project in self.data:
            for cycle in project['cycles']:
                if datetime.fromisoformat(cycle['ends']) < datetime.today():
                    cycle['state'] = 'completed'
                    cnt += 1
        if cnt != 0:
            print(str(cnt) + ' cycle(s) completed')

    def parse_statement(self, statement):
        '''parse a single statement into corresponding function execution'''
        stup = statement.split()
        try:
            if len(stup) == 0:
                pass
            elif stup[0] == 'add':
                if stup[1] == 'p':
                    self.add_project(stup[2])
                elif stup[1] == 'c':
                    self.add_cycle(stup[2])
                else:
                    cprint('error: invalid syntax', 'red')
            elif stup[0] == 'ls':
                if stup[1] == 'p':
                    self.list_project()
                elif stup[1] == 'c':
                    self.list_cycle(stup[2])
                else:
                    cprint('error: invalid syntax', 'red')
            elif stup[0] == 'rm':
                if stup[1] == 'p':
                    self.remove_project(stup[2])
                elif stup[1] == 'c':
                    self.remove_cycle(stup[2], stup[3])
                else:
                    cprint('error: invalid syntax', 'red')
            elif stup[0] == 'tog':
                self.toggle_cycle(stup[1], stup[2])
            elif stup[0] == 'save':
                self.save()
            elif stup[0] == 'reset':
                self.reset()
            elif stup[0] == 'stat':
                self.add_stat()
            elif stup[0] == 'help':
                cprint('syntax: <operation> <object> [<params> [...]]', 'blue')
            elif stup[0] == 'exit':
                sys.exit()
            else:
                cprint('error: invalid syntax', 'red')
        except IndexError:
            cprint('error: index does not exist', 'red')


def mainloop():
    '''main function for lever'''
    # print('Lever 0.0.1')
    cprint('Lever 0.0.2', 'green')
    print('created by Alex Chen')
    print('Type help for more information')
    boot = True
    while True:
        if boot:
            lever = Lever()
            lever.check_state()
            boot = False
        cprint('> ', 'green', end='')
        lever.parse_statement(input())


if __name__ == "__main__":
    mainloop()
