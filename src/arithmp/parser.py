import math
import operator
from pathlib import Path

from lark import Lark, Token, Tree

_builtins = {
    "add": operator.add,
    "sub": operator.sub,
    "mul": operator.mul,
    "div": operator.truediv,
    "mod": operator.mod,
}


class Parser:
    def __init__(self):
        self.parser = Lark(
            Path(__file__).parent.joinpath("arithmp.lark").read_text(), parser="lalr"
        )

        self._variables: dict[str, float] = {"pi": math.pi, "e": math.exp(1)}

    def _eval(self, tree: Tree[Token] | Token, variables: dict[str, float]) -> float:
        if isinstance(tree, Token):
            if tree.type == "NUMBER":
                return float(tree.value)
            else:
                raise ValueError(f"Unexpected token type: {tree.type}")
        match tree.data:
            case "number":
                return self._eval(tree.children[0], variables)
            case "add" | "sub" | "mul" | "div" | "mod":
                return _builtins[tree.data](
                    self._eval(tree.children[0], variables),
                    self._eval(tree.children[1], variables),
                )
            case "pos":
                return self._eval(tree.children[0], variables)
            case "neg":
                return -self._eval(tree.children[0], variables)
            case "power":
                return self._eval(tree.children[0], variables) ** self._eval(tree.children[1], variables)
            case "variable_assignment":
                var_name = str(tree.children[0])
                var_value = self._eval(tree.children[1],variables)
                variables[var_name]=var_value
                return var_value
            case "variable":
                var_name = str(tree.children[0])
                return variables[var_name]
            case _:
                raise ValueError(f"Unexpected tree data: {tree.data}")

    def parse(
    self,
    expression: str,
    *,
    variables: dict[str, float] | None = None
    ) -> float:
        if variables is not None:
            self._variables.update(variables)
        return self._eval(self.parser.parse(expression),self._variables)
         