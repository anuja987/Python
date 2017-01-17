def find_substring():
    small_str = "how"
    list_str = ["abc","hi how are you","fantastic, how about you?"]
    for value in list_str:
        if small_str in value:
            print 'string is substring of s'
        else:
            print 'string is not substring of s'
    return

if __name__=="__main__":
    print(find_substring())
