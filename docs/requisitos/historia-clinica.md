# Historia clínica y registro de consultas

## Historias relacionadas
- **HU03:** como médico, consultar la historia clínica de un paciente para conocer sus antecedentes y atenciones anteriores.
- **HU04:** como médico, registrar los datos de cada consulta para mantener actualizado el historial clínico.

Los siguientes criterios describen el comportamiento propuesto del módulo y servirán para revisar su implementación.

## Consulta de la historia clínica

### Criterios de aceptación de HU03
1. Un médico autorizado puede abrir la historia del paciente seleccionado.
2. La vista identifica al paciente mediante su nombre y código de historia clínica.
3. Las atenciones anteriores se presentan con sus fechas y el profesional que las registró.
4. Si el paciente no tiene consultas registradas, el sistema informa que el historial de atenciones está vacío.
5. Los datos mostrados pertenecen únicamente al paciente seleccionado.
6. Una cuenta sin permiso no puede consultar la información clínica.

## Registro de una consulta
Se propone asociar cada atención con el paciente, la fecha, el profesional y los datos de la consulta que se definan en el formulario del proyecto.

### Criterios de aceptación de HU04
1. Un médico autorizado puede añadir una consulta al paciente seleccionado.
2. El sistema valida los campos obligatorios acordados antes de guardar.
3. La nueva consulta conserva la referencia al paciente y al profesional que la registró.
4. Al guardar, la atención aparece en el historial sin eliminar las consultas anteriores.
5. Si ocurre un error de almacenamiento, se informa que la consulta no pudo registrarse.

## Comprobación manual
Preparar dos pacientes ficticios con historiales distintos. Registrar una nueva consulta en uno de ellos, verificar su aparición y comprobar que el historial del otro paciente permanece sin cambios.
