
class Processor:
    def process(self):
        print("Processor is working")


class Computer:
    def __init__(self):
        # Computer ke andar Processor ka object
        self.processor = Processor()

    def start_computer(self):
        # Processor ka method call hoga
        self.processor.process()

        # Computer start hone ka message
        print("Computer is starting")


computer1 = Computer()
computer1.start_computer()
