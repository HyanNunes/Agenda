import json
from datetime import datetime
from pathlib import Path


ARQUIVO_DADOS = Path(__file__).with_name("compromissos.json")


def carregar_compromissos():
    if not ARQUIVO_DADOS.exists():
        return []

    with ARQUIVO_DADOS.open("r", encoding="utf-8") as arquivo:
        return json.load(arquivo)


def salvar_compromissos(compromissos):
    with ARQUIVO_DADOS.open("w", encoding="utf-8") as arquivo:
        json.dump(compromissos, arquivo, ensure_ascii=False, indent=2)


def listar(compromissos):
    if not compromissos:
        print("A agenda está vazia.")
        return

    print("\nCompromissos:")
    for indice, compromisso in enumerate(compromissos, start=1):
        print(
            f"{indice}. {compromisso['data']} às {compromisso['horario']} "
            f"- {compromisso['descricao']}"
        )


def adicionar(compromissos):
    descricao = input("Descrição do compromisso: ").strip()
    if not descricao:
        print("A descrição não pode ficar vazia.")
        return

    try:
        entrada_data = input("Data (DD/MM/AAAA ou DDMMAAAA): ").strip()
        if entrada_data.isdigit() and len(entrada_data) == 8:
            entrada_data = (
                f"{entrada_data[:2]}/{entrada_data[2:4]}/{entrada_data[4:]}"
            )

        entrada_horario = input("Horário (HH:MM ou HHMM): ").strip()
        if entrada_horario.isdigit() and len(entrada_horario) == 4:
            entrada_horario = f"{entrada_horario[:2]}:{entrada_horario[2:]}"

        data = datetime.strptime(entrada_data, "%d/%m/%Y")
        horario = datetime.strptime(entrada_horario, "%H:%M")
    except ValueError:
        print("Data ou horário inválido. Use DD/MM/AAAA e HH:MM.")
        return

    compromissos.append(
        {
            "descricao": descricao,
            "data": data.strftime("%d/%m/%Y"),
            "horario": horario.strftime("%H:%M"),
        }
    )
    salvar_compromissos(compromissos)
    print("Compromisso adicionado.")


def excluir(compromissos):
    if not compromissos:
        print("Não há compromissos para excluir.")
        return

    listar(compromissos)
    try:
        indice = int(input("Número do compromisso a excluir: "))
    except ValueError:
        print("Digite um número válido.")
        return

    if indice < 1 or indice > len(compromissos):
        print("Número fora da lista.")
        return

    removido = compromissos.pop(indice - 1)
    salvar_compromissos(compromissos)
    print(f"Compromisso '{removido['descricao']}' excluído.")


def sair():
    print("Agenda encerrada.")
