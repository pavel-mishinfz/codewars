import unittest
from .solution import simple_assembler


class TestSimpleAssemblerInterpreter(unittest.TestCase):
    def test_simple_program(self):
        program = '''\
            mov a 5
            inc a
            dec a
            dec a
            inc a'''
        self.assertEqual(simple_assembler([item.strip() for item in program.splitlines()]), {'a': 5})

    def test_program_with_jnz(self):
        program = '''\
            mov a 5
            inc a
            dec a
            dec a
            jnz a -1
            inc a'''
        self.assertEqual(simple_assembler([item.strip() for item in program.splitlines()]), {'a': 1})

        program = '''\
            mov c 12
            mov b 0
            mov a 200
            dec a
            inc b
            jnz a -2
            dec c
            mov a b
            jnz c -5
            jnz 0 1
            mov c a'''
        self.assertEqual(
            simple_assembler([item.strip() for item in program.splitlines()]),
            {'a': 409600, 'c': 409600, 'b': 409600}
        )
