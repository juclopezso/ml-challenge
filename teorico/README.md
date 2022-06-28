# Desafía teórico


## Procesos, hilos y corrutinas
Un caso en el que usarías procesos para resolver un problema y por qué
- R. Un proceso en computación se refiere a una actividad que ejecuta instrucciones junto a unos datos asociados. Estos procesos pueden tener uno o varios hilos de control, tradicionalmente, sólo tienen un hilo de control. Usaría los procesos (con un sólo hilo) para muchas tareas de programación que no necesiten ejecutarse de forma paralela o concurrente, como una única consulta a una API, operaciones matemáticas o escritura de un único elemento en base de datos.

Un caso en el que usarías threads para resolver un problema y por qué.
- R. Los hilos permiten ejecutar tareas de programación al mismo tiempo que otras tareas, en otras palabras, permite ejecutar varias tareas paralelo. Usaría los hilos para ejecutar una tarea en segundo plano, por ejemplo, en una página web donde el usuario pueda ingresar texto y este se guarde de forma automática en base de datos. Un hilo se encargaría de recibir las interacciones del usuario y el otro de guardar los datos ingresados de forma paralela.

Un caso en el que usarías corrutinas para resolver un problema y por qué.
- R. La concurrencia permite ejecutar distintas o varias partes de un algoritmo o programa de forma desordenana sin afectar su resultado, es decir, una operación puede avanzar sin esperar que las demás terminen de ejecutarse. Usaría las corrutinas para ejecutar una tarea donde se deba hacer muchos llamados a APIs, ya que si se ejecutan de forma secuencial, cada llamado debe ser esperado a que termine su ejecución y seguir con el siguiente llamado. En cambio, de forma concurrente un llamado a la API se ejecuta pero no se espera su respuesta para hacer el siguiente llamado.


## Optimización de recursos del sistema operativo
Si tuvieras 1.000.000 de elementos y tuvieras que consultar para cada uno de ellos información en una API HTTP. ¿Cómo lo harías? Explicar.
- R. De ser posible (si el sistema cuenta con múltiples hilos), haría los llamados en un proceso con varios hilos de forma concurrente. Cada hilo se encargaría de una porción de las llamadas a la API y haría las llamadas de forma concurrente para que el hilo no deba esperar la respuesta del llamado para ejecutar el siguiente llamado.


## Análisis de complejidad
Dados 4 algoritmos A, B, C y D que cumplen la misma funcionalidad, con complejidades O(n^2), O(n^3), O(2^n) y O(n log n), respectivamente, ¿Cuál de los algoritmos favorecerías y cuál descartarías en principio? Explicar por qué.
- R. El algoritmo que descartaría sería el C (complejidad 2^n), ya que es el algoritmo que mayor complejidad tiene. Y el algoritmo que favorecería sería el D (complejidad n log n) ya que es el de menor complejidad de la lista. Por ejemplo, si el tamaño de input (n) es de 100, las operaciones que ejecutaría el algoritmo D serían 200, en cambio, para el algoritmo C serían aproximadamente 1.2*10^30.

Asume que dispones de dos bases de datos para utilizar en diferentes problemas a resolver. La primera llamada AlfaDB tiene una complejidad de O(1) en consulta y O(n2) en escritura. La segunda llamada BetaDB que tiene una complejidad de O(log n) tanto para consulta, como para escritura. ¿Describe en forma sucinta, qué casos de uso podrías atacar con cada una?
- R. La base de datos AlfaDB podría ser usada en un caso donde haya muy poca escritura de datos y muchas lectura de los mismos o donde sea muy importante la consulta rápida de datos. Un caso de uso podría ser un buscador de datos, en este caso sería muy importante la consulta de datos de forma rápida para un usuario y menos importante la escritura.
- R. La base de datos BetaDB podría ser usada en más propósitos que la anterior ya que tienen una complejidad de escritura igual a la de consulta. Un ejemplo específico sería un blog, donde las personas puedan postear entradas para que otros usuarios las consulten.