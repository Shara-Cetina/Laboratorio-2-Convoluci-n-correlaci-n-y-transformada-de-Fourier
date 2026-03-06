# Laboratorio No.2 "Convolución, correlación y transformada de Fourier"
## Shara Cetina y Juanita Gómez

## Descripción
Este proyecto contiene el código y la información para comprender la convolución y correlación de señales, además de analizar y caracterizar señales biomédicas con ayuda de la transformada de Fourier.

## Propósito 
<p align="justify">
El propósito de este laboratorio es lograr que el estudiante adquiera las capacidades necesarias para aplicar la convolución, la correlación y la Transformada de Fourier en el procesamiento de señales digitales. Se busca que se comprenda la convolución como una herramienta de filtrado lineal y respuesta de sistemas, y la correlación como una medida de similitud estadística. A través de la digitalización bajo el criterio de Nyquist y el análisis espectral de señales biológicas, se pretende que el estudiante evalúe el impacto de estos procedimientos en la detección de patologías y en la mejora de la calidad de la señal, fundamentales para el mundo laboral de un ingeniero biomédico.

## Metodología 
<p align="justify">
La práctica de laboratorio No.2 consiste en la realización de la convolución, correlación y transformada de Fourier de diferentes tipos de señales. Para la convolución se tomó el código y el número de identificación de cada estudiante que conforma el grupo, en este caso dos personas; se realizó a mano y se programó en python con ayuda de la función "conv_result", por parte de la correlación se realizó utilizando una señal seno y coseno, las cuales se programaron con "np.correlate", por último para la transformada de Fourier fue necesario adquirir una señal EOG (electrooculograma) con ayuda de un generador de señales, a la cual se le cáculo su respectiva frencuencia de Nyquist, por medio de la fórmula FN = 2fmáx, por consiguiente se adquirió la señal por medio de un DAQ, esta se programó con una frecuencia de muestreo de 1000 Hz. La transformada de Fourier y densidad espectral de potencia se obtuvieron por medio de la libería " scipy import fft", en ambos cálculos se realizó su caracterización estadística con su respectivo histograma.

## Diagrama de flujo 

### Parte A

<img width="1024" height="768" alt="1" src="https://github.com/user-attachments/assets/aa6b6fb8-0ef2-4ee1-a2b8-31e82d8671c1" />


### Parte B

<img width="1024" height="768" alt="2" src="https://github.com/user-attachments/assets/ab1e597b-e2b3-4dba-9c31-40604c689136" />

**¿En qué situaciones resulta útil aplicar la correlación cruzada en el procesamiento digital de señales?**
<p align="justify">
La correlación cruzada es una herramienta util en el procesamiento digital de señales, ya que permite medir la similitud entre dos señales en función de su desfase. Además, se utiliza para encontrar una señal especifica dentro de otra de mayor tamaño, así como para calcular o estimar el retraso temporal de una señal respecto a otra. Tambien facilita la determinacion de las características de un sistema desconocido al comparar la señal de entrada con la señal de salida.


### Parte C

<img width="1024" height="768" alt="3" src="https://github.com/user-attachments/assets/863fddcc-3d6e-40f9-8173-862ea0f89ed9" />
<img width="1024" height="768" alt="4" src="https://github.com/user-attachments/assets/f144d27f-1b10-439f-9899-811cc3e4d650" />
<img width="1024" height="768" alt="5" src="https://github.com/user-attachments/assets/c5350d2a-6bee-41de-8e28-2d0f225576db" />

## Calculos manuales

### Datos Shara 

<img width="887" height="591" alt="Shara1" src="https://github.com/user-attachments/assets/7d867ac9-fd03-438f-9e29-7e39b9846d5d" />
<img width="792" height="582" alt="Shara2" src="https://github.com/user-attachments/assets/ab90f52c-3dfe-442e-b02b-e76cedf99b29" />

### Datos Juanita

<img width="477" height="612" alt="Juanita1" src="https://github.com/user-attachments/assets/7b1583f8-a725-4a4b-8550-b2b762df42a7" />
<img width="443" height="612" alt="Juanita2" src="https://github.com/user-attachments/assets/68effbfd-8dc9-4fa3-b2a6-0ece5851032e" />

## Análisis Estadístico

<img width="791" height="463" alt="Convolución 1" src="https://github.com/user-attachments/assets/9e8c4e9c-dd33-4b5d-a249-6a40a4c56514" />
<img width="792" height="476" alt="Convolucion 2" src="https://github.com/user-attachments/assets/db229acb-70c6-4364-9ed0-517f8c10078b" />

<p align="justify">

  
En las convulciones se puede observar como la señal de entrada x[n] y la respuesta al impulso h[n] muestran como se acumula y redistribuye la energía de la señal, generando una salida con mayor duración y picos de amplitud más grandes, debido a que el sistema actúa como un proceso de integración discreta, donde la energía se concentra en ciertos instantes.
  
<img width="790" height="507" alt="Captura de pantalla 2026-03-05 164832" src="https://github.com/user-attachments/assets/cd7076c9-62fb-4c30-a56c-66b6e47c1eb3" />


<p align="justify"> 
La correlación cruzada evidencia el grado de similitud entre dos señales en distintos periodos de tiempo, en este caso se puede observar un máximo de correlación cuando m se vuelve cercano a -2, indicando de esta manera que las señales presentan mayor similitud cuando una de estas se adelanta aproximadamente dos muestras, a su vez, el signo negativo evidencia una diferencia de fase, lo cual tiene demasiado sentido ya que se está trabajando con seno y con coseno.




<img width="791" height="308" alt="EOG" src="https://github.com/user-attachments/assets/7a496598-02c8-44a7-8a1e-c8248ede5f48" />
<img width="716" height="510" alt="H1" src="https://github.com/user-attachments/assets/24f531ef-ebb8-4597-8716-1c9032e86406" />
<img width="790" height="347" alt="TR" src="https://github.com/user-attachments/assets/eef326cc-71b2-489d-b46f-a561fa3d484b" />
<img width="728" height="512" alt="H2" src="https://github.com/user-attachments/assets/de3df279-463a-499c-a996-943f9f2ec0f9" />


<p align="justify">  
Por medio de la transformada de Fourier, la densidad espectral de potencia y los histogramas asociados a estas permiten observar que la mayor cantidad de energía se encuentra en bajas frecuencias decreciendo progresivamente hacia altas, lo cual es un comportamiento característico de las señales biomédicas, ya que todo proceso fisiológico normalmente ocurre de manera lenta y continua, evitando todo movimiento brusco, mayormente en la señal EOG, debido a que los movimientos mecánicos del ojo son procesos relativamente pausados en comparación con la actividad eléctrica de un nervio o músculo, manejando una frecuencia aproximadamente de 30Hz. 

## Análisis de Resultados:
<p align="justify">
Las herramientas matemáticas como la convolución y la correlación son fundamentales en el análisis de señales biomédicas, ya que permiten reducir el ruido mediante filtros digitales, medir la similitud entre dos señales, estimar el desfase o el retraso temporal ellas, modelar la forma en que un sistema fisiologico responde a un estimulo e identificar patrones o eventos especificos como las ondas de un ECG o la actividad registrada un EMG. Sin embargo, estas herramientas presentan ciertas limitaciones, una de ellas es la suposicion de que el sistema es lineal e invariante en el tiempo, condicion que no se cumplen en todos los sistemas biologicos. Además, las señales biomedicas suelemn contener ruido que puede afectar el proceso de filtrado. Por ultimo, la longitud de la señal puede ser un fcator considerable, lo que requiere métodos de procesamiento mas eficientes y, a su vez, una mayor capcidad computacional.
<p align="justify">
Por otro lado, la transformada de Fourier es una herramienta fundamental para convertir señales del dominio del tiempo al dominio de la frecuencia en tiempo real. Esto permite identificar las frecuencias presentes en una señal, implementar filtrados para frecuencias especificas durante la adquisición de la señal y analizar cambios en su espectro. Además, al utilizar su variante rapida, conocida como FFT, es posible reducir significativamente el tiempo de cálculo, esto facilita su aplicacion en sistemas que requieren una respuesta rapida. Sin embargo, tambien presenta algunas limitaciones. Por ejemplo, pueden generarse retrasos en el procesamiento debido a la necesidad de utilizar ventanas de tiempo largas para obtener una mayor precisión en frecuencia. Asimismo, esta tecnica asume que la señal es invariable dentro del intervalo realizado, lo cual no siempre ocurre en señales reales, ya que muchas de ellas cambian con el tiempo.

## Conclusión 

<p align="justify">
En conclusión, el uso de herramientas matemáticas como la convolución, la correlación, la transformada de Fourier y la densidad espectral de potencia es fundamental en el análisis de señales biomédicas y en la formación de un Ingeniero Biomédico. Estas técnicas permiten estudiar las señales tanto en el dominio del tiempo como en el dominio de la frecuencia, facilitando la extracción de información relevante que no es posible identificar únicamente mediante la observación directa de la señal original. A través de la convolución, es posible analizar la respuesta de sistemas y comprender cómo se modifica una señal al pasar por diferentes procesos o filtros, mediante la correlación, se pueden identificar similitudes entre señales o detectar patrones característicos asociados a eventos fisiológicos. La transformada de Fourier y la densidad espectral de potencia permiten analizar la distribución de la energía de la señal en función de la frecuencia, lo que facilita identificar componentes fisiológicas relevantes y diferenciar entre información útil y ruido. En conjunto, estas herramientas permiten mejorar la calidad de las señales biomédicas, optimizar su procesamiento y contribuir a una detección más precisa de posibles patologías, ya que hacen posible revelar patrones, variaciones o anomalías que no serían evidentes en la señal original. 

## Discusión


**¿Qué utilidad poseen herramientas como la convolución y la correlación en áreas como procesamiento de imágenes?**
<p align="justify">
Las herramientas como la convolución y la correlación se utilizan en el procesamiento de imagenes para aplicar filtros especiales que peemiten suavizar la imagen o resaltar ciertas caracterisiticas, como la detección de bordes y el aumento de nitidez. Además, estas técnicas permiten medir las similitudes entre dos imagenes o entre una imagen y una plantilla, alinear imagenes tomadas en diferentes momentos e identificar desplazamientos entre cuadros consecutivos de una secuencia de imagenes.

**¿En cuáles contextos de aplicación la transformada de Fourier ofrece un conjunto de características con mayor poder discriminativo que las que suelen considerarse desde el dominio temporal?** 

<p align="justify">
La transformada de Fourier ofrece mayor poder discriminativo que el análisis en el dominio temporal cuando la información relevante de la señal está asociada a su contenido en frecuencia. Esto ocurre especialmente en el análisis de señales biomédicas como EEG, ECG, EMG o EOG, donde diferentes estados fisiológicos o patologías producen cambios en determinadas bandas de frecuencia, mientras que en el dominio temporal estas diferencias son muy poco evidentes.

**¿En qué se diferencia la correlación cruzada de la convolución?**
<p align="justify">
La correlación cruzada consiste en desplazar una señal directamente sobre otra para poder medir el grado de similitud en cada posición y determinar el desfase temporal donde coinciden mejor. Además, su resultado indica que tan parecidas son las señales segun el desplazamiento aplicado. Por otro lado, la convolución invierte una de las señales antes de realizar la operación de multiplicacion y suma con la otra señal, para despues desplazarla. El resultado de la convolución representa la respuesta del sistema cuando una señal lo atraviesa.
