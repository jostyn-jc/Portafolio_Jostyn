# Jostyn-Jaya

Proyecto de logica de programacion: generador de contraseñas seguro
Fecha:28 de junio del 2026

1. Objetivo del sistema
   
   Desarrollar un sistema funcional que automatice la creacion de contraseñas seguras y aleatorias, permitiendo que las personas mejoren la seguridad de sus cuentas digitales de manera sencilla y rapida, evitando el uso de contraseñas vulnerables.

2. Descripcion de funcionalidades

   El sotfware actua como un asistente de seguridad con las siguientes capacidades
   Validación de datos de entrada: El sistema verifica que el usuario ingrese un valor numérico válido y restringe la longitud a un mínimo de 4 caracteres para garantizar una seguridad básica.
   Generación aleatoria de caracteres: Utiliza una lógica de selección basada en una biblioteca de caracteres (que abarca letras mayúsculas, minúsculas, números y símbolos especiales) para crear claves robustas y difíciles de descifrar.
   Interfaz de usuario simplificada: Proporciona un entorno de consola intuitivo que guía al usuario paso a paso durante la solicitud de parámetros y la entrega del resultado final.
   Control de flujo lógico: El sistema garantiza que el proceso no se interrumpa ante errores de entrada, ofreciendo al usuario la oportunidad de corregir su selección de forma inmediata.

3. Introduccion

   La tecnología ha transformado nuestra forma de interactuar en los entornos digitales, haciendo que la seguridad de nuestras cuentas personales sea una prioridad. Este proyecto presenta un generador de contraseñas seguro desarrollado en Python, diseñado específicamente para resolver el problema de la debilidad en las claves de acceso, aplicando principios de lógica de programación para proteger la identidad de las personas.

4. Descripcion del problema

   Actualmente, muchas personas utilizan contraseñas poco seguras o fáciles de adivinar, lo que facilita el robo de identidad y el acceso no autorizado a información sensible. El problema radica en el pensar contraseñas seguras es un proceso tedioso y demorado. Este software resuelve dicha problemática automatizando la creación de claves mediante combinaciones aleatorias de caracteres.

5. Relacion con los contenidos de la asignatura

   Este generador de contraseñas integra los conceptos aprendidos durante el modulo:
   Estructuras condicionales: Utilizadas para validar que la entrada del usuario sea correcta y manejar excepciones.
   Estructuras repetitivas: Se empleó un ciclo while para asegurar la entrada correcta de datos y un ciclo for para la construcción iterativa de la contraseña basada en la longitud deseada.
   Organización del código: El proyecto se estructuró en bloques lógicos claramente definidos para facilitar su mantenimiento y comprensión.

6. Explicacion del sistema desarrollado

   El sistema es una herramienta basada en una interfaz de consola que solicita al usuario la longitud deseada para su contraseña. El programa incluye una validación inicial para garantizar que la entrada sea numérica y mayor o igual a 4 caracteres, evitando errores. Una vez validado, el sistema utiliza una cadena de caracteres que incluye letras (mayúsculas y minúsculas), números y símbolos especiales, seleccionando elementos al azar mediante la librería random para construir la contraseña final y presentarla al usuario.

7. Cronograma de desarrollo

   Semana 1 seleccion del tema: Elección del generador de contraseñas como solución informática
   Semana 2 diagrama de funcionalidad: Diseño del diagrama de flujo lógico para la generación de claves
   Semana 3 desarrollo de software el entorno: Configuración del repositorio en GitHub y preparación del entorno
   Semana 4 desarrollo de estructuras logicas: Implementación de validaciones con if/else y try-except
   Semana 5 desarrollo de estructuras repetitivas: Programación del bucle while y generación de la contraseña con for
   Semana 6 tecnicas de programacion funcional: Optimización y comentarios del código para mejorar la legibilidad
   Semana 7 integracion de informacion: Finalización de la documentación técnica y el archivo README
   Semana 8 entrega final: Revisión del software funcional y preparación de la presentación.

8. Reflexion sobre el impacto de la tecnologia

   El desarrollo de esta herramienta nos permite comprender que como estudiantes, tenemos la capacidad de crear soluciones para problemas reales de seguridad. La automatización de procesos simples, como la generación de contrasenas, es un paso fundamental hacia una cultura de seguridad digital más responsable en la sociedad actual. Al programar este generador, he podido reflexionar sobre cómo la tecnología no solo sirve para facilitarnos la vida diaria, sino que es una herramienta indispensable para proteger nuestra información personal en un mundo cada vez más conectado. En conclusión, este proyecto demuestra que la lógica de programación aplicada correctamente permite transformar una vulnerabilidad común en una solución técnica accesible y efectiva
