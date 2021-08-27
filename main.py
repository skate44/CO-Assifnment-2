# Main Part of the Program

from Memory import Memory
from RegisterFile import RegisterFile
from ExectutionEngine import ExectutionEngine
from ProgramCounter import ProgramCounter


def main():
    memory = Memory()
    registerFile = RegisterFile()
    exectuionEngine = ExectutionEngine(memory, registerFile)
    PC = ProgramCounter(0)
    halted = False
    cycle = 0

    while not halted:
        inst = memory.fetch(PC.getval(), cycle)
        halted, nextPC = exectuionEngine.execute(inst, cycle)
        PC.dump()
        registerFile.dump()
        PC.update(nextPC)
        cycle += 1

    memory.dump()
    memory.showTraces()

if __name__ == '__main__':
    main()
