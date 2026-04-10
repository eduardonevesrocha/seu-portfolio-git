def pedir_nota(label):
    while True:
        try:
            nota = float(input(f"  {label}: "))
            if 0 <= nota <= 10:
                return nota
            print("  Nota deve ser entre 0 e 10.")
        except ValueError:
            print("  Digite um numero valido.")

def calcular_media(notas, pesos):
    return sum(n * p for n, p in zip(notas, pesos)) / sum(pesos)

def main():
    print("=" * 40)
    print("  Calculadora de Medias - CIn UFPE")
    print("  por Eduardo Neves")
    print("=" * 40)
    print()

    disciplina = input("  Nome da disciplina: ").strip() or "Disciplina"
    print()

    p1 = pedir_nota("Nota P1")
    p2 = pedir_nota("Nota P2")
    p3 = pedir_nota("Nota P3")

    media = calcular_media([p1, p2, p3], [1, 1, 1])

    print()
    print(f"  Media de {disciplina}: {media:.2f}")

if __name__ == "__main__":
    main()
