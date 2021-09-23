Input =“Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing lorem ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of lorem ipsum”


Return the top 5 frequent words...

The solution as it was in the start (at the end f the interview):
```
def most_frequent(input_str: str, num_items=5):
    input_str.replace(".", "")
    input_str.replace(",", "")
    str_list = input_str.split(" ")
    
    
    result_dict = dict()
    for i in str_list:
        if i in result_dict:
            result_dict[i] = result_dict[i] + 1
        else:
            result[i] = 1
    
    del str_list
    
    result_dict = sorted(result_dict, lambda k, v: v)
    
    result = dict()
    i = 0
    for k, v in result_dict.items():
        result[k] = v
        i +=1
        if i == num_items:
            return result
    return result
```

And here's the function to test if:

```
def test_the_count():
    input = "Two Words"
    print(f"Should be an error: {most_frequent(input)}")
    
    input = "Five words exactly are here!  ? ?"
    print(f"Should be the wrong result (? ain't word): {most_frequent(input)}")
    
    input = "Five words exactly are here, they are."
    print(f"This one will work: {most_frequent(input)}")
    
    input = "Five words exactly are here, they are."
    print(f"This one will work: {most_frequent(input, 2)}")
    
    input = "Five words exactly are here, they are."
    print(f"This one will fail: {most_frequent(input, -2)}")
```

Now, this wasn't the best solution. From the outset it was proclaimed a 