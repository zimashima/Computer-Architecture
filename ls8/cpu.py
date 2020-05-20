"""CPU functionality."""

import sys

class CPU:
    """Main CPU class."""

    #day 1 code
    #load immedirate (save the value)
    #constructing cpu and other functions
    
    def __init__(self):
        self.ram =  [0] * 256               # 256 bytes of memories
        self.reg = [0] * 8                  # 8 registers
        self.pc = 0                         # program counter
        self.halted = False                 # halt

    def ram_read(self, mar):               # MAR (Memory Address Register)
        return self.ram[mar]               # contains address being read or written to

    def ram_write(self, mdr, mar):         # MDR (Memory Data Register)
        self.ram[mar] = mdr                # data that was read or data to write
            
    def LDI(self):                          # store a value in a register
        self.reg[self.ram_read(self.pc+1)] = self.ram_read(self.pc+2)
        self.pc += 3
                              
    def PRN(self):                     # print value in a register
        print(f'value: {self.reg[self.ram_read(self.pc+1)]}')
        self.pc += 2
    
    def HLT(self):                          # Halt
        self.halted = True
        self.pc += 1

    def MUL(self):
        self.alu("MUL", self.ram_read(self.pc+1), self.ram_read(self.pc+2))
        self.pc +=3

    def run(self):                          # Run the CPU

        #hash table because it's cooler than if-elif
        run_instruction = {
            162: self.MUL(),
            131: self.LDI(),
            71: self.PRN(),
            1: self.HLT()
        }

        while not self.halted:
            IR = self.ram_read(self.pc)     # Instruction Register (IR)
            run_instruction[IR]
            print(IR)
            print(run_instruction[IR])
        self.halted = True

    def load(self):
        address = 0
        with open(sys.argv[1]) as func:
            for line in func:
                string_val = line.split("#")[0].strip()
                if string_val == '':
                    continue
                v = int(string_val, 2)
                self.ram[address] = v
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


