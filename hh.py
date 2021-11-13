import networkx as nx 
import matplotlib.pyplot as plt

seq1 = [5, 4, 4, 4, 4, 4, 3, 3, 3, 3, 3]
seq2 = [6, 3, 3, 3, 3, 2, 2, 2, 2, 2, 1, 1]

def Graph_Check(Seq):
    print("Checking if ", Seq, "is graphical:")
    while True:
        newSeq = []
        first = Seq[0] #Every time I start from the first element of the sequence
        if first == 0:
            return True
        for i in range(len(Seq)-1):
            if i < first: #Decrease by one (the number of elements that the first one says) 
                newSeq.append(Seq[i+1]-1)
            else:
                newSeq.append(Seq[i+1]) #leave the others as they were
            if newSeq[i] < 0: #
                return False
        Seq = sorted(newSeq)
        Seq = Seq[::-1] #descending order
        print(Seq)
        print("")

Graph1 = Graph_Check(seq1)
print(seq1)
if Graph1 == True:
    print("The sequence",seq1,"is graphical.")
    G = nx.random_degree_sequence_graph(seq1)
    pos = nx.circular_layout(G)
    nx.draw_networkx(G,pos)
    plt.show()
else:
    print("The sequence",seq1,"is not graphical.")
Graph2 = Graph_Check(seq2)
print(seq2)
if Graph2 == True:
    print("The sequence",seq2,"is graphical.")
    G = nx.random_degree_sequence_graph(seq2)
    pos = nx.circular_layout(G)
    nx.draw_networkx(G,pos)
    plt.show()
else:
    print("The sequence",seq2,"is not graphical.")
