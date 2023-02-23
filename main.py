import itertools

filee = 'data.txt'

def readData(file_name):
    # Abrir el archivo y leer las líneas
    with open(file_name, 'r') as archivo:
        for line in archivo:
            line = line.strip()
    # Devolver la lista de líneas 
    return line

R = 1
L = -1

initial = {
    "0": {"1": ("1","X",R), "X": ("18", "0", R)},
    "1": {"1": ("2","X",R), "X": ("18", "1", R)},
    "2": {"1": ("2","1",R), "X": ("3", "0", R)},
    "3": {"X": ("4", "A", R)},
    "4": {"X": ("5", "0", R)},
    "5": {"X": ("12", "A", L)},  
}

pos = {
    "7": {"1": ("7", "A", R), "0": ("7", "0", R), "A": ("7", "A", R), "X": ("8", "0", L)},
    "11": {"1": ("11", "1", L), "0": ("8", "0", L)}
}

num = {
    "8": {"1": ("8", "1", L), "0": ("9", "0", L), "A": ("10", "1", R)},
    "9": {"1": ("9", "1", L), "0": ("12", "0", L), "A": ("10", "1", R)},
    "10": {"1": ("10", "1", R), "0": ("10", "0", R), "X": ("11", "1", L)}
}

next = {
    "12": {"1": ("12", "1", L), "0": ("12", "0", L), "A": ("12", "A", L), "X": ("13", "X", R)},
    "13": {"1": ("14", "X", R), "0": ("15", "1", R)},
    "14": {"1": ("14", "1", R), "0": ("7", "0", R)},
}

end = {
    "15": {"1": ("15", "A", R), "0": ("15", "0", R), "A": ("15", "A", R), "X": ("16", "X", L)},
    "16": {"0": ("17", "X", L), "A": ("16", "1", L)},
    "17": {"1": ("18", "X", R), "0": ("17", "X", L), "A": ("17", "X", L)}
}

turing_table = {**initial, **pos, **num, **next, **end}
# print(turing_table)

listData = readData(filee)
# print(listData)

# Esto de aqui es el string inicial VVV
# .chain concateno elementos de lista de listas en una plana
tape = ["X"] + list(itertools.chain(*listData)) + ["X"] * 165

initial_pos = 1

class Turing:
    def __init__(self, tape, turing_table, initial_pos = 1) -> None:
        self.tape = tape
        self.pos = initial_pos
        self.turing_table = turing_table
        self.value = self.tape[self.pos]
        self.state = "0"
    
    def move(self) -> None:
                 
        self.value = self.tape[self.pos]
                       
        new = self.turing_table[self.state][self.value]
        
        self.state = new[0]
        self.tape[self.pos] = new[1]
        self.pos += new[2]        

        # Se imprime el movimiento de la máquina
        # Dependiendo el número de espacios en la máquina se cambian por _
        tape_str = ''.join(self.tape).replace("X", "_")
        # Muestra en dónde se encuentra la cabeza
        head_str = ''.join([' ']*(self.pos - 1)) + '^'
        print(tape_str)
        print(head_str)
        print(f"State: {self.state}")
        print()
        
    def run(self) -> str:
        while self.state != "18":
            self.move()
        return "".join(self.tape).replace("X", "") + " = " + str(self.tape.count("1"))
    
    
output = Turing(tape, turing_table).run()
print(output)