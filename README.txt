Organizador de Arquivos Automático em Python

📝 Descrição

Este é um script em Python desenvolvido para automatizar a organização de arquivos em um diretório específico. Ele analisa todos os arquivos de uma pasta (como a de "Downloads", por exemplo) e os move para subpastas nomeadas de acordo com suas extensões. O objetivo é transformar uma pasta desorganizada em um ambiente estruturado de forma rápida e eficiente.

✨ Funcionalidades

- Análise de Diretório: O script lê todos os itens de uma pasta de origem especificada pelo usuário.
- Criação de Subpastas: Cria automaticamente pastas com base nas extensões dos arquivos encontrados (ex: 'pdf', 'jpg', 'docx').
- Movimentação de Arquivos: Move cada arquivo para a subpasta correspondente à sua extensão.
- Tratamento de Exceções: Ignora subdiretórios já existentes na pasta de origem e lida com arquivos que não possuem extensão, movendo-os para uma pasta 'outros'.

⚙️ Como Funciona

O script utiliza as bibliotecas padrão do Python `os` e `shutil`. A lógica principal é a seguinte:
1.  Solicita ao usuário o caminho completo da pasta a ser organizada.
2.  Lista todos os itens no diretório.
3.  Para cada item, verifica se é um arquivo.
4.  Extrai a extensão do arquivo (ex: `.png` se torna `png`).
5.  Verifica se já existe uma subpasta com o nome da extensão. Se não, ela é criada.
6.  Move o arquivo da pasta de origem para a pasta de destino correta.

🚀 Como Usar

1.  Clone ou baixe este repositório:
    ```bash
    git clone https:https://github.com/gabrielvieira-dev0/Organizador-de-arquivos-Python.git
    ```
2.  Navegue até a pasta do projeto:
    ```bash
    cd nome-da-pasta-do-projeto
    ```
3.  Execute o script pelo terminal:
    ```bash
    python organizador.py
    ```
4.  Informe o caminho: Quando solicitado, cole o caminho completo da pasta que você deseja organizar e pressione Enter.

Atenção: Recomenda-se testar o script em uma pasta de exemplo antes de usá-lo em diretórios importantes.

🛠️ Tecnologias Utilizadas

- Python 3.12
- Bibliotecas Padrão:
  - `os`: Para interagir com o sistema operacional (listar diretórios, criar pastas).
  - `shutil`: Para realizar operações de alto nível com arquivos (mover arquivos).

🧠 O que aprendi com este projeto

Desenvolver este script foi uma ótima oportunidade para solidificar conceitos importantes:

- Manipulação de Arquivos e Diretórios: Aprofundei meus conhecimentos sobre como o Python pode interagir com o sistema de arquivos, usando funções como `os.listdir()`, `os.path.join()`, `os.path.splitext()`, `os.makedirs()` e `shutil.move()`.

- Lógica de Programação Estruturada: Pratiquei o uso de laços (`for`), condicionais (`if/else`) e tratamento de erros básicos para construir um fluxo de execução robusto e previsível.
- Importância das Bibliotecas Padrão: Percebi o quão poderosa é a biblioteca padrão do Python, capaz de resolver problemas reais e complexos sem a necessidade de instalar pacotes externos.
- Desenvolvimento Orientado a Problemas: Aprendi a identificar um problema do dia a dia e traduzi-lo em uma solução de software funcional, desde a concepção da ideia até a implementação do código.
