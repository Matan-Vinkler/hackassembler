from globals.predefined_symbols import *
from globals.predefined_symbol_values import *

class SymbolTable:
    __table: dict

    def __init__(self) -> None:
        self.__table = dict()

        self.__table[R0_SYMBOL] = R0_VALUE
        self.__table[R1_SYMBOL] = R1_VALUE
        self.__table[R2_SYMBOL] = R2_VALUE
        self.__table[R3_SYMBOL] = R3_VALUE
        self.__table[R4_SYMBOL] = R4_VALUE
        self.__table[R5_SYMBOL] = R5_VALUE
        self.__table[R6_SYMBOL] = R6_VALUE
        self.__table[R7_SYMBOL] = R7_VALUE
        self.__table[R8_SYMBOL] = R8_VALUE
        self.__table[R9_SYMBOL] = R9_VALUE
        self.__table[R10_SYMBOL] = R10_VALUE
        self.__table[R11_SYMBOL] = R11_VALUE
        self.__table[R12_SYMBOL] = R12_VALUE
        self.__table[R13_SYMBOL] = R13_VALUE
        self.__table[R14_SYMBOL] = R14_VALUE
        self.__table[R15_SYMBOL] = R15_VALUE

        self.__table[SP_SYMBOL] = SP_VALUE
        self.__table[LCL_SYMBOL] = LCL_VALUE
        self.__table[ARG_SYMBOL] = ARG_VALUE
        self.__table[THIS_SYMBOL] = THIS_VALUE
        self.__table[THAT_SYMBOL] = THAT_VALUE

        self.__table[SCREEN_SYMBOL] = SCREEN_VALUE
        self.__table[KBD_SYMBOL] = KBD_VALUE

    def addEntry(self, symbol: str, address: int) -> None:
        self.__table[symbol] = address

    def contains(self, symbol: str) -> bool:
        return symbol in self.__table.keys()

    def getAddress(self, symbol: str) -> int:
        return self.__table[symbol]