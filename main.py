import time
import json

config_file = 'configuration.json'


class Turing:
    def __init__(self, tape, turing_table) -> None:
        self.state = "0"
        self.pos = 1

        self.tape = ["X"] + [x for x in tape] + ["X"]
        self.turing_table = turing_table
        self.value = self.tape[self.pos]

    def move(self) -> None:

        if self.pos == len(self.tape) - 1:
            self.tape.append("X")

        self.value = self.tape[self.pos]

        new = self.turing_table[self.state][self.value]

        self.state = new[0]
        self.tape[self.pos] = new[1]
        self.pos += new[2]

    def run(self):

        while self.state != "18":
            print(self, end="\r")
            time.sleep(0.0001)
            self.move()

        print(self)

    def __str__(self) -> str:

        tape_str = ''.join(self.tape).replace("X", "⬜")

        return f"State {self.state}: ".rjust(10, " ") + tape_str[:self.pos] + "[" + tape_str[self.pos] + "]" + tape_str[
                                                                                                               self.pos + 1:]


def main():
    config = json.load(open(config_file, 'r'))

    meme = Turing(input(">"), config['transitions'])
    meme.run()


if __name__ == "__main__":
    main()
