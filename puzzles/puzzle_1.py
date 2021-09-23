# All the comments here were added after the interview
# Formatting of the input text adjucted a bit (string split for readability)
# No changes otherwise

# But of course!..
Input = "Lorem Ipsum is simply dummy text of the printing and " \
        "typesetting industry. Lorem Ipsum has been the industry standard " \
        "dummy text ever since the 1500s, when an unknown printer took a " \
        "galley of type and scrambled it to make a type specimen book. It has " \
        "survived not only five centuries, but also the leap into electronic " \
        "typesetting, remaining essentially unchanged. It was popularised in the " \
        "1960s with the release of Letraset sheets containing lorem ipsum " \
        "passages, and more recently with desktop publishing software like " \
        "Aldus PageMaker including versions of lorem ipsum"


# Return the top num_items frequent words...

def most_frequent(input_str: str, num_items=5):
    """Brute-force word frequency counter"""
    # Brute force approach to the task.
    # To call it 'sub-optimal' would be much too generous
    # You know the word "cringeworthy"?
    # This way of processing our input definitely is.
    input_str.replace(".", "")
    input_str.replace(",", "")
    str_list = input_str.split(" ") # Hopefully, we have a list of all words here
    # But in real-life situation

    # Now, this one does NOT hold the final result
    result_dict = dict()

    # Let's count word frequencies...
    # Words from this list are used as a key for a dictionary
    # And then we increment the values
    for i in str_list:
        if i in result_dict:
            result_dict[i] = result_dict[i] + 1 # The word's already there...
        else:
            result[i] = 1 # Ouch! A typo.

    del str_list

    result_dict = sorted(result_dict, lambda k, v: v)

    result = dict()
    i = 0
    for k, v in result_dict.items():
        result[k] = v
        i += 1
        if i == num_items:
            return result
    return result

# This function is a test suite for a previous one
# Outputs are pretty much self-explanatory
def test_the_count():
    input = "Two Words"
    print(f"Should be an error: {most_frequent(input)}") # Out default number of items is 5 – KeyError expected

    input = "Five words exactly are here!  ? ?"
    print(f"Should be the wrong result (? ain't a word): {most_frequent(input)}") # ? is definitely not a word

    input = "Five words exactly are here, they are."
    print(f"This one will work: {most_frequent(input)}") # Spoiler: It won't before we refactor most_frequent()

    input = "Five words exactly are here, they are."
    print(f"This one will work: {most_frequent(input, 2)}") # Spoiler: It won't before we refactor most_frequent()

    input = "Five words exactly are here, they are."
    print(f"This one will fail: {most_frequent(input, -2)}") # Returned values would be wrong...
    # ... as we do not check for negatives. Sanitize your inputs, folks!
