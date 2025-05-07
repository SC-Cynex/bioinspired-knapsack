import random
from src.genetic_algorithm import genetic_algorithm

def parse_list_input(text):
    try:
        values = list(map(int, text.strip().split()))
        if not values or any(v < 0 for v in values):
            raise ValueError
        return values
    except:
        print("❌ Entrada inválida. Digite números inteiros positivos separados por espaço.")
        return None

def generate_items(n, value_range=(1, 100), weight_range=(1, 50)):
    values = [random.randint(*value_range) for _ in range(n)]
    weights = [random.randint(*weight_range) for _ in range(n)]
    capacity = int(sum(weights) * 0.6)
    return values, weights, capacity

def get_manual_input():
    while True:
        v_input = input("Digite os VALORES dos itens (separados por espaço): ")
        values = parse_list_input(v_input)
        if values: break

    while True:
        w_input = input("Digite os PESOS dos itens (separados por espaço): ")
        weights = parse_list_input(w_input)
        if weights and len(weights) == len(values): break
        print("❌ A quantidade de pesos deve ser igual à de valores.")

    while True:
        try:
            capacity = int(input("Digite a capacidade da mochila: "))
            if capacity <= 0:
                raise ValueError
            break
        except:
            print("❌ Digite um número inteiro positivo para a capacidade.")

    return values, weights, capacity

print("📦 Problema da Mochila 0/1 com Algoritmo Genético")
print("1 - Inserir dados manualmente")
print("2 - Gerar dados automaticamente")

while True:
    choice = input("Escolha uma opção (1 ou 2): ")
    if choice in {'1', '2'}:
        break
    print("❌ Opção inválida. Escolha 1 ou 2.")

if choice == '1':
    values, weights, capacity = get_manual_input()
else:
    while True:
        try:
            n_items = int(input("Quantos itens deseja gerar? (ex: 10, 100, 2500): "))
            if n_items <= 0:
                raise ValueError
            break
        except:
            print("❌ Digite um número inteiro positivo.")

    values, weights, capacity = generate_items(n_items)
    print(f"\n🔧 {n_items} itens gerados automaticamente.")
    print(f"Capacidade da mochila: {capacity}")

solution, total_value = genetic_algorithm(values, weights, capacity)

if solution is None:
    print("❌ Nenhuma solução válida foi encontrada.")
    exit()

selected_items = [i for i, bit in enumerate(solution) if bit == 1]
total_weight = sum(weights[i] for i in selected_items)
capacity_used_pct = (total_weight / capacity) * 100 if capacity > 0 else 0

print("\n🎯 Melhor solução encontrada:")
print(f"👉 Itens selecionados (índices): {selected_items}")
print(f"🧠 Representação binária da solução: {solution.tolist()}")
print(f"📦 Peso total da mochila: {total_weight} / {capacity} ({capacity_used_pct:.2f}%)")
print(f"💰 Valor total obtido: {total_value}")
print(f"📊 Quantidade de itens escolhidos: {len(selected_items)}")

print("\n📋 Detalhes dos itens selecionados:")
print(f"{'Índice':<6} {'Valor':<6} {'Peso':<6}")
print("-" * 22)
BLOCK_SIZE = 20
total = len(selected_items)

for start in range(0, total, BLOCK_SIZE):
    end = min(start + BLOCK_SIZE, total)
    for i in selected_items[start:end]:
        print(f"{i:<6} {values[i]:<6} {weights[i]:<6}")
    if end < total:
        response = input(f"... Mostrando itens {start + 1}-{end} de {total}. Ver mais? (s/n): ").lower()
        if response != 's':
            break

