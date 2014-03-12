from django.shortcuts import render


def truncate_value(value):
    """
    >>> truncate_value('simple test text')
    'simple tes ...
    >>> truncate_value('coisa')
    'coisa ...
    """
    return str(value)[0:10] + ' ...'
