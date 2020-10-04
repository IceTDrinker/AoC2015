from enum import Enum
from pathlib import Path

content = None
with open(f"exercise_and_input/{Path(__file__).with_suffix('').name}/input.txt", "r") as f:
    content = f.readlines()


class InputType(Enum):
    AND = 0
    OR = 1
    NOT = 2
    LSHIFT = 3
    RSHIFT = 4
    CONST = 5


class Input:
    def __init__(self, input_dict, input_type, input_parameter_1, input_parameter_2=None) -> None:
        self.input_dict = input_dict
        self.input_type = input_type
        self.input_parameter_1 = input_parameter_1
        self.input_parameter_2 = input_parameter_2

        self.value = None

    def eval(self):
        if self.value is not None:
            return self.value

        input_parameter_1_value = None
        try:
            input_parameter_1_value = int(self.input_parameter_1)
        except ValueError:
            input_parameter_1_value = self.input_dict[self.input_parameter_1].eval()

        input_parameter_2_value = None
        if self.input_parameter_2 is not None:
            try:
                input_parameter_2_value = int(self.input_parameter_2)
            except ValueError:
                input_parameter_2_value = self.input_dict[self.input_parameter_2].eval()

        if self.input_type == InputType.AND:
            self.value = input_parameter_1_value & input_parameter_2_value
        elif self.input_type == InputType.OR:
            self.value = input_parameter_1_value | input_parameter_2_value
        elif self.input_type == InputType.NOT:
            self.value = ~input_parameter_1_value
        elif self.input_type == InputType.LSHIFT:
            self.value = input_parameter_1_value << input_parameter_2_value
        elif self.input_type == InputType.RSHIFT:
            self.value = input_parameter_1_value >> input_parameter_2_value
        elif self.input_type == InputType.CONST:
            self.value = input_parameter_1_value

        return self.value


input_dictionary = {}

for line in content:
    line = line.strip()
    input_operation, output_name = line.split(" -> ")

    if "AND" in input_operation:
        op1, op2 = input_operation.split(" AND ")
        input_dictionary[output_name] = Input(input_dictionary, InputType.AND, op1, op2)
    elif "OR" in input_operation:
        op1, op2 = input_operation.split(" OR ")
        input_dictionary[output_name] = Input(input_dictionary, InputType.OR, op1, op2)
    elif "NOT" in input_operation:
        op1 = input_operation.replace("NOT ", "", 1)
        input_dictionary[output_name] = Input(input_dictionary, InputType.NOT, op1)
    elif "LSHIFT" in input_operation:
        op1, op2 = input_operation.split(" LSHIFT ")
        input_dictionary[output_name] = Input(input_dictionary, InputType.LSHIFT, op1, int(op2))
    elif "RSHIFT" in input_operation:
        op1, op2 = input_operation.split(" RSHIFT ")
        input_dictionary[output_name] = Input(input_dictionary, InputType.RSHIFT, op1, int(op2))
    else:
        input_dictionary[output_name] = Input(input_dictionary, InputType.CONST, input_operation)

a_wire_value = input_dictionary["a"].eval()
print(f"Value in wire a : {a_wire_value}")

for _, v in input_dictionary.items():
    v.value = None

input_dictionary["b"].value = a_wire_value
new_a_wire_value = input_dictionary["a"].eval()
print(f"Value in wire a : {new_a_wire_value}")
