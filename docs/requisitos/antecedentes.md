# Registro de antecedentes y alergias

## Historia relacionada
**HU06:** como médico, registrar los antecedentes y las alergias del paciente para considerar esta información durante futuras atenciones.

Los criterios siguientes constituyen una especificación propuesta para el desarrollo del módulo.

## Comportamiento esperado
Los antecedentes y las alergias deben estar asociados al paciente seleccionado y disponibles para los profesionales autorizados que consulten su historia. Se propone registrar la fecha de actualización y el usuario responsable.

## Criterios de aceptación
1. Un médico autorizado puede registrar antecedentes y alergias en la historia del paciente seleccionado.
2. El formulario identifica claramente al paciente antes de guardar.
3. Después del guardado, la información puede recuperarse desde la misma historia clínica.
4. Actualizar esta información no modifica los antecedentes ni las alergias de otros pacientes.
5. El sistema permite distinguir entre información aún no registrada y una declaración explícita de ausencia de alergias conocidas.
6. Si falta información obligatoria acordada, se indica qué debe completarse antes de guardar.
7. Si falla el almacenamiento, se informa que la actualización no pudo completarse.
8. Una cuenta sin permiso no puede modificar esta información.

## Comprobación manual
Registrar antecedentes y una alergia ficticia en un paciente de prueba. Volver a consultar la historia, comprobar la persistencia y confirmar que otro paciente mantiene sus propios datos. Verificar también el estado sin información y la restricción por rol.
