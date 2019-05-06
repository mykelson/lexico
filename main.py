def main():
    """ Main function """

    first_string = input("Please enter the first string: ")
    print(f"{rearrangeWord(first_string)}")


def rearrangeWord(word):
    """ Rearrange the word, stating it's next lexicographically greater word """

    n = 0
    m = 0
    result = []

    # Convert the string into a list.
    for n in range(len(word)):
        result.append(word[n])

    # Rearrange the list
    for m in range(len(result)):
        if (m+1) >= len(result):
            return "no answers"

        if result[m] < result[m+1]:
            # Swap.
            result[m], result[m+1] = result[m+1], result[m]

            # Convert the list back into a string before returning it.
            return list_to_string(result)
       

def list_to_string(a):
    """ Convert a list into a string """

    res = ''.join(a)

    return res


if __name__ == "__main__":
    main()