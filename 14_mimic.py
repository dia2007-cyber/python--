"""
14. mimic

Neste desafio você vai fazer um gerador de lero-lero.

É um programa que lê um arquivo, armazena a relação entre as palavras e
então gera um novo texto respeitando essas relações para imitar um
escritor de verdade.

Para isso você precisa:

A. Abrir o arquivo especificado via linha de comando.

B. Ler o conteúdo e separar as palavras obtendo uma lista de palavras.

C. Criar um dicionário de "imitação".

Nesse dicionário a chave será uma palavra e o valor será uma lista
contendo as palavras que aparecem no texto após a palavra usada na chave.

Por exemplo, suponha um arquivo com o conteúdo: A B C B A

O dicionário de imitação deve considerar que:
* a chave A contém uma lista com a palavra B
* a chave B contém uma lista com as palavras C e A
* a chave C contém uma lista com a palavra B

Além disso precisamos considerar que:
* a chave '' contém uma lista com a primeira palavra do arquivo
* a última palavra do arquivo contém uma lista com a palavra ''.

Com o dicionario imitador é bastante simples emitir aleatoriamente texto
que imita o original. Imprima uma palavra, depois veja quais palavras podem
vir a seguir e pegue uma aleatoriamente como a proxima palavra do texto.

Use a string vazia como a primeira palavra do texto para preparar as coisas.

Nota: o módulo padrão do python 'random' conta com o random.choice(list),
método que escolhe um elemento aleatório de uma lista não vazia.
Abaixo segue um exemplo de execução do seu programa:

"""
import random
import sys


def mimic_dict(filename):
     """Cria um dicionário de imitação a partir do arquivo fornecido."""
     with open(filename, 'r') as arquivo:
         texto = arquivo.read().lower().split()
         dicionario = {}

         # Considera a palavra vazia
         primeiro = True
         for i in range(len(texto)):
             palavra = texto[i]
             if primeiro:
                 dicionario[''] = [palavra]
                 primeiro = False
             else:
                 if texto[i - 1] not in dicionario:
                     dicionario[texto[i - 1]] = []
                 dicionario[texto[i - 1]].append(palavra)

         # Adiciona a última palavra
         if texto:
             ultima_palavra = texto[-1]
             if ultima_palavra not in dicionario:
                 dicionario[ultima_palavra] = []
             dicionario[ultima_palavra].append('')

         return dicionario

# sua solução #
def print_mimic(mimic_dict, word):
     """Gera e imprime um texto de 200 palavras usando o dicionário de imitação."""
     texto = []
     for _ in range(200):
         texto.append(word)
 # Obtém a próxima palavra a partir da palavra atual
         palavras_possiveis = mimic_dict.get(word, [])
         if not palavras_possiveis:
             break  
    # Se não houver palavras possíveis, finalize
         word = random.choice(palavras_possiveis)

     print(' '.join(texto))

# chamada do programa
def main():
     """Função principal para execução do programa."""
     if len(sys.argv) != 2:
         print('Utilização: ./14_mimic.py file-to-read')
         sys.exit(1)

     dict = mimic_dict(sys.argv[1])
     print_mimic(dict, '')

if __name__ == '__main__':
     main()


