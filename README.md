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
Parte A
<img width="1024" height="768" alt="1" src="https://github.com/user-attachments/assets/aa6b6fb8-0ef2-4ee1-a2b8-31e82d8671c1" />


Parte B
<img width="1024" height="768" alt="2" src="https://github.com/user-attachments/assets/ab1e597b-e2b3-4dba-9c31-40604c689136" />

**¿En qué situaciones resulta útil aplicar la correlación cruzada en el procesamiento digital de señales?**
La correlación cruzada es una herramienta util en el procesamiento digital de señales, ya que permite medir la similitud entre dos señales en función de su desfase. Además, se utiliza para encontrar una señal especifica dentro de otra de mayor tamaño, así como para calcular o estimar el retraso temporal de una señal respecto a otra. Tambien facilita la determinacion de las características de un sistema desconocido al comparar la señal de entrada con la señal de salida.


Parte C
<img width="1024" height="768" alt="3" src="https://github.com/user-attachments/assets/863fddcc-3d6e-40f9-8173-862ea0f89ed9" />
<img width="1024" height="768" alt="4" src="https://github.com/user-attachments/assets/f144d27f-1b10-439f-9899-811cc3e4d650" />
<img width="1024" height="768" alt="5" src="https://github.com/user-attachments/assets/c5350d2a-6bee-41de-8e28-2d0f225576db" />

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

## Análisis de Resultados: (SHARA)

### Alcance y posibles limitaciones de herramientas matemáticas como la convolución y la correlación en el análisis de señales biomédicas.

### Alcance y posibles limitaciones de emplear la transformada de Fourier para aplicaciones en tiempo real.

## Conclusión 

<p align="justify">
En conclusión, el uso de herramientas matemáticas como la convolución, la correlación, la transformada de Fourier y la densidad espectral de potencia es fundamental en el análisis de señales biomédicas y en la formación de un Ingeniero Biomédico. Estas técnicas permiten estudiar las señales tanto en el dominio del tiempo como en el dominio de la frecuencia, facilitando la extracción de información relevante que no es posible identificar únicamente mediante la observación directa de la señal original. A través de la convolución, es posible analizar la respuesta de sistemas y comprender cómo se modifica una señal al pasar por diferentes procesos o filtros, mediante la correlación, se pueden identificar similitudes entre señales o detectar patrones característicos asociados a eventos fisiológicos. La transformada de Fourier y la densidad espectral de potencia permiten analizar la distribución de la energía de la señal en función de la frecuencia, lo que facilita identificar componentes fisiológicas relevantes y diferenciar entre información útil y ruido. En conjunto, estas herramientas permiten mejorar la calidad de las señales biomédicas, optimizar su procesamiento y contribuir a una detección más precisa de posibles patologías, ya que hacen posible revelar patrones, variaciones o anomalías que no serían evidentes en la señal original. 

## Discusión


**¿Qué utilidad poseen herramientas como la convolución y la correlación en áreas como procesamiento de imágenes?** (SHARA)

**¿En cuáles contextos de aplicación la transformada de Fourier ofrece un conjunto de características con mayor poder discriminativo que las que suelen considerarse desde el dominio temporal?** 

<p align="justify">
La transformada de Fourier ofrece mayor poder discriminativo que el análisis en el dominio temporal cuando la información relevante de la señal está asociada a su contenido en frecuencia. Esto ocurre especialmente en el análisis de señales biomédicas como EEG, ECG, EMG o EOG, donde diferentes estados fisiológicos o patologías producen cambios en determinadas bandas de frecuencia, mientras que en el dominio temporal estas diferencias son muy poco evidentes.

**¿En qué se diferencia la correlación cruzada de la convolución?** (SHARA)
