#This program will automatically detect what screen resolution you are using.
from pynput.mouse import Button, Controller
mouse = Controller()
A = (0,999999)
B = (999999,0)
mouse.position = A
C = str(mouse.position)
mouse.position = B
D = str(mouse.position)
E=(C[4:-1])
F=int(E)
G=(D[:-4])
H=(G[1:])
I=int(H)
J=str(I+1)
K=str(F+1)
print("Screen Resolution is: "+J+"x"+K)
