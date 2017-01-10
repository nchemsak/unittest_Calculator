class Calculator():
    """Performs the four basic mathematical operations

    Methods:
     add(number, number)
     subtract(number, number)
     multiply(number, number)
     divide(number,number)
    """

    def add(self, firstOperand, secondOperand):
        """Adds two numbers together

        Arguments:
          firstOperand - Any number
          secondOperand - An number
        """

        return firstOperand + secondOperand


    def subtract(self, firstOperand, secondOperand):
        """Subtract secondOperand from firstOperand

        Arguments:
          firstOperand - Any number
          secondOperand - Any number
        """

        return firstOperand - secondOperand

    def multiply(self, firstOperand, secondOperand):
        """Multiply two numbers

        Arguments:
          firstOperand - Any number
          secondOperand - Any number
        """

        return firstOperand * secondOperand

    def divide(self, firstOperand, secondOperand):
        """Divide firstOperand by secondOperand

        Arguments:
          firstOperand - Any number
          secondOperand - Any number
        """

        return firstOperand / secondOperand
