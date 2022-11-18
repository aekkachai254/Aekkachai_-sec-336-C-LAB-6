class graph:
    def __init__(self):
        self.x = [[" "," "],[" "," "]]

    def create_edge(self, edge):
        if self.x[0][1] == " " and self.x[1][0] == " ":
            self.x[0][1] = edge
            self.x[1][0] = edge
            self.x[1][1] = "0"
        else:
            self.x.append(["0"] * (len(self.x) + 1))
            for i in range(len(self.x)):
                if i == 0:
                    self.x[i].append(edge)
                elif i == len(self.x) - 1:
                    self.x[i][0] = edge
                else:
                    self.x[i].append("0")

    def connect(self, edge1, edge2):
        if edge1 == edge2:
            print('its the same edge.')
            return

        for i in range(len(self.x)):
            if self.x[0][i] is edge1 :
                for j in range(len(self.x)):
                    if self.x[j][0] is edge2:
                        if self.x[i][j] == "0" and self.x[j][i] == "0":
                            self.x[i][j] = "1"
                            self.x[j][i] = "1"
                        else:
                            print('its already existed.')

    def disconnect(self, edge1, edge2):
        if edge1 == edge2:
            print('its the same edge.')
            return

        for i in range(len(self.x)):
            if self.x[0][i] is edge1 :
                for j in range(len(self.x)):
                    if self.x[j][0] is edge2:
                        if self.x[i][j] == "1" and self.x[j][i] == "1":
                            self.x[i][j] = "0"
                            self.x[j][i] = "0"
                        else:
                            print('its doesnt existed.')

    def print_(self):
        for i in self.x:
            print(i)

def main():
    TableA = graph()
    # exercise 1
    # TableA.create_edge("A")
    # TableA.create_edge("B")
    # TableA.create_edge("C")
    # TableA.create_edge("D")
    # TableA.connect("A", "B")
    # TableA.connect("A", "C")
    # TableA.connect("C", "D")
    # TableA.connect("B", "C")
    # TableA.print_()

    # exercise 2
    # TableA.create_edge("A")
    # TableA.create_edge("B")
    # TableA.create_edge("C")
    # TableA.create_edge("D")
    # TableA.create_edge("E")
    # TableA.create_edge("F")
    # TableA.connect("A", "B")
    # TableA.connect("A", "C")
    # TableA.connect("C", "D")
    # TableA.connect("A", "F")
    # TableA.connect("F", "E")
    # TableA.connect("D", "E")
    # exercise 3
    TableA.create_edge("A")
    TableA.create_edge("B")
    TableA.create_edge("C")
    TableA.create_edge("D")
    TableA.create_edge("E")
    TableA.create_edge("F")
    TableA.connect("A", "B")
    TableA.connect("A", "C")
    TableA.connect("C", "D")
    TableA.connect("C", "F")
    TableA.connect("E", "F")
    TableA.print_()
    print()
    TableA.disconnect("C", "F")
    TableA.disconnect("A", "B")
    TableA.disconnect("C", "D")
    TableA.print_()
    print()
    TableA.connect("A", "E")
    TableA.connect("B", "C")
    TableA.connect("D", "F")

if __name__ == "__main__":
    main()