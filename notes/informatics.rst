Informatics
###############

.. contents:: Table of contents

Databases
************
Relational databases
======================
A relational database is a digital database whose organization is based on the relational model of data, as proposed by E.F. Codd in 1970. This model organizes data into one or more tables (or "relations") of rows and columns, with a unique key for each row.

Prior to the advent of this model, databases were usually hierarchical, and each tended to be organized with a unique mix of indexes, chains, and pointers. The simplicity of the relational model led to it soon becoming the predominant type of database.

Virtually all relational database systems use SQL (Structured Query Language) as the language for querying and maintaining the database.

ACID Properties
-----------------
In computer science, **ACID** (*Atomicity, Consistency, Isolation, Durability*) is a set of properties that guarantee that database transactions are processed reliably. In the context of databases, a single logical operation on the data is called a transaction. 

- *Atomicity* requires that each transaction be "all or nothing": if one part of the transaction fails, the entire transaction fails, and the database state is left unchanged.
- *Consistency* property ensures that any transaction will bring the database from one valid state to another.
- *Isolation* property ensures that the concurrent execution of transactions results in a system state that would be obtained if transactions were executed serially, i.e., one after the other.
- *Durability* means that once a transaction has been committed, it will remain so, even in the event of power loss, crashes, or errors.

Join clause
---------------
A *join clause* combines records from two or more tables in a relational database. It creates a set that can be saved as a table or used as it is.

Non-relational databases
===========================
A NoSQL (often interpreted as Not only SQL) database provides a mechanism for storage and retrieval of data that is modeled in means other than the tabular relations used in relational databases. Motivations for this approach include simplicity of design, horizontal scaling, and finer control over availability. The data structures used by NoSQL databases (e.g. key-value, graph, or document) differ from those used in relational databases, making some operations faster in NoSQL and others faster in relational databases. The particular suitability of a given NoSQL database depends on the problem it must solve.

Most NoSQL stores lack true ACID transactions or Join clause, although a few recent systems have made them central to their designs. NoSQL databases are increasingly used in big data and real-time web applications. NoSQL systems are also called "Not only SQL" to emphasize that they may also support SQL-like query languages. The NoSQL discussions become strong around 2009.


Definitions
**************
Vocabulary
============
"Out of the box" (feature)
-----------------------------
An out of the box feature or functionality, particularly in software, is a feature or functionality of a product that works immediately after installation without any configuration or modification.

Internationalization and localization (i18n)
---------------------------------------------
In computing, internationalization and localization are means of adapting computer software to different languages, regional differences and technical requirements of a target market (locale).

The terms are frequently abbreviated to the numeronyms ``i18n`` (where 18 stands for the number of letters between the first i and the last n in the word “internationalization,” a usage coined at DEC in the 1970s) and ``L10n`` for "localization", due to the length of the words.

Grammars for text parsing
--------------------------
Backus-Naur Form (BNF), Extended Backus-Naur Form (EBNF) and regular extensions to BNF: 
    http://matt.might.net/articles/grammars-bnf-ebnf/

Principle of least astonishment
--------------------------------
"if a necessary feature has a high astonishment factor, it may be necessary to redesign the feature."
    https://en.wikipedia.org/wiki/Principle_of_least_astonishment

Tips
*******
- http://www.howtogeek.com/189974/how-to-share-your-computers-files-with-a-virtual-machine/

Links
*********
- http://overapi.com/

- http://ppenteado.net/
    > Teaching
    
- https://lai.iag.usp.br/projects/seminarios-gai/wiki

- http://research.microsoft.com/en-us/collaboration/fourthparadigm/

- http://rosettacode.org/

- http://ccsl.ime.usp.br/
