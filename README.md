### Getting Started

To get started with using the `astrie` package, follow these steps:

1. **Installation**

    Install the package using pip:
    ```bash
    pip install astrie
    ```

2. **Importing**

    Import the `AsTrie` class from the `astrie` module:
    ```python
    from astrie import AsTrie
    ```

3. **Object Initialization**

    Initialize an instance of the `AsTrie` class:
    ```python
    trie = AsTrie()
    ```

### Methods

#### Adding Words

To add words to the trie, you can use the following methods:

- To add a single word:
    ```python
    trie.add("Python")
    ```

- To add a list of words at once:
    ```python
    word_list = ["pineapple", "butterfly", "adventure", "rainbow", "whisper",
        "enchantment", "tranquility", "galaxy", "serendipity", "blossom",
        "chocolate", "meadow", "firefly", "symphony", "serenade",
        "moonlight", "horizon", "oasis", "velvet", "reflection",
        "sunrise", "wonder", "starlight", "cascade", "mystic",
        "melody", "twilight", "radiant", "journey", "destiny",
        "harmony", "peaceful", "embrace", "shimmer", "gentle",
        "serene", "dreamer", "captivate", "inspire", "tranquility",
        "cherish", "ethereal", "wanderlust", "cherished", "radiant",
        "adventure", "captivate", "radiant", "enjoy", "serenity","Python","Hello","World"]
        
    trie.add_many(word_list)
    ```

#### Removing Words

To remove words from the trie, you can use these methods:

- To remove a single word:
    ```python
    trie.remove("Python")
    ```

- To remove a list of words:
    ```python
    trie.remove_many(["Hello", "World"])
    ```

- To empty the trie:
    ```python
    trie.clear()
    ```

#### Checking and Counting

You can perform various checks and obtain counts using these methods:

- To check if a word exists in the trie:
    ```python
    exists = trie.has("horizon")
    print(exists)
    
    >>> True
    ```

- To check if there are words that start with a given prefix:
    ```python
    starts_with = trie.starts_with("ad")
    print(starts_with)
    
    >>> True
    ```

- To get the count of words that start with a prefix:
    ```python
    starts_with_count = trie.starts_with_count("ad")
    print(starts_with_count)
    
    >>> 2
    ```

- To get the count of words equal to a given word:
    ```python
    count_equals = trie.count_equals("adventure")
    print(count_equals)
    
    >>> 2
    ```

- To get the count of unique words in the trie:
    ```python
    unique_count = trie.unique_count()
    print(unique_count)
    
    >>> 48
    ```

#### Retrieving Words

You can retrieve words using these methods:

- To get a generator object for all words in the trie:
    ```python
    all_words_generator = trie.all_words()
    for word in all_words_generator:
        print(word)
    
    >>> 
    pineapple
    butterfly
    adventure
    ...
    World
    ```

- To get a generator object for words that start with a prefix:
    ```python
    starts_with_generator = trie.words_starts_with("m")
    for word in starts_with_generator :
        print(word)
    >>>
    meadow
    melody
    moonlight
    mystic
    ```

Remember that for generator objects, you need to iterate over them to access the actual words they yield.
###### Note: This trie only works on alphabetical characters. If you want to use intergers typecast them into string before adding them to the trie.