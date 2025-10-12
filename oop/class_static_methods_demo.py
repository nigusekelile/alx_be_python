class Calculator:
    # Class attribute
    calculation_type = "Arithmetic Operations"
    
    @staticmethod
    def add(a, b):
        """
        Static method to add two numbers.
        
        Static methods don't have access to the class or instance.
        They behave like regular functions but belong to the class namespace.
        
        Args:
            a (int/float): First number
            b (int/float): Second number
            
        Returns:
            int/float: Sum of a and b
        """
        return a + b
    
    @classmethod
    def multiply(cls, a, b):
        """
        Class method to multiply two numbers.
        
        Class methods have access to the class via the 'cls' parameter.
        They can access and modify class attributes.
        
        Args:
            cls: The class (Calculator)
            a (int/float): First number
            b (int/float): Second number
            
        Returns:
            int/float: Product of a and b
        """
        print(f"Calculation type: {cls.calculation_type}")
        return a * b
    
    # Additional examples to further demonstrate the concepts
    @classmethod
    def set_calculation_type(cls, new_type):
        """
        Class method that modifies class attribute.
        
        This demonstrates how class methods can change class-level data.
        """
        cls.calculation_type = new_type
        return f"Calculation type updated to: {new_type}"
    
    @staticmethod
    def is_even(number):
        """
        Another static method example.
        
        This doesn't need access to class or instance data.
        """
        return number % 2 == 0
    
    @classmethod
    def get_class_info(cls):
        """
        Class method that returns information about the class.
        """
        return f"This is the {cls.__name__} class for {cls.calculation_type}"
