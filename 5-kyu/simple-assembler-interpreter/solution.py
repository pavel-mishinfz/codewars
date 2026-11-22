def simple_assembler(program):
    i = 0
    registers = {}
    while i < len(program):
        stmt = program[i]
        stmt_as_list = stmt.split()
        cmd, register = stmt_as_list[0], stmt_as_list[1]
        if len(stmt_as_list) == 3:
            value = stmt_as_list[2]
            try:
                value = int(value)
            except ValueError:
                value = registers[value]
        if cmd == 'mov':
            registers[register] = value
        elif cmd == 'inc':
            registers[register] += 1
        elif cmd == 'dec':
            registers[register] -= 1
        elif cmd == 'jnz':
            if (register.isdigit() and register != 0) or registers[register] != 0:
                i += value
                continue
        i += 1
    return registers