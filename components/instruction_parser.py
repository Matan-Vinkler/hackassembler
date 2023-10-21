from utils.comment_remove import remove_comments

from globals.instruction_type import InstructionType
from globals.hack_language import AT_SIGN, LABEL_SIGN, EQUAL_SIGN, JUMP_SIGN, COMMENT_SIGN

class Parser:
    __insData: dict[str, str]
    __currentIns: str
    __currentInsIndex: int

    def __init__(self, file) -> None:
        self.__insData = [remove_comments(line.strip()).strip() for line in file if remove_comments(line.strip()).strip() != ""]

        self.__currentInsIndex = 0
        self.__currentIns = self.__insData[self.__currentInsIndex]

    def hasMoreLines(self) -> bool:
        return self.__currentInsIndex < len(self.__insData)

    def advance(self) -> None:
        self.__currentInsIndex += 1
        if self.hasMoreLines():
            self.__currentIns = self.__insData[self.__currentInsIndex]

    def reset(self) -> None:
        self.__currentInsIndex = 0
        self.__currentIns = self.__insData[self.__currentInsIndex]

    def getCurrentInstruction(self) -> str:
        return self.__insData[self.__currentInsIndex]

    def instructionType(self) -> InstructionType:
        if self.__currentIns.startswith(AT_SIGN):
            return InstructionType.A_INSTRUCTION
        elif self.__currentIns.startswith(LABEL_SIGN):
            return InstructionType.L_INSTRUCTION
        
        return InstructionType.C_INSTRUCTION


    def symbol(self) -> str:
        # Should be called if A_INSTRUCTION or L_INSTRUCTION

        if(self.instructionType() == InstructionType.L_INSTRUCTION):
            return self.__currentIns[1:-1]

        return self.__currentIns[1:]

    def dest_comp_jump(self) -> tuple[str, str, str]:
        # Should be called if C_INSTRUCTION

        ins = Parser.insHelper(self.__currentIns)

        components = ins.split(EQUAL_SIGN)
        dest = components[0]

        comp_jump = components[1].split(JUMP_SIGN)
        comp = comp_jump[0]
        jump = comp_jump[1]

        return (dest, comp, jump)
    
    @staticmethod
    def insHelper(ins: str) -> str:
        if ins.find(EQUAL_SIGN) == -1:
            ins = EQUAL_SIGN + ins

        if ins.find(JUMP_SIGN) == -1:
            ins = ins + JUMP_SIGN

        return ins