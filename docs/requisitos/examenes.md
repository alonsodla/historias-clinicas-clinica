# Consulta de resultados de análisis y exámenes

## Historia relacionada
**HU05:** como médico, visualizar los resultados de análisis y exámenes de un paciente para complementar su evaluación.

Este documento define criterios propuestos para desarrollar la consulta de resultados. No incorpora archivos clínicos ni resultados reales.

## Datos de referencia propuestos
Cada resultado se asociará con un paciente e incluirá una identificación del análisis o examen y su fecha. El formato de presentación del resultado se elegirá al implementar el módulo.

## Criterios de aceptación
1. Un médico autorizado puede consultar los resultados asociados al paciente seleccionado.
2. Cada resultado identifica al paciente, el tipo de examen y la fecha.
3. Los resultados se presentan en un orden definido, con los más recientes primero.
4. Si no existen resultados, el sistema muestra un mensaje que lo indique.
5. Si un resultado no está disponible, se informa su estado sin presentar datos incompletos como un resultado válido.
6. Seleccionar un resultado de un paciente no permite acceder a resultados de otro paciente sin la autorización correspondiente.
7. Una cuenta sin permisos no puede recuperar los resultados mediante la interfaz ni mediante una solicitud directa.

## Comprobación manual
Utilizar resultados ficticios de dos pacientes. Comprobar la identificación, el orden de fechas, el caso sin resultados y el rechazo de acceso desde una cuenta sin permisos. Verificar que cada resultado se vincula con el paciente correcto.
