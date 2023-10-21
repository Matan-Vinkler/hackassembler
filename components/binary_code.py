from globals.hack_language import *
from globals.hack_binary import *

class Code:
    __compData: dict
    __destData: dict
    __jumpData: dict

    def __init__(self) -> None:
        self.__compData = dict()
        self.__destData = dict()
        self.__jumpData = dict()

        self.__destData[DEST_NULL_1] = DEST_NULL_BIN
        self.__destData[DEST_NULL_2] = DEST_NULL_BIN
        self.__destData[DEST_M] = DEST_M_BIN
        self.__destData[DEST_D] = DEST_D_BIN
        self.__destData[DEST_DM] = DEST_DM_BIN
        self.__destData[DEST_MD] = DEST_DM_BIN
        self.__destData[DEST_A] = DEST_A_BIN
        self.__destData[DEST_AM] = DEST_AM_BIN
        self.__destData[DEST_MA] = DEST_AM_BIN
        self.__destData[DEST_AD] = DEST_AD_BIN
        self.__destData[DEST_DA] = DEST_AD_BIN
        self.__destData[DEST_ADM] = DEST_ADM_BIN

        self.__jumpData[JUMP_NULL_1] = JUMP_NULL_BIN
        self.__jumpData[JUMP_NULL_2] = JUMP_NULL_BIN
        self.__jumpData[JUMP_JGT] = JUMP_JGT_BIN
        self.__jumpData[JUMP_JEQ] = JUMP_JEQ_BIN
        self.__jumpData[JUMP_JGE] = JUMP_JGE_BIN
        self.__jumpData[JUMP_JLT] = JUMP_JLT_BIN
        self.__jumpData[JUMP_JNE] = JUMP_JNE_BIN
        self.__jumpData[JUMP_JLE] = JUMP_JLE_BIN
        self.__jumpData[JUMP_JMP] = JUMP_JMP_BIN

        self.__compData[COMP_0] = COMP_0_BIN
        self.__compData[COMP_1] = COMP_1_BIN
        self.__compData[COMP_MINUS1] = COMP_MINUS1_BIN
        self.__compData[COMP_D] = COMP_D_BIN
        self.__compData[COMP_A] = COMP_A_BIN
        self.__compData[COMP_M] = COMP_M_BIN
        self.__compData[COMP_ND] = COMP_ND_BIN
        self.__compData[COMP_NA] = COMP_NA_BIN
        self.__compData[COMP_NM] = COMP_NM_BIN
        self.__compData[COMP_MINUSD] = COMP_MINUSD_BIN
        self.__compData[COMP_MINUSA] = COMP_MINUSA_BIN
        self.__compData[COMP_MINUSM] = COMP_MINUSM_BIN
        self.__compData[COMP_DPLUS1] = COMP_DPLUS1_BIN
        self.__compData[COMP_APLUS1] = COMP_APLUS1_BIN
        self.__compData[COMP_MPLUS1] = COMP_MPLUS1_BIN
        self.__compData[COMP_DMINUS1] = COMP_DMINUS1_BIN
        self.__compData[COMP_AMINUS1] = COMP_AMINUS1_BIN
        self.__compData[COMP_MMINUS1] = COMP_MMINUS1_BIN
        self.__compData[COMP_DPLUSA] = COMP_DPLUSA_BIN
        self.__compData[COMP_DPLUSM] = COMP_DPLUSM_BIN
        self.__compData[COMP_DMINUSA] = COMP_DMINUSA_BIN
        self.__compData[COMP_DMINUSM] = COMP_DMINUSM_BIN
        self.__compData[COMP_AMINUSD] = COMP_AMINUSD_BIN
        self.__compData[COMP_MMINUSD] = COMP_MMINUSD_BIN
        self.__compData[COMP_DANDA] = COMP_DANDA_BIN
        self.__compData[COMP_DORA] = COMP_DORA_BIN
        self.__compData[COMP_DANDM] = COMP_DANDM_BIN
        self.__compData[COMP_DORM] = COMP_DORM_BIN

    def dest(self, ins: str) -> str:
        return self.__destData[ins]
    
    def comp(self, ins: str) -> str:
        return self.__compData[ins]
    
    def jump(self, ins: str) -> str:
        return self.__jumpData[ins]