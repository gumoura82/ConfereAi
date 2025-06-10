
class Estoque:
    def __init__(self, dados):
        self.dados = dados

    def atualizar(self, unidade, item, quantidade):
        if quantidade <= 0:
            return "❌ Quantidade inválida."
        if unidade in self.dados and item in self.dados[unidade]:
            self.dados[unidade][item]["quantidade"] -= quantidade
            return f"{quantidade}x {item} retirados de {unidade}"
        return "Unidade ou item não encontrado."

    def verificar_alertas(self, unidade):
        alertas = []
        for item, dados in self.dados.get(unidade, {}).items():
            if dados["quantidade"] < dados["minimo"]:
                alertas.append(f"⚠️ Alerta: {item} em {unidade} abaixo do mínimo!")
        return alertas or [f"✅ Todos os itens em {unidade} estão acima do mínimo."]

    def redistribuir(self, origem, destino, item):
        try:
            item_origem = self.dados[origem][item]
            item_destino = self.dados[destino][item]

            excesso = item_origem["quantidade"] - item_origem["ideal"]
            if excesso > 0:
                necessidade = max(item_destino["ideal"] - item_destino["quantidade"], 0)
                transferir = min(excesso, necessidade)
                item_origem["quantidade"] -= transferir
                item_destino["quantidade"] += transferir
                return f"🔄 {transferir}x {item} movidos de {origem} para {destino}"
            return "ℹ️ Nenhum excesso para redistribuir."
        except KeyError:
            return "❌ Item não disponível em ambas as unidades."

    def itens_em_falta(self):
        faltando = []
        for unidade, itens in self.dados.items():
            for item, info in itens.items():
                if info["quantidade"] < info["minimo"]:
                    faltando.append((unidade, item))
        return faltando

    def buscar_item_global(self, nome_item):
        locais = []
        for unidade, itens in self.dados.items():
            if nome_item in itens:
                locais.append((unidade, itens[nome_item]["quantidade"]))
        return locais or "Item não encontrado."


# Exemplo de uso
if __name__ == "__main__":
    dados_estoque = {
        "Unidade_A": {
            "luvas": {"quantidade": 150, "minimo": 100, "ideal": 200},
            "seringas": {"quantidade": 70, "minimo": 80, "ideal": 150}
        },
        "Unidade_B": {
            "luvas": {"quantidade": 60, "minimo": 100, "ideal": 200},
            "algodão": {"quantidade": 300, "minimo": 200, "ideal": 400}
        }
    }

    estoque = Estoque(dados_estoque)

    print(estoque.atualizar("Unidade_A", "seringas", 20))
    for alerta in estoque.verificar_alertas("Unidade_A"):
        print(alerta)
    print(estoque.redistribuir("Unidade_A", "Unidade_B", "luvas"))
    print("Itens em falta:", estoque.itens_em_falta())
    print("Busca global por 'luvas':", estoque.buscar_item_global("luvas"))
