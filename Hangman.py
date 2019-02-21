def hang():
    gallows = [',--;-', '| ', '| ', '| ', '| ', '| ', '|_____']
    parts = iter([' 0 ', '/', '|', '\\', ' | ', ' A ', '/ ', '\\'])
    sequence = [1, 3, 1, 1, 2]
    for i, v in enumerate(sequence, start=1):
        for k in range(v):
            gallows[i] += next(parts)
            yield '\n'.join(gallows)
    raise StopIteration
