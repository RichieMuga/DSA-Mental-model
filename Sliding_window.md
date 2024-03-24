# Sliding window

## what is it?

This is a technique used when one visualizes a window in maybe an array or a linked list and travels with it like a cartepillar or as a fixed size

### types of sliding windows

#### Fixed sliding window

Moves in a fixed length along the data structure used in a fixed number of elements one can use.

#### Dynamic sliding window

Moves like a cartepillar, until some certain condition is met, it can stay without moving

### Recognizing these types of problems

1. Things that Iterate over each other.
    - In that: contigious squence elements
    - which are: strings, arrays or even linked lists
    - Calculate, either the min, max, shortest, longest or even contained

### Question Variants

#### Fixed length

- Maximum subarray of size k

#### Dynamic variant

- Smallest sum greater than or equal to some value k

#### Dynamic with an auxiliary datastructure

- This uses a dynamic datastructure like a hashmap

- Longest substting w/ no more than k distinct characters

- Permutations( Different arrangement of a string )

#### What is the commonality

1. Everything is grouped sequentially
    - Keywords like subarray or substrings are dead giveaways

2. Longest, smallest or Contained
    - Max or min
