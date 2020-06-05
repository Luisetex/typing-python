import random
from typing import Any, List, Union, TypeVar

from typing import Type

test_list = ['a', 'b', 'c', 'd', 1, 2, 3, 4]
test_str = ['a', 'b', 'c', 'd']
test_int = [1, 2, 3, 4]

def choose_random_any(list_: List[Any]) -> Any:
    return random.choice(list_)

random_choice_any = choose_random_any(test_list)

def choose_random_union(list_:  List[Any]) -> Union['str', 'int']:
    return random.choice(list_)

random_choice_union = choose_random_union(test_list)

T = TypeVar('T')

def choose_random_typevar(list_: List[T]) -> T:
    return random.choice(list_)

random_choice_typevar_mixed = choose_random_typevar(test_list)
random_choice_typevar_strs = choose_random_typevar(test_str)
random_choice_typevar_int = choose_random_typevar(test_int)


reveal_type(random_choice_any)
reveal_type(random_choice_union)
reveal_type(random_choice_typevar_mixed)
reveal_type(random_choice_typevar_strs)
reveal_type(random_choice_typevar_int)
