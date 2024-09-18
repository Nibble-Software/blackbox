# Blackbox

**Author: Marcelo de Jesús Núñez**

Developed for the **Nibble team**

## Overview
This library contains an automated black box 
code evaluation for c++ and python. 
Using the path of the source file, and array of inputs and 
outputs the system will evaluate the provided code and respond
according to the specified inputs and outputs

## Requirements
- g++ installed
- python3 installed
- in Linux systems probably you have to create an alias for python3 called python

## Execution

For execution, you have to call the `blackbox` method to start code evaluation

```python
from blackbox.blackbox import blackbox

def main() -> None:
    solution = blackbox('python','print("Hello World!!")',None,["Hello World!!"])
    print(solution)

if __name__ == '__main__':
    main()
```

### Parameters
- language: a string with the selected language (actually supports c++ and python)
- solution_filepath: the path of the source code
- inputs: a string array with all the inputs that the kernel has to add to the code evaluation
- outputs: an array with the expected outputs of the source code

### Response

The kernel will return a dictionary containing:
- status: the status of the evaluation (see above for more details)
- expected: the expected outputs given previously
- got: the real outputs thrown by the source code

## Possible Responses

### PASSED
This message indicates that the code passed the test

### FAILED
This message indicades that the code didn't respond the same as the 
specified outputs

### COMPILATION_ERROR
In this case, for compilated languages (e.g c++) it will
a message indicating that the source has a compilation error

### EXECUTION_ERROR
In case that the return code of the execution is not 0, the library
will return this message

### TIMEOUT_ERROR
The evaluation will wait only 10 seconds, after that it 
will raise a timeout error

# Contact
- E-mail: [mdjnunez9706@gmail.com](mailto:mdjnunez9706@gmail.com)
- Github: [chelo154](https://github.com/chelo154)
- Linkedin [Marcelo de Jesús Núñez](https://www.linkedin.com/in/marcelo-de-jesús-nuñez-490b05191/)