from stack_and_queue.stack import Stack
def validate_brackets(str):
    """
    this method figure out whether or not brackets in the string are balanced

    return true if opened brackets euqal the closed brackets else false 
    """
    if not len(str):
            raise Exception("Method can not be ran with an empty string")

    modified_stack = []
    last_index = len(modified_stack) - 1
    open_brackets = ["{", "(", "["]
    closed_brackets = ["}", ")", "]"]

    for character in str:
        print(character)
        if character in open_brackets:
            modified_stack.append(character)
        elif character in closed_brackets:
            if not len(modified_stack):
                return False
            if modified_stack[last_index] == "(" and character == ")":
                modified_stack.pop()
            elif modified_stack[last_index] == "{" and character == "}":
                modified_stack.pop()
            elif modified_stack[last_index] == "[" and character == "]":
                modified_stack.pop()
            else:
                return False

    if len(modified_stack) > 0:
        return False

    return True



if __name__=="__main__":
    print(ValidateBrackets("{}")) # True
    print(ValidateBrackets("{}(){}"))  # True
    print(ValidateBrackets("()[[Extra Characters]]"))  # True
    print(ValidateBrackets("(){}[[]]"))  # True
    print(ValidateBrackets("{}{Code}[Fellows](())"))  # True
    print(ValidateBrackets("[({}]"))  # False
    print(ValidateBrackets("(](")) # False
    print(ValidateBrackets("{(})")) # False
