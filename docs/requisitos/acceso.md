# Acceso al sistema y permisos por rol

## Historia relacionada
**HU02:** como personal de la clínica, iniciar sesión con una cuenta y permisos según el rol para acceder únicamente a la información autorizada.

Este documento propone criterios de aceptación para la implementación. No acredita que el inicio de sesión ya esté disponible.

## Comportamiento esperado
El sistema debe verificar las credenciales y aplicar los permisos de la cuenta a cada operación. Ocultar una opción de la interfaz no reemplaza la comprobación del permiso al ejecutar la acción.

## Permisos iniciales propuestos
| Perfil | Operaciones del proyecto |
| --- | --- |
| Recepción | Registrar pacientes, consultar datos de identificación, buscar pacientes y gestionar las citas autorizadas. |
| Médico | Buscar pacientes y acceder a las historias clínicas, consultas, resultados, antecedentes y alergias autorizados. |

Los nombres definitivos de roles y el alcance de acceso a cada paciente se acordarán con el equipo antes de implementar la autorización.

## Criterios de aceptación
1. Una cuenta activa con credenciales correctas puede iniciar sesión.
2. Las credenciales incorrectas se rechazan sin conceder acceso al sistema.
3. El usuario recibe únicamente las opciones y operaciones permitidas para su rol.
4. Una operación solicitada directamente también se rechaza si la cuenta no tiene permiso.
5. El usuario puede cerrar su sesión y las operaciones protegidas dejan de estar disponibles.
6. Los mensajes de error de acceso no incluyen contraseñas ni información clínica.

## Comprobación manual
Usar cuentas de prueba para recepción y medicina. Verificar el inicio y cierre de sesión, un intento con contraseña incorrecta y una operación fuera de los permisos de cada perfil. Conservar solo datos ficticios en las evidencias.
