import pandas as pd

class Tab:
    file = "test.txt"

test = pd.Series([Tab(), Tab()],
    name = 'tab',
    index = ['riff1', 'riff2'])



tabs = pd.Series([Tab(), Tab(), Tab(), Tab(), Tab()],
    name = 'tab',
    index = ['intro', 'verse', 'chorus', 'bridge', 'solo riff'])

solo = pd.Series(['build-up', 'sweeps', 'melodic triplets', 'bluesy triplets'])

df = {
        'index':['r1-A', 'r1-B', 'r2', 'r3', 'r4', 'r5'],
        'cols': [
            { 'name': 'song part',
              'data': [1, 2, 3, 4, 5, 6]}
        ]   
    }

df