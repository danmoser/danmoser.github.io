Bravo
########

.. contents:: Table of Contents


Meetings
***********
Meetings (absence)
====================
- March
- April
- May

Meeting 05/02/16
==================
- Daniel não poderá comparecer
- Avanços no Data Publish VO

Daniel: Data Publishing
--------------------------
- Contato inicial Vinicius
- VMs criadas (Debian 8), com usuários sudoers Daniel, Antonio, Vinicius e Walter.

Extra
------------
- Daniel recomenda serviços (básicos) de VM da Digital Ocean. Há opções de servidores a partir de USD 5/mês (https://www.digitalocean.com/pricing/). Outras opções são http://linode.com/ e http://cloudsigma.com/.

Meeting 08/01/16
==================
- Daniel relata planejamento do Data Publishing com Walter e contato com os voluntários.
- Paulo contar sobre o protótipo do Titanbrowse, serviço que ele gostaria de disponibilizar através do servidor BRAVO
- Paula quer conversar sobre pedido de financiamento FAPESP

Antonio e C. Paladini também presentes.

Paulo: Titanbrowse
---------------------
- Serviço Web para acesso de imagens de sensoriamento multi-spectral, rodando para testes na Amazon Cloud.
- Uso de < 20 GB de dados, idealmente 100 GB. 
- Implementado em Java. Contém visualização global, de cada cubo; poderosa ferramenta de busca com base nos meta-dados. 
- Implementado em IDL, operações vetoriais em tabelas. Abandonou SQL por ser muito dependente de strings.
- Adql* seria possível; a ser implementado. Pode-se facilmente na solução implementar uma fórmula complicada para buscas/relacionar dados.
- Ideia é disponibilizar online, principalmente para facilitar problemas de instalação.
- Falta implementar acesso aos protocolos VO. 

Infra BraVO
------------
- 2 servidores físicos. TALVEZ no futuro, um para deployment e um aplicações estáveis. 
- OpenNebula criando VMs.
- "Dockers" como alternativa à VM (quando VM são similares).


Extra
----------------------
- Paula: Financ. FAPESP p/ layers SSDs e outros. Problema: pedido recusado. Motivos XYZ... Não temos $$ para adquisição, e dentro do pedido pedindo incluir um bolsa analista (FTE). 
- Quer tentar novamente... Pedidos de instrumentação (projetos técnicos). P/ FAPESP, pouca ciência (= projeto técnico). Claudia Medeiros é simpatizante. Embarcar como e-Science (novo, já saiu edital), computação...
- FAPESP, dificuldade de obter financiamento. Falta $$, INCT-A acabou, o novo (Beatriz), postergado para "resposta" em abril/junho, para começar no fim do ano (sendo otimista). 
- Pergunta Antonio: outras fontes de financiamento. 
- Alberto: vale a pena fazer. e-Science (21/março). Resposta sai em outubro. Precisa ter gente da computação. 
- Tentativa pedido na computação, impossível sem networking pesado, necessidade de resposta rápida. 
- Alex: conversar com a Claudia Medeiros, e transformar e-Science em projeto de pesquisa. 
- Antonio: vai conversar com contato na FAPESP e possíveis empresas. 
- Alberto: tem $$ para os IVOAs. 

Daniel: Data Publishing
--------------------------
Contato com Walter: separar Data Publishing de Data Center por vezes é muito difícil... Tentativa de juntar esforços.

Dúvida: os voluntários são para ajudar no Data Publishing e Data Center, correto?? R: Sim.

Vinicius indisponível até meados de Fevereiro. Antonio demonstrou interesse, mas não avaliou em detalhes a parte técnica até meados de dezembro.

No "how to publish" do IVOA, só 2 toolkits apresentam conteúdo em Python: CVO e GAVO. Acionei o suporte de ambos e, como de costume no pessoal de VO, eles foram super prestativos. O CVO na verdade tem muita coisa em Java, nem tudo está livre (por agora?), enquanto que o GAVO tem tudo livre e excelente documentação. Nas palavras do Patrick Dowler (CVO):

    *Our approach differs somewhat from GAVO: opencadc provides a toolkit (libraries) from which you can assemble and customise VO services, while GAVO provides a more works-out-of-the-box framework that you can configure. We are moving to providing a better starting point through some example service projects and HOWTO documentation, but really our s/w is for shops that want to run highly scalable and robust services, customise the behaviour in some cases, and support a variety of authentication mechanisms and back-end systems.*
    
Deliberado
~~~~~~~~~~~~~~~~~~
- Abrir 2 VMs no mesmo servidor no LAi (open nebula), baseadas no Debian.
- Solução Canadá (Antonio) e GAVO-Dachs (Daniel).
- Acesso externo (VPN) precisa ser confirmada. 
- Walter: (Sra.) chefe do VO da Africa do Sul demonstrou sinergia. Eles também estão no início, (talvez) convergencia. Bom para representar o BraVO na próxima reunião IVOA.

Meeting 04/12/15
==================
- Paula passar o status da sinergia BRAVO & S-PLUS
- novos integrantes do BRAVO, voluntários fora da area académica
- emails diversos de interesse no BRAVO que eu recebi
- estabelecermos uma telecom regular, 1x por mês

S-Plus
--------
Survey, sinergia com J-PAS e J-Plus.

BraVO publicação do S-Plus VO complaied. 
Paula está com data management do S-Plus.
BraVO tem servidor para isso comprado pelo INCT-A no LAi. 
1o. VO archive no Brasil.

Paula fazendo documentação. Ajuda bemvinda.

Voluntários
------------
Pessoas vêem as páginas e se oferecem para ajudar.

2 voluntários potenciais: Nenhum é astrônomo. São da computação.

Antonio (?), ajuda em 3 frentes: 
    - gerenciamento do servidor hardware. "OpenNebula" instalado, mas ninguém conhece no LAi. 
    - Software, como configurar e dividir os serviços. 
    - ?

Vinicius, desenvolvedor de sistemas, querem participar das soluções de data publishing. Houve chamadas dos "Casos de Usuário", e ninguém foi capaz de resolver (comercialmente). Dados interoperados, públicos, ...

Para S-Plus, é necessário soluções comerciais.

Paula e Alex verão sobre a contribuição do Carlos Paladini (LAi).

Beacon e caso de usuário
-------------------------
Daniel assume o caso com Vinicius e Antonio para colaboração no data publishing.

Pessoal
----------------
Paulo Pessoal: definição para 6 meses.

Walter: focado para S-Plus. Toolkit existe (alemão).
    - "Cesca": centro para o J-Plus. Equipe técnica grande. Database do J-PAS/+, com ferramentas e serviços VO.
    - Framework in Python (web): Pyramid (http://www.pylonsproject.org/). Do "zero" e tudo livre. 
    - Enviará mais detalhes técnicos por e-mail.

Reuniões
-----------
1a (ou 2a) sextas-feiras do mês.


Data Publishing Info
***********************
Visão geral
==============
- A IVOA (http://ivoa.net) definiu uma série de serviços web chamados VO
- O Brasil (i.e., nós!) somos membros da IVOA através do BRAVO, que só conta com trabalhos voluntários.
- A Paula está no Data-Management do survey astronômico S-plus (http://www.iag.usp.br/labcosmos/en/s-plus/) e quer publicar os dados em VO
- O Walter é um post-doc do IAG que usará os dados do S-plus para sua pesquisa e está ajudando a Paula
- Eu sou um post-doc que estou no Chile e que tenho outras observações para publicar em VO, assim como dados de modelos
- O que percebemos é que é muito difícil separar VO data publishing (meu caso) de VO data center (caso do S-plus)...
- Você e o Antonio são parte do time para ligarmos os pontos entre astronomia e computação, junto comigo e o Walter (e a Paula, quando der).
- No BRAVO também contamos com outros 2 post-docs (Alberto, em Portugual) e Paulo (nos EUA), e o prof. Alex (IAG) e que eventualmente nos ajudarão. 
- Vamos testar 2 soluções: a do GAVO-Dachs (Alemanha) e a do CADC (Canadá). Para isso, criamos 2 VMs no servidor do BRAVO.

S-Plus survey
===============
S-Data managements docs no GoogleDrive.

Dados técnicos:
    - Virtualização com OpenNebula.
    - Volume de 100 TB/ano.
    - 2 tipos de transferências do Cerro Tololo para LAi: raw_data e *pré-processados*.
    - VO Space público (e privato).
    - Data Publishing, Toolkit CVO ou GAVO


ceFca notes
--------------
Walter
~~~~~~~
VO CEFCA (random notes)

- Implementation from scratch
- All libraries/dependencies used are open source

- Storage:
    - 2x14TB SSD for database and web services (for S-PLUS for now)
    - HDD for images, accesible only when needed by the web services

- Database:
    - Postgres + python codes

- From pipeline to public:
    - Databases used in the pipeline are different than for the public access (note from Walter)
    - So we would need from CEFCA the database schemas (tables, columns, ...)
    - pyramid web framework app based on python + VO Services (TAP, etc) -> cone search/"skyserver" -> use alladin, etc

- Front end:
    - implemented Apache HTTP server
    - implemented website (similar to sdss' skyserver) (even more user friendly), with form searches, SQL searches, cross-match, etc.

Paula
~~~~~~~~
* implementation done from scratch in Python

    are there libraries?
        JH: we used libraries (astropy, pywcs,...)

    are we considering shoaring our implementations?
        JH: we should improve a bit the implementation

    Both JH and Tamara never heard about VO before arriving here. None of them has ever attended an IVOA-interop meeting

    JH: the development is "very specific" and oriented to our data

* Hired

    JH hired for db management and publishing (which ended up being VO)

* Public and private access

    Phase 3 data not public and not accessible via web-portal

    Phase 2 will be private.
    Password protected data-access (certainly works with Topcat and Aladin)

* protocols

    Cone search, TAP, SIAP

    SSAP still pending

* Data models

    Interops working on data-models on data-cubes
    ceFca could get involved at some point

* Database

    Deisgned by JH and Tamara
        It is postgresNG
    
    Why postgres?
        JH: people here were using mySQL. We evaluated the possibilities but JH knew postgres which is known to manage big amount of data better than mySQL and with a bigger data model.

    Do IVOA db documents leave freedom of db implementation?
        JH: totally free

* Where does the system becomes "VO-compliant"?

    The db can be any. The Python layer receives VO-compliant requests, queries the db
        and gives VO-compliant replies.

* Registry

    The service will be registered (possibly to the euro-vo registry with the help of SVO)

Caso de Usuário Beacon
========================
TBD


VMs
================
Acesso
--------
- `LAi form <https://docs.google.com/forms/d/1mKY9AB-8V73VYz1MXVV3t4sKxcEMYrRyolhX7zHJ8no/viewform?formkey=dERKVTJzU25LdW9mMEUzYVRWS0FkX2c6MA>`_
- "gina", 143 107 18 54, porta 20001
- VPN?

Dachs
---------
- Debian 8.2
- 10.180.0.225
- **Dachs instalado**

CADC
--------
- Debian 8.2
- 10.180.0.226



VO key concepts and vocabulary
*******************************
VO Basics
============
What is a VO?

- *Wikipedia*: "VO is a collection of interoperating data archives and software tools which use the internet as research environment"

- IVOA (developer PoV): "VO is a ecosystem of mutually compatible datasets, resources, services, and software tools which use a common set of technologies and a common set of standards. They aren't just rules, but include *middleware*: registry services, distributed storage, sign-on services, etc.

VO was built on top of Internet standards, specially HTTP and XML, SOAP/WSDL or REST for description of the web services.

*VO service* term has a wide application, but usually means "anything that does something for you, implying a communication between two or more computers".

*VO resource* comprises web pages, database, storage element, interactive application - anything that is uniquely addressable through the Internet.

VO architecture
::

    |            USER LAYER
    | REGISTRY                 DATA ACCESS
    | (Finding)    VO CORE     (Getting)
    |                          PROTOCOLS
    |        RESOURCE LAYER

Development according to the TCG (Technical Coordination Group).
    
Key standardization areas
==========================
Data access
------------
What defines a target: RA, DEC (and a radius in a search). 
    - SIA = images
    - SSA = spectra
    - SCS = source catalogues
    - ... several others

TAP: Table Access Protocol, access to more complex search, as date, filters, etc.

SQL queries (very limited), lead to ADQL development (Astronomical Data Query Language), dealing with strings and XML formats.

**VO do not dictate what deployers do internally, but rather simply to make them commit to standard interfaces**.

VO Table is a *exchange* medium, not a primary storage format.

Resources and registries
--------------------------
- Resource Identifier: how to uniquely specify a resource
- Resource Metadata
- Resource Registries: yellow pages, that **there isn't a unique centralized registry**. 

- Registry Interface: describes the standardized way in which applications should communicate with registries:
    - Searchable registries (queries)
    - Publishing registries (place of information)

In VO exists a registry of registries.

Data modeling and semantics
-----------------------------
A cone search returns much more than RA and DEC if columns are standard. 
    - Phot DM = photometric data
    - Obs. core DM = collections of observational data
    - VO event = transient events

Standard *UTypes*: how to define elements of a data model.
    - STC: Space-Time Coordinates
    - UDC: Universal Content Descriptors

Sharing: Distributed Computational Infrastructure
----------------------------------------------------------
**IVOA needs highly technical standards to specify how services glue together**. 
VOSI: VO Support Interfaces.

*Web Services Basic Profile* is a kind of guidebook for constructing web services that complies with both general web standards and IVOA standards. Universal Worker Service, JDL (Job Description Language).

*Vo Space* is the ability to share stored information through the VO standard.

**VO philosophy is not to mandate any particular remote storage technology, but just to specify how to interface to such a remote storage system**.

A participating system has to have a unique address following the ``vos://aaa.bbb.ccc/xxx`` form, to provide methods.

Sharing: Collaborative Space, Authentication, etc
----------------------------------------------------
The initial stages of VO development relied on fully public data. However, much of astronomy involves data with proprietary access. This requires a standard definition of identity, methods for authenticating, authorize the used, etc.

VO uses the system of public key encryption, X509 certificates, TLS...

Sharing: applications
----------------------
Rather that mega-application, it is more efficient if smaller apps specialize in particular jobs and communicate between each other. The ways are VO Tables and SAMP (Simple Application Message Protocol), ``a hub and spokes`` communication method.

Any SAMP-compatible application can start a Hub if there isn't one already running.

What standards do I want?
--------------------------
Depends on what you want to do. 

- Data center: SIA, SCS, TAP, etc. How to parse incoming ADQL queries. Set up its own publishing, registry. "Full searchable registry" is related to the VO Space implementation, that may require a SSO (Single Sign-on) method.

- Application writer: how to query a registry. How to query one or more types of data service. How to understand VO Tables. How to speak to SAMP hub.


Vocabulary
*************
- API: application programming interface, is a set of routines, protocols, and tools for building software applications. Em geral, está associada a capacidade de se passar uma instrução por uma linha de comando.

- JSON: JavaScript Object Notation), is an open standard format that uses human-readable text to transmit data objects consisting of attribute–value pairs. It is the primary data format used for asynchronous browser/server communication (AJAJ), largely replacing XML (used by AJAX).

- OWL: Ontology Web Language: W3C specs.

- RDF: Resource Description Framework: W3C specs.

- REST: Representational State Transfer is the software architectural style of the WWW.

- RESTful: conform to the constraints of REST. 

- Semantic Web: extension of WWW by W3C.

- SKOS (related to RDF)

- SOAP: Simple Object Access Protocol, XML based. Is a protocol specification for exchanging structured information in web services. 

- (Apache) Spark: is a fast and general engine for big data processing, with built-in modules for streaming, SQL, machine learning and graph processing.

- Spoke-hub distribution paradigm: is a system of connections arranged like a wire wheel (as a bike wheel) in which all traffic moves along spokes connected to the hub at the center.

- URI: Uniform Resource Identifier, is a string of characters used to identify the name of a resource. Such identification enables interaction with representations of the resource over a network, typically the World Wide Web, using specific protocols. Schemes specifying a concrete syntax and associated protocols define each URI.

- WADL (related to WSDL)

- Web Service: is a service offered by a device in the WWW. Example, HTTP.

- WSDL: Web Services Description Language, XML based. Is an *interface definition language* that is used for describing the functionality offered by a web service.






