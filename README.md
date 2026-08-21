# EasyQueue

A Python implementation of a fixed-size queue data structure with bounded capacity management. This library provides a straightforward queue implementation demonstrating core object-oriented principles and queue mechanics.

## Overview

EasyQueue implements a classical queue (FIFO: First-In-First-Out) with a pre-allocated fixed size. The implementation uses pointer-based tracking to manage the front and rear of the queue, supporting standard queue operations: enqueue (insertion), dequeue (removal), and state queries.

The library is published on PyPI for easy installation and use.

## Features

- **Fixed-size queue implementation**: Pre-allocated capacity with bounds checking
- **Pointer-based management**: Tracks front and rear pointers for efficient operations
- **State tracking**: Explicit empty and full state flags
- **Error handling**: Reports when queue is full or empty
- **Stress-tested**: Validated with 500+ sequential operations

## Technical Implementation

### Queue Structure

The queue maintains:
- A fixed-size list initialized with empty placeholders
- A `front_pointer` indicating the position of the first element
- An `end_pointer` tracking the position of the last element
- State flags (`is_Empty`, `is_Full`) for O(1) state checking

### Core Operations

**Enqueue (`enQueue`)**: Inserts a value at the end of the queue. Before insertion, checks if the queue is empty (special case: initialises front pointer). For subsequent insertions, calculates the correct position using `front_pointer + current_length`. Raises an error if the queue is full.

**Dequeue (`deQueue`)**: Removes and returns the element at the front pointer. Increments the front pointer and resets state flags when the queue becomes empty.

**State Queries**: 
- `length()`: Iterates through the queue to count non-empty positions
- `isEmpty()`: Returns the empty state flag
- `isFull()`: Returns the full state flag

### Design Considerations

The implementation uses a **pre-allocated list** rather than dynamic resizing, which simplifies the logic but limits capacity to the initial size. This design choice emphasizes understanding of bounded structures and explicit state management—key concepts in systems programming and embedded systems.

## Installation

Install from PyPI:

```bash
pip install basicQueue
```

Or clone and use directly:

```bash
git clone https://github.com/muhammadali-250408/my-python-queue-library.git
cd my-python-queue-library
```

## Usage

### Basic Example

```python
from easyqueue import Queue

# Create a queue with maximum capacity of 5
q = Queue(5)

# Add elements
q.enQueue(10)
q.enQueue(20)
q.enQueue(30)

# Remove an element (FIFO)
first = q.deQueue()  # Returns 10
print(first)  # Output: 10

# Check queue state
print(q.isEmpty())  # Output: False
print(q.isFull())   # Output: False

# Get current queue length
print(q.length())  # Output: 2
```

### Full Example with State Checking

```python
from easyqueue import Queue

q = Queue(3)

# Enqueue elements
q.enQueue("A")
q.enQueue("B")
q.enQueue("C")

print(q.isFull())  # Output: True (queue now at capacity)
print(q.length())  # Output: 3

# Dequeue elements
print(q.deQueue())  # Output: A
print(q.deQueue())  # Output: B

print(q.isEmpty())  # Output: False
print(q.length())   # Output: 1

# Continue dequeuing
print(q.deQueue())  # Output: C
print(q.isEmpty())  # Output: True

# Attempting to dequeue from empty queue
q.deQueue()  # Output: ERROR 002: QUEUE IS EMPTY
```

### Error Handling

The queue reports errors when capacity or state constraints are violated:

```python
from easyqueue import Queue

q = Queue(2)
q.enQueue(1)
q.enQueue(2)
q.enQueue(3)  # Output: LIST IS FULL, then ERROR 001: QUEUE HAS REACHED MAX SIZE

q2 = Queue(1)
q2.deQueue()  # Output: ERROR 002: QUEUE IS EMPTY
```

## Testing

Basic testing has been performed with 500+ sequential enqueue and dequeue operations to validate correctness under stress conditions. The TEST.py file (referenced in the repository) contains example use cases demonstrating queue operations.

## Limitations

- **Fixed capacity**: Queue size is determined at initialization and cannot be resized
- **No dynamic growth**: Once full, no additional elements can be added
- **Pointer wrapping not implemented**: After dequeuing all elements, the front pointer resets to 0 but does not wrap around the array
- **Simple length calculation**: The `length()` method iterates through all positions, making it O(n) rather than O(1)
- **No thread safety**: Not designed for concurrent access

## Future Improvements

- Implement circular buffer mechanics for efficient pointer wrapping
- Add dynamic resizing capability
- Implement O(1) length tracking with a size counter
- Add thread-safe operations for concurrent environments
- Comprehensive unit test suite with automated testing
- Type hints for better IDE support and type checking
- Iterator support for queue traversal

## Tech Stack

**Language**: Python 3

**Package Manager**: PyPI (basicQueue)

## License

No license specified. See repository for details.

## Repository

[GitHub Repository](https://github.com/muhammadali-250408/my-python-queue-library)

[PyPI Package](https://pypi.org/project/basicQueue/)
