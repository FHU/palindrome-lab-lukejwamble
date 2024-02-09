#REMOVE PASS AND FIX THIS FUNCTION
def palindrome(word):
    backwards = word[::-1]

    if word == backwards and word != "":
        return True
    else:
        return False

#YOUR CODE GOES HERE
if __name__ == "__main__":
    print(palindrome(input().lower().replace(" ", "")))
