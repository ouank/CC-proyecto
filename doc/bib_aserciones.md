# Elección y justificación de la biblioteca de aserciones usada.

La biblioteca de aserciones elegida es el [Assert Statement](https://docs.python.org/3/reference/simple_stmts.html#the-assert-statement) nativo de Python.

Lo he comparado con otras dos de las bibliotecas de aserciones más populares para Python, que son [assertpy](https://assertpy.github.io/docs.html) y [grappa](https://github.com/grappa-py/grappa).
Tanto assertpy como grappa están usando un lenguaje más natural para las declaraciones de asercion, lo que puede hacerlas más claramente legibles en el lenguaje natural inglés. Ambas bibliotecas son claramente más verbosas al escribir el código que una simple assert statement en su forma más sencilla. Si la decisión fuera entre esas dos, estoy a favor de assertpy ya que también sigue las expresiones regulares de Python comparadas con grappa, cuya sintaxis es un poco diferente. Pero, el assert statement nativa puede hacer todo lo que necesito (por ahora). Además, para mí las declaraciones de assert statements nativas en Python son más sencillo e intuitivas y por lo tanto, leer, escribir y debug será más fácil. Entonces, no prefiero añadir otra biblioteca que no añada valor extra a mi proyecto.  
Si en la continuación del proyecto se descubre que el assert statement nativo no es suficiente para mis necesidades, estoy dispuesto a cambiar de opinión (ya que esto también forma parte del proceso de aprendizaje).  

Addicionalmente, el marco de pruebas elegido será [pytest](https://docs.pytest.org/en/stable/), que apoya las assert statements nativas en Python (también trabajar con pytest y assertpy es possible).



