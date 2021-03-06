# Diccionario

## Git

Sistema de control de versiones.

## Servidor

Cualquier equipo conectado a internet que permite que se conecten otros equipos a él. Permiten accesos masivos, gran ancho de banda y siempre encendidos.

## Backend

Todo lo que se hace en el servidor.

## Frontend

Lo que se hace para el cliente.

## ETL

Extract Transform Load. Datos: extraer, reformatear, limpiar, cargar, analizar, reutilizar. Extracción: calidad. Transformación: traducir código, unir datos, agrupar. Cargar: sobreescribir, duplicar, añadir.

## API

Interfaz de Programación de Aplicaciones. Interfaz para que se comuniquen aplicaciones de SW y compartan datos entre ellos.(Locales, Remotas: SOAP, REST)

## BBDD

Conjunto de información almacenado y consultado sistemáticamente (relacionales, NoSQL, autogestionadas...)

## Notación O grande

Análisis de algoritmos para estimar consumo de recursos de un algoritmo. Razon de crecimiento: razón a la cual el costo de un algoritmo crece conforme el tamaño de la entrada crece (eficiencia)

## Redes
- Router: gestor que conecta el ordenador con las redes (puesta de enlace, gateway)
- Hub: conecta varios dispositivos a una red interna. Tiene varios puertos ethernet (el envío de datos se da a todos los dispositivos conectados)
- Switch: un hub inteligente, se aprende las direcciones físicas de los dispositivos conectados (MARC) reduce tráfico y es más seguro que hub
- TCP/IP: protocolo de comunicación de redes
- IP: 32 bits, dentro de una red no se repiten
- MAC: matrícula del pc
- DNS: Domain Name System (traduce el nombre del buscador a su IP)
- HTTP: protocolo de transferencia de hipertexto
----------------------------------------------------------
- Packet-tracer: software de simulación de redes (CISCO)
- Red informática: conjunto de equipos conectados entre sí capaces de intercambiar información.
- Internet: red WAN (Wide Area Network) más grande que existe. Protocolo TCP/IP.
- WWW: (Worl Wide Web) Es un servicio sobre la infraestructua Internet.
- Red PAN: Personal Area Network (ejemplo hogar)
- Red LAN: Local Area Network (ejemplo ofinas)
- Red MAN: Metropolitan Area Network (ejemplo empresas grandes)
- Red WAN: Wide Area Network (ejemplo internet)
- Red GAN: Global Area Network (ejemplo companía internacional)
- Topologías de redes: ring, mesh, star, line, tree, bus, fully connect

## Seguridad

- Malware: malicious software. Tipos:
  - Virus: busca alterar el correcto funcionamiento. Necesita ser ejecutado por el usuario
  - Gusano: no necesita intervención del usuario. Puede replicarse y enviar copias a otros usuarios
  - Troyano: va dentro de un programa legítimo para introducirse en el equipo. No se propaga a sí mismo. Buscan acciones ocultas: robar información, abrir puertas traseras
  - Spyware: se instala por si solo mediante una segunda aplicación. Busca recolectar información
  - Adware: no siempre es dañino. Busca mostrar publicidad. Se instala a travñes de la instalación de otras aplicaciónes
  - Ransomware: secuestra datos del ordenador y pide rescate económico. Suele darse a través de un gusano o malware
- Tipos de ataque:
  - DDoS (denegación de servicio): ataque que busca tirar el servidos con una sobrecarga de solicitudes
  - Inyeccion SQL: fragementos de código que se introducen por ejemplo a través de formularios para obtener información y alterar las BBDD
  - Man in the middle: interceptar una comunicación entre dos sistemas
  - XSS: inyectar un script en la salida de una aplicación web y ejecutarlo en el navegador del cliente
  - Ingeniería social: manipular a las personas para que compartan información (Phising: capturar información personal mediante técnicas engañosas)
 - Pentesting: práctica de atacar diversos entornos con la intención de descubrir errores, vulnerabilidades, fallos de seguridad.
 
 ## PLN
 
 - Expresión regular/regex: patrones usados en programación para encontrar una combinación de caracteres dentro de una cadena de texto (busqueda de elementos en textos, reeemplazar, validar información de formularios, automatizar acciones, reformatear texto, scrapping...)
 - Web scrapping: técnicas de extracción de datos de una web de forma automatizada (convertir en BBDD estructurada la información publicada en web)
 - Crawling: es el algoritmo que se mueve por las webs imitando el comportamiento humano.
 - PLN: procesamiento del lenguaje natural (modelos lógicos gramaticales, modelos probabilísticos)
 - Machine learning: capacidad de una máquina o SE para aprender mediante la adaptación de algoritmos de su programación respecto a la entrada de datos (aprendizaje supervisado, aprendizaje no supervisado, aprendizaje por refuerzo)
 - Deep learning: es un tipo de machine learning que permite entrenar a una computadorapara que realice taread de forma similar a como las realizan los seres humanos

 ## HTML
 
 - HTML: Hypertext Markup Language. Lenguaje de marcado qu los navegadores saben interpretar.
 - CSS: lenguaje que define la apariencia de un documento escrito en lenguaje marcado.
 - JavaScript: lenguaje de programación que funciona de manera nativa en los navegadores (lenguaje interpretado).
 - Responsive Design: técnica que permite tener una misma web adaptada a las diferentes plataformas (PC, tablet, smartphone) (librería: bootstrap).
 - API tensorflow.js: permite hacer IA en el navegador.
 
 ## SQL
 
 - SQL: Structure Query Language. Lenguaje de consulta estructurada utilizado para administrar y recuperar informacion desde sistemas de gestión de BBDD relacionales (Ejemplo comandos: SELECT, WHERER, INSERT, DELETE, UPDATE)
 - BBDD relacional: colección de elementos de datos organizados en un conjunto de tablas conformadas por filas y columnas a través de las cuales se puede acceder a la información para leerla, cambiarla, borrarla o insertar nuevos datos.
 - Datos estructurados: normalmente archivos de texto en formato tabla, hojas de cálculo o BBDD relacionales con títulos en cada catergoría que permite identificarlos. Los datos pueden ser ordenados y procesados fácilmente por herramientas de minería de datos.
 - Datos no estructurados: datos binarios que no tienen estructura interna identificable. Conglomerado masivo y desorganizado.
 - IA: combinación entre estadística, matemáticas e informática para organizar e interpretar datos de diferentes fuentes y extraer conocieminto para posteriormente extrapolarlo y generalizarlo.
 
  ## Rendimiento de las aplicaciones IA
 
 - Concurrencia: capacidad de ejecutar un programa o parte en desorden sin afectar al resultado final
 - Latencia: tiempo que tarda en transmitirse un paquete dentro de la red
 - Eficiencia algorítmica: término usado para describir aquellas propiedades de los algoritmos que están relacionadas con la cantidad de recursos utilizados. (la eficiencia depende de lo que se considere prioritario: complejidad de tiempo, complejidad de espacio)
 - Notación asintótica: permite respresentar la complejidad de los algoritmos de manera independiente al HW (ejemplo: notación O Grande. Coste de un algoritmo en función de los parámetros de entrada)
- Notación O Grande: herramienta funcional para determinar la complejidad de un algoritmo, trata de medir el número de operaciones (como unidad básica de cálculo) para resolver un problema dado. Términos de complejidad: constante(O(1)), lineal(O(n)), logarítmica(O(log n)), cuadrática(O(n^2)), exponencial(O(2^n)), explosión combinatoria(O(n!)) 
 
 ## Estadística descriptiva
 
 - Estadística descriptiva: organiza, reúne y comunica información numérica. Tendencia central: media, mediana, moda. Medidas de dispersión: varianza, desviación estándar, rango. Medidas de distribución:campana de Gauss (simetría, curtosis)
 - Etapas de un proceso de análisis de datos: definir el problema, recolección de datos, limpieza de datos, exploración mediante estadística descriptiva, análisis mediante estadística inferencial, conclusiones.
