from patterns.singleton import Singleton


class Logger(metaclass=Singleton):

    def __init__(self, name):
        self.name = []
        if name not in self.name:
            self.name.append(name)

    def log(self, level, text):
        file = open("logging_files/" + str(self.name), 'a')
        file.write(f"{level}: {self.name} | {text}\n")
        print(f"{level}: {self.name} | {text}")


if __name__ == "__main__":
    s1 = Logger("log1")
    s2 = Logger("log2")
    print(s1)
    print(s2)
    print(s1 == s2)

