# Swap

"Swap" is a common term used in programming and computer science, referring to the exchange or interchange of values between two variables. This operation involves switching the content of two variables, effectively swapping their values.

## Purpose of Swap

The swap operation is frequently used for reordering, sorting, and optimizing algorithms. It allows for the rearrangement of values without the need for additional temporary variables.

### Example Code in Python

```python
# Swapping values in Python
a = 5
b = 10

# Before swap
print("Before swap: a =", a, ", b =", b)

# Swapping values using a temporary variable
temp = a
a = b
b = temp

# After swap
print("After swap: a =", a, ", b =", b)
```

### Example Code in JavaScript (Array Elements)

```js
// Array declaration
let array = [10, 30, 40, 55]

// X is the starting point and Y is the ending point
let x = 0
let y = array.length - 1

// Temporary variable
let temp;


// Condition: as long as X is less than or equal to Y
while (x <= y) {
  temp = array[x]

  // Swapping values using a temporary variable
  array[x] = array[y]
  array[y] = temp

  // Increment and decremet
  x++;
  y--;
}

console.log('The swapped array', array)
```