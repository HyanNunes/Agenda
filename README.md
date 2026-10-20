# Agenda

Programa de linha de comando para organizar compromissos. Os dados ficam salvos
em `compromissos.json`, no mesmo diretório dos arquivos Python.

## Arquivos e funções

- `main.py`: exibe o menu e encaminha a opção escolhida.
- `funcoes.py`: contém as ações do menu:
  - `listar`: mostra os compromissos cadastrados.
  - `adicionar`: cadastra um compromisso com descrição, data e horário. A data
    pode ser informada como `DD/MM/AAAA` ou apenas números (`DDMMAAAA`), e o
    horário como `HH:MM` ou apenas números (`HHMM`); os separadores são
    inseridos automaticamente.
  - `excluir`: remove um compromisso pelo número exibido na lista.
  - `sair`: informa o encerramento do programa.

## Como executar

Com Python 3 instalado, execute `python main.py` no diretório do programa.
