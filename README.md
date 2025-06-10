
# 📦 ConfereAí - Sistema de Gestão de Estoque com NFC

O **ConfereAí** é um sistema de gestão de estoque hospitalar, inspirado na tecnologia da Amazon, que utiliza **NFCs** para agilizar a atualização de insumos entre almoxarifado e unidades clínicas. Foi projetado para minimizar atrasos, evitar falhas no reabastecimento e facilitar a redistribuição inteligente de materiais entre setores.

## 👨‍⚕️ Cenário de Uso

Imagine um hospital onde o consultório solicita materiais ao almoxarifado. O responsável escaneia os produtos via NFC com um celular e, automaticamente, o estoque é atualizado. Isso reduz falhas humanas e acelera processos críticos.

---

## 🧠 Funcionalidades

- Atualização de estoque com validação de entrada
- Alerta automático de insumos abaixo do mínimo
- Redistribuição entre setores baseada em excesso e necessidade
- Busca global de itens e quantidades por unidade
- Relatório de insumos em falta

---

## 💡 Tecnologias e Técnicas Utilizadas

- Python 3
- Estrutura de dados: dicionários e listas aninhadas
- POO (Programação Orientada a Objetos)
- Análise de algoritmos com notação Big-O
- Pensado para futura integração com leitura NFC

---

## 🧪 Exemplo de Execução

```python
estoque = Estoque(dados_estoque)
print(estoque.atualizar("Unidade_A", "seringas", 20))
print(estoque.verificar_alertas("Unidade_A"))
print(estoque.redistribuir("Unidade_A", "Unidade_B", "luvas"))
print(estoque.itens_em_falta())
```

---

## 👥 Equipe

- Juan Francisco Alves Muradas — RM: 555541
- Gustavo Oliveira de Moura — RM: 555827
- Lynn Bueno Rosa — RM: 551102
- Leonardo Pasquini Baldaia — RM: 557416