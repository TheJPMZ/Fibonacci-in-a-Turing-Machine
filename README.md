# Fibonacci in a Turing Machine
This is a project that consists of simulating a Turing Machine that calculates the Fibonacci sequence. This project was made for the Algorithms and Complexity class at "University of the Valley" in Guatemala.

## Conventions
* Fibonacci sequence starts at 0.
* Unary representation of numbers. (0 = 0, 1 = 1, 11 = 2, 111 = 3, 1111 = 4, etc.)
* When simulating the Turing Machine, the blank symbol is represented by the character "□".
* Machine's pointer is represented by the character surrounded by brackets "[ ]".

## Turing Machine
To simulate the Turing Machine, the file "main.py" must be executed with python 3.6 or higher.
A json file is required for the Turing Machine configuration, which must have the following structure:
```json
{
    "transitions":{
        "State": {"Symbol": ["Next state", "Symbol to write", "Direction"]},
    }
}
```

To execute the program, the following command must be executed:
```bash
python main.py
```

With the given input, the program will simulate the Turing Machine.

## Graph representation of the Turing Machine
![imagen](https://user-images.githubusercontent.com/64183934/222681481-9f0250d6-cfd9-449b-99fd-007849d6c9ae.png)

- Blue nodes are initial checks and preparation for the Turing Machine.
- Purple nodes are counting nodes.
- Red nodes are transition nodes.
- Orange nodes calculate the Fibonacci sequence.
- Magenta nodes remove everything but the result.