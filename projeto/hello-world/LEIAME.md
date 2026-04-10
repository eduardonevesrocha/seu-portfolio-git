## Calculadora de Medias - CIn UFPE

Projeto pessoal feito por **Eduardo Neves** durante os estudos no CIn-UFPE.

Calcula a media de uma disciplina a partir das notas P1, P2 e P3 e informa
se o aluno foi aprovado, precisa de prova final ou foi reprovado, seguindo
os criterios do CIn.

**Como rodar:**

```
python script.py
```

**Criterios de aprovacao:**

| Media | Situacao      |
|-------|---------------|
| >= 7  | Aprovado      |
| 4-7   | Prova Final   |
| < 4   | Reprovado     |

Na prova final, a media final e calculada como `(media + nota_pf) / 2`.
Aprovado se media final >= 5.
