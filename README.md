# Jogo Run n' Gun
Este foi um projeto desenvolvido como uma avaliação para a disciplina de Linguagens de Programação da graduação de Matemática Aplicada na FGV (Fundação Getúlio Vargas). Nesse projeto desenvolvemos um jogo no estilo Run n' Gun de plataforma baseado em jogos como "Contra". O objetivo do jogo é matar todos os inimigos e chegar à região verde ao fim do mapa.

## Assets
Retiramos as assets utilizadas no design do jogo a partir do site [https://bakudas.itch.io/generic-run-n-gun](https://bakudas.itch.io/generic-run-n-gun)

## Como Jogar
```
A e D: anda lateralmente para esquerda e direita
S: agacha
SPACEBAR: pula
MOUSE LEFT BUTTON: atira
R: recarrega
SPACEBAR + W: olha para cima
SPACEBAR + S: olha para baixo
```

## Como Executar o Jogo

1. Instale as dependências do projeto:
    ```
    pip install -r requirements.txt
    ```
 
2. Execute o script `main.py`:
    ```
    cd src/ 
    python3 main.py
    ```

## Como Rodar os Testes do Jogo:
1. Execute o script de testes do diretório raiz:
    ```
    python3 -m unittest
    ```
