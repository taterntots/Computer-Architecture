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
        # self.ops = {
            # LDI: 0b10000010,
            # HLT: 0b00000001,
            # PRN: 0b01000111,
            # MUL: 0b10100010
        #     'ADD': '10100000 00000aaa 00000bbb',
        #     'SUB':  '10100001 00000aaa 00000bbb',
        #     'DIV':  '10100011 00000aaa 00000bbb',
        #     'MOD':  '10100100 00000aaa 00000bbb',

        #     'INC':  '01100101 00000rrr',
        #     'DEC':  '01100110 00000rrr',

        #     'CMP': '10100111 00000aaa 00000bbb',

        #     'AND': '10101000 00000aaa 00000bbb',
        #     'NOT': '01101001 00000rrr',
        #     'OR': '10101010 00000aaa 00000bbb',
        #     'XOR': '10101011 00000aaa 00000bbb',
        #     'SHL': '10101100 00000aaa 00000bbb',
        #     'SHR': '10101101 00000aaa 00000bbb'
        # }
        # stack pointer will need an initial value

    def ram_read(self, MAR):
        return self.ram[MAR]

    def ram_write(self, MAR, MDR):
        self.ram[MAR] = MDR

    # def op_hit(self, operand_a, operand_b):
    #     self.running = False
    #     sys.exit(1)

    def load(self):
        """Load a program into memory."""

        address = 0

        with open(sys.argv[1]) as file:
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

            operand_a = self.ram_read(self.pc+1)
            operand_b = self.ram_read(self.pc+2)

            if IR == LDI:
                self.reg[operand_a] = operand_b
                self.pc += 3

            elif IR == PRN:
                print(self.reg[operand_a])
                self.pc += 2 
            
            elif IR == MUL:
                self.alu('MUL', operand_a, operand_b)
                self.pc += 3

            elif IR == HLT:
                self.running == False