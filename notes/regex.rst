Expressões regulares (er, *re* ou *regex*)
#############################################

.. contents:: Table of contents

Palestra P. Penteado no GAi
==============================
Importância de manipulação de strings é negligenciada. Grande quantidade de informação é representada em strings (caracteres). E.g., internet e bancos de dados.

Um exemplo de falha de segurança por uma má parametrização de strings: Heartbleed bug, descoberto em Abril de 2014. Na época de sua descoberta, 17\% dos servidores web certificados por autoridades confiáveis estavam expostos a esta vulnerabilidade.

ASCII = única forma de codificar strins no 1980's.
    - 2$^7$=128 ASCII padrão fixo (até unicode); não há acentuação.
    - 2$^8$=256 ASCII extendido (várias versões)

Unicode foi desenhado para substituir o ASCII. Mais usados:
    - UTF-8 e Latin1, ou ISO 8859-1

Python: "\\u2207" (ou seja, codificação do binário 2207 em unicode, 'u') produz o caracter nabla.

Uma convenção com strings: string == "":
    - True, se string é vazio.
    - Falso, se não vazio (inclusive espaços ou tabulação).

Exemplo: regex '.+irg\\.cub' specifies:

- One or more occurences (+) of any character (.)
- followed by an occurence of irg.cub (the period is escaped with the backslash.

Alguns caracteres tem significado específico:
    - a|bc => "a" ou "b" seguido de "c"
    - a|b|c == [abc]
    - ^ = tudo, menos aquilo

Boa prática: SEMPRE comentar regex, para não ter que ficar "decifrando" a regra toda vez que ler o código.

Há uma função Python que troca caracteres especiais para ASCII.

Python
==========
Sources
---------
- https://docs.python.org/2/library/re.html
- https://docs.python.org/2/howto/regex.html
- http://www.tutorialspoint.com/python/python_reg_expressions.htm

- https://regex101.com/
- http://overapi.com/regex/

Examples
----------

.. code:: python

    """Code to remove linebreaks (useful blank lines instead)."""

    import re

    rule = r'^>([^\n\r]+)[\n\r]([A-Z\n\r]+)'
    
    regex = re.compile(rule, re.MULTILINE)
    matches = [m.groups() for m in regex.finditer(text)]
    
    for m in matches:
        print 'Name: %s\nSequence:%s' % (m[0], m[1])

    # Other way (MUCH better):
    re.findall(rule, text)#, re.DOTALL)

    # Another:
    returnmatch = re.compile(rule, re.MULTILINE).findall(text)

``(http(?!.*Trial.*))`` retorna todas as linhas iniciadas por "http" e que **não** contenham posteriormente a palavra "Trial" (case sensitive).

``([^\s]+)`` retorna palavra até o primeiro espaço/vazio.

.. code:: python
    
    def start_case_words(s):
        """ Function to put a string in Start Case. 
        
        It can by vectorized by numpy: ``vecstart = np.vectorize(start_case_words) """
        return re.sub(r'\w+', lambda m:m.group(0).capitalize(), s)

