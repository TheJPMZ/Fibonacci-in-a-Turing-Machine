import itertools
import time
import json

filee = 'data.txt'
config_file = 'configuration.json'


# Esto de aqui es el string inicial VVV
# .chain concateno elementos de lista de listas en una plana

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
        tape_str = ''.join(self.tape).replace("X", "□")
        # Muestra en dónde se encuentra la cabeza
        head_str = ''.join([' ']*(self.pos)) + '^'
        print(tape_str)
        print(head_str)
        print(f"State: {self.state}")
        print()
        
    def run(self) -> str:
        # Takin execution time
        start_time = time.time()
        while self.state != "18":
            self.move()
        print("Tiempo: %s segundos" % (time.time() - start_time))
        return "".join(self.tape).replace("X", "") + " = " + str(self.tape.count("1"))
    
    


def multiple(file_name, config_file):
    f = open(config_file)
    data = json.load(f)
    turing_table = data["transitions"]
    line_list = []
    output_list = []
    with open(file_name, 'r') as archivo:
        for line in archivo:
            line_list.append(line.strip())
            
    for i in line_list:
        taper = ["X"] + list(itertools.chain(*i)) + ["X"] *50*((len(line_list))*2)
        output_list.append(Turing(taper, turing_table).run()+'\n')
        
    with open('output.txt', 'a') as file:
        file.truncate(0)
        file.writelines(output_list)
        file.close()
    # Devolver la lista de líneas 
    
multiple(filee, config_file)