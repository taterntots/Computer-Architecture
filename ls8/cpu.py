"""CPU functionality."""

import sys

LDI = 0b10000010
HLT = 0b00000001
PRN = 0b01000111
MUL = 0b10100010

class CPU:
    """Main CPU class."""

    def __init__(self):
        """Construct a new CPU."""
        self.reg = [0] * 8
        self.pc = 0
        self.ram = [0] * 256
        self.running = True
        self.branchtable = {}
        self.branchtable[LDI] = self.handle_LDI
        self.branchtable[HLT] = self.handle_HLT
        self.branchtable[PRN] = self.handle_PRN
        self.branchtable[MUL] = self.handle_MUL
        # stack pointer will need an initial value

    def ram_read(self, MAR):
        return self.ram[MAR]

    def ram_write(self, MAR, MDR):
        self.ram[MAR] = MDR

    def handle_LDI(self, operand_a, operand_b):
        self.reg[operand_a] = operand_b
        self.pc += 3

    def handle_HLT(self, operand_a, operand_b):
        self.running == False

    def handle_PRN(self, operand_a, operand_b):
        print(self.reg[operand_a])
        self.pc += 2 

    def handle_MUL(self, operand_a, operand_b):
        self.alu('MUL', operand_a, operand_b)
        self.pc += 3

    def load(self, filename):
        """Load a program into memory."""

        address = 0

        with open(filename) as file:
            for line in file:
                string_val = line.split('#')[0].strip()
                if string_val == '':
                    continue
                else:
                    value = int(string_val, 2)
                    self.ram[address] = value
                    address += 1

    def alu(self, op, reg_a, reg_b):
        """ALU operations."""

        if op == "ADD":
            self.reg[reg_a] += self.reg[reg_b]
        elif op == "MUL":
            self.reg[reg_a] *= self.reg[reg_b]
        else:
            raise Exception("Unsupported ALU operation")

    def trace(self):
        """
        Handy function to print out the CPU state. You might want to call this
        from run() if you need help debugging.
        """

        print(f"TRACE: %02X | %02X %02X %02X |" % (
            self.pc,
            #self.fl,
            #self.ie,
            self.ram_read(self.pc),
            self.ram_read(self.pc + 1),
            self.ram_read(self.pc + 2)
        ), end='')

        for i in range(8):
            print(" %02X" % self.reg[i], end='')

        print()

    def run(self):
        """Run the CPU."""
        self.trace()

        while self.running:
            # IR is the instruction register
            IR = self.ram_read(self.pc)
            # print(IR)

            operand_a = self.ram_read(self.pc+1)
            operand_b = self.ram_read(self.pc+2)

            if IR == HLT:
                self.running = False
            else:
                self.branchtable[IR](operand_a, operand_b)