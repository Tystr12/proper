class Person:
    """
    Person dataclass to use to store information in a datatype.

    """
    def __init__(self, name:str, age:int, job:str, hobby:str):
        """
        Constructor for person datatype.

        :param name: name of the person a string
        :param age: age of the person an int
        :param job: the person's job a string
        :param hobby: the person's hobby a string
        """
        self.name = name
        self.age = age
        self.job = job
        self.hobby = hobby

    def print_info(self) -> None:
        """
        Prints the info of a person to the console.
        :return: None, calls print function
        """
        print(f'{self.name} {self.age} {self.job} {self.hobby}')



def main()-> None:
    x = Person("Ty", 18, "Programmer", "Soccer")
    x.print_info()
    x.__setattr__("language", "python")
    x.print_info()
    print(x.__getattribute__("language"))

if __name__ == "__main__":
    main()