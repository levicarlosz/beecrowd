itens = [
    {"codigo": 1, "especificacao": "Cachorro Quente", "preco": 4.00},
    {"codigo": 2, "especificacao": "X-Salada", "preco": 4.50},
    {"codigo": 3, "especificacao": "X-Bacon", "preco": 5.00},
    {"codigo": 4, "especificacao": "Torrada simples", "preco": 2.00},
    {"codigo": 5, "especificacao": "Refrigerante", "preco": 1.50}
]

item, quantidade = map(int, input().split())

total = quantidade * itens[item-1]["preco"]

print(f"Total: R$ {total:.2f}")