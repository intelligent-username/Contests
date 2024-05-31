class ClassA:
    def __init__(self, attribute1, attribute2):
        self.attribute1 = attribute1
        self.attribute2 = attribute2

    def sample_method(self):
        return f"Attribute1: {self.attribute1}, Attribute2: {self.attribute2}"

# Step 2: Create an Instance of the Specified Class
instance = ClassA("value1", 42)

# Step 3: Display the Namespace of the Instance
print(instance.__dict__)
