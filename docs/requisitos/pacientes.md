# Registro y búsqueda de pacientes

## Historias relacionadas
- **HU01:** como recepcionista, registrar los datos personales de un paciente.
- **HU08:** como personal autorizado, buscar pacientes por nombre, DNI o código de historia clínica.

Este documento propone los criterios de aceptación para desarrollar y revisar el módulo. Su incorporación no implica que la funcionalidad esté implementada.

## Registro de pacientes
La recepción debe poder crear un paciente y consultar los datos personales permitidos para su rol. Se propone registrar nombres, apellidos y DNI como datos obligatorios, y teléfono y correo como datos de contacto opcionales.

### Criterios de aceptación de HU01
1. Un usuario autorizado puede guardar un paciente con los datos obligatorios completos.
2. Si falta un campo obligatorio, el sistema indica cuál es y no guarda un registro incompleto.
3. El sistema rechaza un DNI que ya pertenece a otro paciente.
4. Cada paciente recibe un código único de historia clínica.
5. Después de guardar, se muestra la confirmación y el paciente puede recuperarse mediante la búsqueda.
6. Si falla el guardado, se informa el error sin mostrar una confirmación de éxito.

## Búsqueda de pacientes

### Criterios de aceptación de HU08
1. Un usuario autorizado puede buscar por nombre, DNI o código de historia clínica.
2. La búsqueda por nombre admite coincidencias parciales e ignora diferencias entre mayúsculas y minúsculas.
3. La búsqueda por DNI o código identifica al paciente por el valor completo.
4. Si aparecen homónimos, se muestran los identificadores permitidos para distinguirlos.
5. Si no hay coincidencias, se informa que no se encontraron pacientes.
6. Seleccionar un paciente no amplía los permisos del usuario sobre su información clínica.

## Comprobación manual
Crear dos pacientes ficticios con nombres similares y DNI distintos. Buscar por cada criterio, comprobar que ambos pueden distinguirse e intentar registrar nuevamente uno de los DNI. Registrar el resultado obtenido y el esperado en la evidencia de prueba.
