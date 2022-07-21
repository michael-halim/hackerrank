if __name__ == '__main__':
    string = input()

    arr = [False, False, False, False, False]
    for letter in string:
        if arr[0] and arr[1] and arr[2] and arr[3] and arr[4]:
            break
        if not arr[0] and letter.isalnum():
            arr[0] = True
            
        if not arr[1] and letter.isalpha():
            arr[1] = True

        if not arr[2] and letter.isdigit():
            arr[2] = True

        if not arr[3] and letter.islower():
            arr[3] = True

        if not arr[4] and letter.isupper():
            arr[4] = True
    
    for check in arr:
        print(check)