# pagina_msx
Aplicación web que nos ayuda a controlar nuestra colección de juegos de nuestro ordenador: MSX

Queremos hacer una aplicación web que nos ayude a controlar nuestra colección de juegos de nuestro ordenador preferido: el MSX.

Vamos a crear una aplicación con las siguientes características:

# La aplicación debe tener una hoja de estilo. Para ello lo mejor es que busques una plantilla HTML/CSS: con lo que ya tienes la hoja de estilo y ...
# Las plantillas que uses en la aplicación se heredarán de la plantilla base.html (esta plantilla la puedes crear a partir de la plantilla HTML que has buscado).
# La plantilla base tendrá al menos dos bloques: uno para indicar el título y otro para poner el contenido.
# La página principal tendrá una imagen con el logotipo MSX al pulsar sobre está imagen  nos llevará a a página /juegos.
# La página /juegos nos mostrara un buscador, para ello pon un formulario con un cuadro de texto donde puedas poner el nombre de un juego que quieres buscar. Cuando pulséis el botón de buscar enviará la información a la página /listajuegos. El formulario enviará los datos con el método POST.
# En la página /listajuegos (qué sólo se puede acceder por el método POST) aparecerán los juegos cuyo nombre empiezan por la cadena que hemos añadido al formulario. Si no hemos indicado ninguna cadena mostrará todos los juegos.