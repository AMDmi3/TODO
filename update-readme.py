#!/usr/bin/env python3

dashboard_projects = [
    {'gha': 'AMDmi3', 'ghp': 'findmaildirs', 'rpl': 'findmaildirs'},
    #{'gha': 'AMDmi3', 'ghp': 'glosm', 'rpl': 'glosm'},
    {'gha': 'AMDmi3', 'ghp': 'hoverboard-sdl', 'rpl': 'hoverboard'},
    {'gha': 'AMDmi3', 'ghp': 'jsonslicer', 'rpl': 'python:jsonslicer', 'pypi': 'jsonslicer'},
    #{'gha': 'AMDmi3', 'ghp': 'kiconvtool', 'rpl': 'kiconvtool'},
    {'gha': 'libSDL2pp', 'ghp': 'libSDL2pp', 'rpl': 'libsdl2pp' },
    {'gha': 'repology', 'ghp': 'libversion', 'rpl': 'libversion'},
    #{'gha': 'AMDmi3', 'ghp': 'opendaed', 'rpl': 'opendaed'},
    #{'gha': 'AMDmi3', 'ghp': 'openstrike', 'rpl': 'openstrike'},
    #{'gha': 'AMDmi3', 'ghp': 'planetonomy', 'rpl': 'planetonomy'},
    {'gha': 'repology', 'ghp': 'py-libversion', 'rpl': 'python:libversion', 'pypi': 'libversion'},
    {'gha': 'AMDmi3', 'ghp': 'qnetwalk', 'rpl': 'qnetwalk'},
    #{'gha': 'AMDmi3', 'ghp': 'ssdaligntest', 'rpl': 'ssdaligntest'},
    #{'gha': 'AMDmi3', 'ghp': 'streetmangler', 'rpl': 'streetmangler'},
    {'gha': 'AMDmi3', 'ghp': 'tiletool', 'rpl': 'tiletool'},
    #{'gha': 'AMDmi3', 'ghp': 'tspell', 'rpl': 'tspell'},
]

def print_dashboard(file):
    print('| Project | ★ | Build | Release | Commits | Packaging |', file=file)
    print('|---------|---|-------|---------|---------|-----------|', file=file)

    for project in dashboard_projects:
        ghp = project.get('ghp')
        gha = project.get('gha')
        rpl = project.get('rpl')
        pypi = project.get('pypi')

        cells = []
        cells.append(f'[{ghp}](https://github.com/{gha}/{ghp})')
        cells.append(f'[![GitHub stars](https://img.shields.io/github/stars/{gha}/{ghp}.svg?label=)](https://github.com/{gha}/{ghp})')
        cells.append(f'[![Build Status](https://travis-ci.org/{gha}/{ghp}.svg?branch=master&label=)](https://travis-ci.org/{gha}/{ghp})')
        cells.append(f'[![GitHub release](https://img.shields.io/github/release/{gha}/{ghp}.svg?label=)](https://github.com/{gha}/{ghp}/releases)')
        if pypi:
            cells[-1] += f' [![PyPI version](https://img.shields.io/pypi/v/{pypi}.svg)](https://pypi.org/project/{pypi}/)'
        cells.append(f'[![Github commits (since latest release)](https://img.shields.io/github/commits-since/{gha}/{ghp}/latest.svg?label=)](https://github.com/{gha}/{ghp}/commits/master)')
        cells.append(f'[![Packaging status](https://repology.org/badge/vertical-allrepos/{rpl}.svg?header=)](https://repology.org/project/{rpl}/versions)')
        print('| ' + ' | '.join(cells) + ' |', file=file)

#| [jsonslicer](https://github.com/AMDmi3/jsonslicer) | [![Build Status](https://travis-ci.org/AMDmi3/jsonslicer.svg?branch=master)](https://travis-ci.org/AMDmi3/jsonslicer) | ![GitHub release](https://img.shields.io/github/release/AMDmi3/jsonslicer.svg) | [![Github commits (since latest release)](https://img.shields.io/github/commits-since/AMDmi3/jsonslicer/latest.svg)](https://github.com/AMDmi3/jsonslicer) | [![Packaging status](https://repology.org/badge/vertical-allrepos/python:jsonslicer.svg)](https://repology.org/project/python:jsonslicer/versions) |

with open('README.md') as readme:
    lines = [line.strip() for line in readme]

with open('README.md', 'w') as readme:
    in_dashboard = False
    for line in lines:
        if line == '## Project status dashboard':
            in_dashboard = True
            print(line + '\n', file=readme)
            print_dashboard(file=readme)
            print('', file=readme)
        elif line.startswith('#'):
            in_dashboard = False
            print(line, file=readme)
        elif not in_dashboard:
            print(line, file=readme)
