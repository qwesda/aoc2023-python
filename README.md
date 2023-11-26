#  AOC 2023 スたんくん + クウェスダさま [python edition]

This is the repository for the Advent of Code 2023 (https://adventofcode.com/2023).

### Basic rules

- try to solve it by yourself first
- this is not about speed, it is good to let the problem stew for a few hour (or days), while the brain is working on it in the background
- ask for hints if you get stuck
- don't use any non-standard library packages (e.g. `numpy`, `pandas`, `scipy`, `sympy`, ...)
- don't use code assistants like github copilot, tabnine, ...

頑張ってね！

### Notes on code style

Consistency is very important to quickly read/parse code, follow the same style you choose everywhere!

Stuff that work very well for me:

#### Use descriptive variable/function names

This is often ignored in university settings, where the exact opposite is taught. 
Variables are names `x`, `y`, `a`, `b` and it is left to the reader (often a future version of oneself) to figure out what the fuck they mean.
There are a few exceptions to this, like `f` for an opened file or `x`, `y` in list comprehension ...

Sometimes thinking of a fitting name is already half of the solution! As the saying goes:

> There are only two hard problems in computer science:
> 0) Cache invalidation
> 1) Naming things
> 2) Off-by-one errors

#### Don't write stupid comments

Again 大学先生 will disagree, but do not put obvious stuff in comments. 
Comments are for non-obvious stuff that can't be easily from the code itself. 
If the function is well named it should be obvious what is supposed to happen.

#### Code should be layed like text

Think of it like sentences, paragraphs and chapters. Use whitespace (newlines) to separate them.
