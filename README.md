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

