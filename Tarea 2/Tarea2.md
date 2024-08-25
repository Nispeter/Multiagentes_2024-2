# Tarea 2
Nicolas Parra Garcia\
2029422588
## Pregunta 1
### Comportamiento normal 
![alt text](image-6.png)
### 0 evaporation rate
![alt text](image-7.png)
Cuando no hay evaporacion los quimicos se mantienen en el mundo, haciendo que se acumule hasta que todos los patches tengan maximo valor, las hormigas no pueden diferenciar en donde esta la comida.
### 0 diffusion rate
Al no haber difucion los quimicos no se exparsen, creando lineas dificiles de seguir.
![alt text](image-11.png)
### max evaporation-rate
Es como si no hubiera quimico debido a que desaparece muy rapido.
![alt text](image-8.png)
### max difussion rate
El quimico es detectable de muy lejos por lo que confunde a las hormigas.
![alt text](image-9.png)
## Pregunta 2
- **SetupFood:** ![alt text](image-12.png)
- **to-go:**![alt text](image-15.png)
-**Uphill-chemical:**![alt text](image-22.png)
-**Wiggle:** ![alt text](image-14.png)
## Pregunta 3
Al recoger comida se hace la llamada a  uphill-nest-scent el cual verifica constantemente si la tortuga se encuentra en el nest, de lo contrario sigue el nest-chemical con un angulo de busqueda entre -45 y 45 grados y se mueve hasta llegar a este. 
## Pregunta 4
Comida equidistante\
Se puede observar que las hormigas obtienen comida de los 3 food source simultaneamente 
![alt text](image-5.png)
## Pregunta 5
Implementacion *naive* donde las hormigas recuerdan donde esta su hogar
![alt text](image-17.png)
![alt text](image-19.png)
## Pregunta 6
![alt text](image-21.png)\
Al no haber limite superior las hormigas se atascan, moviendose hacia donde hay mas concentracion de quimico, es decir en el camino y no en la comida. Esto hace que se corte el rastro de quimico.
![alt text](image-20.png)