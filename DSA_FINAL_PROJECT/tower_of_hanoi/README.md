# Tower of Hanoi Implementation

This project implements the classic Tower of Hanoi puzzle using Python, featuring a recursive solution and a custom stack data structure. The implementation includes a visual representation of the puzzle's state after each move.

## Problem Description

The Tower of Hanoi is a classic puzzle where the objective is to move a stack of disks from one rod to another, following these rules:

1. Only one disk can be moved at a time
2. Each move consists of taking the upper disk from one of the stacks and placing it on top of another stack or on an empty rod
3. No larger disk may be placed on top of a smaller disk

## Project Structure

The project consists of two main Python files:

1. `stack.py`: Contains the implementation of the Stack data structure
2. `tower_of_hanoi.py`: Contains the recursive solution to the Tower of Hanoi puzzle

### Stack Implementation (`stack.py`)

The Stack class is a custom implementation designed specifically for the Tower of Hanoi puzzle. It includes:

```python
class Stack:
    def __init__(self, size, name):
        # Initialize stack with fixed size and name
        self.size = size
        self.stack = [None] * size
        self.top = -1
        self.name = name
```

Key methods:

- `push(item)`: Add a disk to the top of the stack
- `pop()`: Remove and return the top disk
- `peek()`: View the top disk without removing it
- `is_empty()`: Check if the stack is empty
- `is_full()`: Check if the stack is full
- `get_items()`: Return list of items currently in the stack

### Tower of Hanoi Implementation (`tower_of_hanoi.py`)

The TowerOfHanoi class implements the complete solution with these features:

```python
class TowerOfHanoi:
    def __init__(self, num_disks):
        self.num_disks = num_disks
        self.moves = 0
        # Initialize three stacks for the towers
        self.source = Stack(num_disks, "A")
        self.spare = Stack(num_disks, "B")
        self.target = Stack(num_disks, "C")
```

Key components:

- Recursive solution algorithm
- Visual representation of towers
- Move counting and tracking
- Input validation
- Error handling

## Installation

1. Clone the repository:

```bash
git clone https://github.com/yourusername/tower_of_hanoi.git
cd tower_of_hanoi
```

2. Ensure you have Python 3.x installed:

```bash
python --version
```

No additional dependencies are required as the implementation uses only Python standard library.

## Usage

1. Run the program:

```bash
python tower_of_hanoi_new.py
```

2. When prompted, enter the number of disks you want to solve the puzzle with:

```
Enter the number of disks: 3
```

3. The program will:
   - Display the initial state of the towers
   - Show each move with updated tower states
   - Print the total number of moves made
   - Show the minimum possible moves for that number of disks

## Visual Output Example

The program provides a visual representation of the towers:

```
Current State:
 =================================
    |          |         ===  
    |          |        ===== 
    |          |       =======
 =======    =======    =======
    A          B          C   
 =================================
```

Where:

- `===` represents a disk (more = symbols means larger disk)
- `|` represents an empty rod position
- `A`, `B`, `C` are the tower names

## Algorithm Details

The solution uses a recursive algorithm with these steps:

1. Base case: If only one disk, move it directly from source to target
2. Recursive case:
   - Move n-1 disks from source to spare (using target as temporary)
   - Move the largest disk from source to target
   - Move n-1 disks from spare to target (using source as temporary)

Time Complexity: O(2^n)

- Each disk doubles the number of moves needed
- Total moves required = 2^n - 1, where n is the number of disks

Space Complexity: O(n)

- Due to the recursive call stack depth

## Error Handling

The program includes robust error handling for:

- Invalid input types (non-integers)
- Negative numbers
- Zero disks
- Stack overflow/underflow conditions

## Contributing

Feel free to fork this repository and submit pull requests for any improvements. Some areas for potential enhancement:

- Adding an iterative solution
- Implementing an animation of the moves
- Adding a GUI interface
- Supporting multiple algorithms for comparison

## License

This project is open source and available under the MIT License.
