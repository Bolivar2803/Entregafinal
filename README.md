# Entregafinal
Robot recoje basura 

El desarrollo del sistema para seleccionar un objeto Wally involucra varios pasos y funcionalidades. A continuación, se explica el proceso de manera detallada:

El robot Wally comienza su operación desde una posición inicial llamada "home". Desde este punto de partida, Wally sigue una trayectoria predefinida para explorar el terreno en busca de un objeto objetivo. Durante esta exploración, Wally utiliza una cámara ubicada al lado de su garra para capturar imágenes del entorno.

La cámara del robot Wally juega un papel crucial en la búsqueda del objeto objetivo. A medida que avanza en su trayectoria de exploración, la cámara captura imágenes del terreno. Estas imágenes son procesadas por un sistema de inteligencia artificial (AI) implementado en el robot. La AI analiza la imagen en busca de características específicas que coincidan con el objeto objetivo, en este caso, el objeto Wally.

Cuando Wally detecta un objeto en la imagen capturada por la cámara, ajusta automáticamente la trayectoria de la cámara para que el objeto quede centrado en la imagen. Este ajuste de trayectoria facilita la determinación precisa de la orientación del objeto y su categoría mediante el sistema de AI implementado en el robot. Además, un sensor ubicado junto a la garra de Wally mide la distancia al objeto detectado.

Con la información obtenida de la imagen y la distancia al objeto, Wally interpreta los datos para determinar el punto en el espacio donde se encuentra el objeto y la orientación que debe tener su garra para agarrarlo correctamente. Utilizando esta información, el robot se desplaza hacia el objeto y realiza una acción para agarrarlo con éxito.

Una vez que Wally ha logrado agarrar el objeto objetivo, se dirige al contenedor correspondiente que se encuentra dentro del alcance de su garra y deposita el objeto allí. Este contenedor está diseñado específicamente para la categoría a la que pertenece el objeto recogido.

Después de depositar el objeto en el contenedor, Wally regresa a su posición inicial "home" para prepararse y continuar con la exploración en busca de más objetos. Si Wally no encuentra más objetos dentro del alcance de su garra y cámara, se moverá a otro lugar completo para realizar otra exploración y buscar nuevos objetos.

En resumen, el desarrollo del sistema de selección de un objeto Wally involucra la exploración autónoma del terreno, el reconocimiento y ajuste de trayectoria del objeto objetivo, el cálculo de la posición y orientación para agarrarlo, el depósito en el contenedor correspondiente y la capacidad de moverse a diferentes ubicaciones para seguir explorando en busca de más objetos. Estas funcionalidades se apoyan en el uso de una cámara, un sistema de AI, un sensor de distancia y una trayectoria definida para lograr el objetivo final de seleccionar y recolectar los objetos Wally de manera eficiente y precisa.
