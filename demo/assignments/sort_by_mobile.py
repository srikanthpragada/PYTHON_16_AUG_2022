data = [('James', '8150696123'), ('Scott', '7305122225'),
        ('Larry', '8150796123'), ('Bill', '6305192225'), ('Steve', '9193600056'),
        ('Andy', '8106591234')]

for name, mobile in sorted(data, key=lambda t: t[1]):
    print(f"{name:20} - {mobile}")
