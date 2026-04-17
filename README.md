# ETL CSV Import

Este repositório contém um projeto simples de ETL para manipulação de bases CSV usando Python e pandas.

## Estrutura do repositório

- `base1.csv` - primeiro arquivo de dados de exemplo
- `base2.csv` - segundo arquivo de dados de exemplo
- `Import pandas.py` - script Python para importar e processar os dados
- `requirements.txt` - dependências do projeto

## Requisitos

- Python 3.12+ recomendado
- Um ambiente virtual Python (`venv` ou similar)

## Instalação

1. Crie e ative um ambiente virtual:

   ```powershell
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1
   ```

2. Instale as dependências:

   ```powershell
   python -m pip install -r requirements.txt
   ```

## Uso

Execute o script principal com Python:

```powershell
python "Import pandas.py"
```

Ajuste o script conforme necessário para os seus dados de entrada e pipeline ETL.

## Observações

- Caso prefira usar o terminal bash ou outro shell, adapte os comandos de ativação do ambiente virtual.
- Se necessário, renomeie o arquivo `Import pandas.py` para um nome sem espaços para facilitar a execução em alguns ambientes.
