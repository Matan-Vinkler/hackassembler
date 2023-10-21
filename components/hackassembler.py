from components.instruction_parser import Parser
from components.symboltable import SymbolTable
from components.binary_code import Code

from utils.filename_handling import FileNameHandling
from utils.binary_represent import intToBin
from globals.hack_language import LABEL_SIGN, COMMENT_SIGN
from globals.hack_binary import C_STARTBITS
from globals.instruction_type import InstructionType

class HackAssembler:
    __symbolTable: SymbolTable
    __parser: Parser

    __binFileName: str
    __currentRamIndex: int
    __debugFlag: bool

    def __init__(self, filePath: str, debugFlag: bool) -> None:
        with open(filePath, "r") as self.__asmfile:
            self.__symbolTable = SymbolTable()
            self.__parser = Parser(self.__asmfile)

            self.__binFileName = FileNameHandling.asmToBin(filePath)
            self.__currentRamIndex = 16
            self.__debugFlag = debugFlag

    def firstPass(self) -> None:
        index = 0
        while self.__parser.hasMoreLines():
            insType = self.__parser.instructionType()
            if insType == InstructionType.L_INSTRUCTION:
                symbol = self.__parser.symbol()

                if not self.__symbolTable.contains(symbol):
                    self.__symbolTable.addEntry(symbol, index)
                else:
                    index += 1
            else:
                index += 1

            self.__parser.advance()

    def secondPass(self) -> None:
        code = Code()
        binIns: str

        self.__parser.reset()

        binFile = open(self.__binFileName, "a+")
        binFile.truncate(0)

        index = 0
        while self.__parser.hasMoreLines():
            insType = self.__parser.instructionType()

            if insType == InstructionType.A_INSTRUCTION:
                symbol = self.__parser.symbol()

                value: int
                if symbol.isnumeric():
                    value = int(symbol)
                elif self.__symbolTable.contains(symbol):
                    value = self.__symbolTable.getAddress(symbol)
                else:
                    value = self.__currentRamIndex
                    self.__currentRamIndex += 1

                    self.__symbolTable.addEntry(symbol, value)

                binIns = intToBin(value)

            elif insType == InstructionType.C_INSTRUCTION:
                dest, comp, jump = self.__parser.dest_comp_jump()

                compBin = code.comp(comp)
                destBin = code.dest(dest)
                jumpBin = code.jump(jump)

                binIns = C_STARTBITS + compBin + destBin + jumpBin

            if insType != InstructionType.L_INSTRUCTION:
                if self.__debugFlag:
                    print(f"{index}: {binIns} -> {self.__parser.getCurrentInstruction()}")

                binFile.write(binIns + "\n")
                index += 1

            self.__parser.advance()

        binFile.close()
        self.__asmfile.close()