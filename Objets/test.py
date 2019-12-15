instructions = ["Hello"]

commande = instructions[0]
for i in range(1, len(instructions)):
    commande = commande + " " + instructions[i]
print(commande)

