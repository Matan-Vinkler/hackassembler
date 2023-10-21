from globals.hack_language import COMMENT_SIGN

def remove_comments(text_ins: str) -> str:
    comment_index = text_ins.find(COMMENT_SIGN)
    if comment_index != -1:
        return text_ins[:comment_index]
    else:
        return text_ins