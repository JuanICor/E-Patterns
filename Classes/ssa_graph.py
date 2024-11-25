# mypy: disable-error-code=empty-body

from __future__ import annotations
from egglog import Expr, i64Like, StringLike, i64, rewrite, vars_, var

class SSA(Expr):
    def __init__(self, value: i64Like) -> None: ...

    @classmethod
    def function(self, func_name: StringLike) -> SSA: ...

    def __add__(self, a: SSA) -> SSA: ...

    def __sub__(self, a: SSA) -> SSA: ...

@function
def load(variable: SSA) -> SSA: ...

@function
def store(variable: SSA) -> SSA:
    return variable

def istore(const: i64Like) -> SSA:
    return SSA(const)


a = var("a", SSA)
x, y = vars_("x y", i64)

def SSA_ruleset():
    yield rewrite(SSA(x) + SSA(y)).to(SSA(x + y))
    yield rewrite(SSA(x) - SSA(y)).to(SSA(x - y))
    yield rewrite(load(a)).to(a)