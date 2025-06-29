import prettytable

table = prettytable.PrettyTable()

table.add_column("Pokemenon", ["Pikachu", "Charmander", "Bulbasaur"])
table.add_column("Type", ["Electric", "Fire", "Grass"])
table.align = "c"

print(table)