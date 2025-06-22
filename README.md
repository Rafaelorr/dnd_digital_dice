# Python Dice Roller
## Features

* Roll any number of dice of any size.
* Add a modifier to the total roll.
* Roll with:

  * **Normal mode** (standard rolls)
  * **Advantage** (roll two dice and take the higher)
  * **Disadvantage** (roll two dice and take the lower)

---

## Usage

```bash
python ndn.py <amount> <size> <modifier> <advantage>
```

### Parameters

| Argument    | Type  | Description                                                                      |
| ----------- | ----- | -------------------------------------------------------------------------------- |
| `amount`    | `int` | Number of dice to roll                                                           |
| `size`      | `int` | Number of sides on each die (e.g., 6 for a d6, 20 for a d20)                     |
| `modifier`  | `int` | A value added to the final total of the dice roll                                |
| `advantage` | `str` | `"a"` for advantage, `"d"` for disadvantage, or any other string for normal roll |

---

## How It Works

* In **normal** rolls, each die generates a random number between 1 and the number of sides.
* In **advantage/disadvantage** rolls, each die roll is replaced with the higher/lower of two attempts.
