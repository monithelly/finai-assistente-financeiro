def investimento(mensal, taxa, meses):
    total = 0
    for i in range(meses):
        total = (total + mensal) * (1 + taxa)
    return round(total, 2)


def emprestimo(valor, taxa, meses):
    parcela = (valor * taxa) / (1 - (1 + taxa) ** -meses)
    return round(parcela, 2)