## ComparsistaScript

Nombre completamente simbólico, sin ninguna relación real con el objetivo y funcionalidad del proyecto, debido a que la idea original surge cuando el autor, osease yo, quiere poder descargar de YouTube todos los pasodobles de sus comparsas favoritas, ya divididos directamente, sin tener que perder tiempo en páginas web de terceros.

### Aviso

Si alguien quiere cogerlo y mejorarlo, arreglar fallos, o en definitiva, dedicarle más tiempo del que yo estoy dispuesto, que lo copie y ya.

### Requisitos

1.  Tener Windows, porque se usa un **.exe**
2.  Instalar **python** (3)
3.  Instalar **pip**
4.  Ejecutar **python -m pip install pytube==6.4.2** en la consola para instalar **pytube**

### Descripción

Proyecto realizado en Python por alguien nada versado en absoluto sobre Python, con la intención de generar una herramienta de uso simple y directo para descargar discos completos a partir de vídeos de YouTube.

### Funcionalidad

Tras introducir el ID del vídeo a descargar, se piden al usuario las distintas marcas de tiempo en las cuales dividir el vídeo, pudiendo así obtener cada parte por separado, a las cuales se les extraerá el audio para generar todas las canciones por separado.

### Créditos

El script utiliza la herramienta FFmpeg, una colección de software libre para la manipulación de streaming, audio y vídeo creada por Fabrice Bellard.

Más información acerca de FFmpeg: <https://es.wikipedia.org/wiki/FFmpeg>
Web oficial del proyecto: <http://ffmpeg.org/>

### Errores conocidos y cosas a tener en cuenta al usar el script u otras cosas que probablemente no me importen

1.  No hay control de excepciones (aunque no te deberían dar si sigues las instrucciones)
