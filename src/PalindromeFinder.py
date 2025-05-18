def check_if_palindrome(palindrome):
    is_palindrome = True
    for i in range(0, len(palindrome)):
        if palindrome[i] != palindrome[len(palindrome) - 1 - i]:
            is_palindrome = False
            break
    return  is_palindrome
