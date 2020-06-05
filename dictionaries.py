from typing import Dict

simple_dict: dict = {
    'a': 0,
    'b': 1,
    'c': 3
}

cool_dict: Dict['str', int] = {
    'a': 0,
    'b': 1,
    'c': 2
}

reveal_type(simple_dict)
reveal_type(cool_dict)


class AwesomeDict(TypedDict):
    numa: int
    numb: int
    numc: int
    string: str
    isThisAwesome: bool

awesome_dict: AwesomeDict = {
    'numa': 0,
    'numb': 19,
    'numc': 84,
    'string': 'is this awesome?',
    'isThisAwesome': True
}


reveal_type(awesome_dict)
