# Registro de resolução de conflito

O conflito aconteceu no arquivo `exercicios/ex03-conflito/REGISTRO.md`.

A ideia foi criar duas branches a partir de um mesmo ponto do projeto: `docs/conflito-a` e `docs/conflito-b`. Nas duas branches, eu alterei o mesmo trecho do mesmo arquivo, de propósito, para gerar um conflito real no momento do merge.

Na branch A, eu mudei a linha principal do arquivo e também adicionei uma linha extra. Depois disso, fiz o merge dessa branch na `main`.

Na branch B, eu também alterei essa mesma linha principal e adicionei outra linha extra. Quando tentei fazer o merge dela na `main`, o Git identificou que havia conflito, porque o mesmo trecho já tinha sido modificado antes pela branch A.

Para resolver, eu abri o arquivo manualmente, analisei as duas versões e decidi manter informações das duas branches, juntando o conteúdo de forma organizada em uma versão final.

Depois de ajustar o arquivo, marquei o conflito como resolvido com:

```bash
git add exercicios/ex03-conflito/REGISTRO.md
git commit -m "fix(ex03): resolve conflito de merge"