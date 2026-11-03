# Registro y consulta de citas médicas

## Historia relacionada
**HU07:** como recepcionista, registrar y consultar las citas médicas para organizar las atenciones de los pacientes.

Este documento propone criterios de aceptación para el módulo de citas.

## Datos de una cita
Se propone vincular cada cita con un paciente registrado, un profesional, una fecha y un horario. Las reglas de duración y disponibilidad se acordarán antes de implementar la agenda.

## Criterios de aceptación
1. Un recepcionista autorizado puede registrar una cita para un paciente existente.
2. El sistema solicita el paciente, el profesional, la fecha y el horario antes de guardar.
3. La disponibilidad del profesional se comprueba según las reglas de agenda acordadas.
4. Si el horario no está disponible, el sistema rechaza el registro e informa el motivo.
5. Después del guardado, la cita puede encontrarse en la consulta de agenda.
6. La consulta permite identificar al paciente y al profesional de cada cita.
7. Si no hay citas para el criterio seleccionado, se informa que no existen registros.
8. Si ocurre un error al guardar, no se presenta la cita como confirmada.
9. Una cuenta sin permisos no puede crear citas ni consultar información restringida de la agenda.

## Comprobación manual
Crear citas ficticias para dos pacientes y profesionales de prueba. Consultar la agenda y comprobar que los datos corresponden a cada cita. Intentar reservar un horario ocupado según las reglas acordadas y verificar el rechazo sin duplicar la reserva.
