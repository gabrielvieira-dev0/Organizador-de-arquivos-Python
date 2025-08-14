# Nenhuma instalação extra é necessária.

import os
import shutil

def organizar_arquivos_por_extensao(caminho_da_pasta):
    """
    Organiza os arquivos em uma pasta de origem, movendo-os para
    subpastas baseadas em suas extensões.
    """
    print(f"Analisando a pasta: {caminho_da_pasta}")

    # Verifica se o caminho fornecido é um diretório válido
    if not os.path.isdir(caminho_da_pasta):
        print(f"Erro: O caminho '{caminho_da_pasta}' não é uma pasta válida.")
        return

    # Lista todos os arquivos na pasta de origem
    arquivos = os.listdir(caminho_da_pasta)

    for arquivo in arquivos:
        # Monta o caminho completo do arquivo
        caminho_completo_arquivo = os.path.join(caminho_da_pasta, arquivo)

        # Ignora se for uma pasta
        if os.path.isdir(caminho_completo_arquivo):
            continue

        # Obtém a extensão do arquivo (ex: '.txt', '.jpg')
        _, extensao = os.path.splitext(arquivo)
        extensao = extensao[1:].lower() # Remove o ponto e converte para minúsculas

        # Se não tiver extensão, podemos colocar em uma pasta "outros"
        if not extensao:
            extensao = 'outros'
        
        # Define o caminho da pasta de destino
        pasta_destino = os.path.join(caminho_da_pasta, extensao)

        # Cria a pasta de destino se ela não existir
        if not os.path.exists(pasta_destino):
            print(f"Criando pasta: {pasta_destino}")
            os.makedirs(pasta_destino)

        # Move o arquivo para a pasta de destino
        try:
            print(f"Movendo '{arquivo}' para a pasta '{extensao}'...")
            shutil.move(caminho_completo_arquivo, pasta_destino)
        except Exception as e:
            print(f"Erro ao mover o arquivo {arquivo}: {e}")

    print("\nOrganização concluída!")

# Executa a função principal
if __name__ == "__main__":
    # Obs: Altere este caminho para a pasta que você deseja organizar.
    # Por exemplo: "C:\Users\SeuUsuario\Downloads"
    pasta_para_organizar = input("Digite o caminho completo da pasta que deseja organizar: ")
    organizar_arquivos_por_extensao(pasta_para_organizar)