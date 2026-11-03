# Sistema de gestión de historias clínicas

Proyecto grupal del curso **Ingeniería de Software CIB02**, de la Facultad de Ingeniería Eléctrica y Electrónica de la Universidad Nacional de Ingeniería.

## Objetivo

Desarrollar un sistema para organizar la información de los pacientes de una clínica y permitir al personal autorizado registrar y consultar datos personales, historias clínicas, consultas, resultados de análisis y citas.

## Estado inicial

El repositorio contiene la documentación y las reglas de exclusión iniciales. El código de la aplicación y sus pruebas se incorporarán mediante ramas de trabajo.

## Historias de usuario

La numeración conserva el orden de prioridad de la propuesta del proyecto.

| Historia | Usuario | Funcionalidad |
| --- | --- | --- |
| HU01 | Recepcionista | Registrar los datos personales de un paciente. |
| HU02 | Personal de la clínica | Iniciar sesión con una cuenta y acceder según los permisos de su rol. |
| HU03 | Médico | Consultar la historia clínica, los antecedentes y las atenciones anteriores de un paciente. |
| HU04 | Médico | Registrar los datos de cada consulta médica. |
| HU05 | Médico | Visualizar los resultados de análisis y exámenes de un paciente. |
| HU06 | Médico | Registrar los antecedentes y las alergias del paciente. |
| HU07 | Recepcionista | Registrar y consultar las citas médicas. |
| HU08 | Personal autorizado | Buscar pacientes por nombre, DNI o código de historia clínica. |

## Flujo de ramas acordado

El equipo utilizará **GitHub Flow**. La única rama permanente será `main`; cada tarea se desarrollará en una rama corta creada desde la versión actualizada de `main`.

| Rama | Finalidad | Rama de destino |
| --- | --- | --- |
| `main` | Versión integrada y comprobada del proyecto. | No aplica. |
| `feature/huNN-descripcion` | Desarrollar una funcionalidad o una parte de una historia de usuario. | `main` |
| `bugfix/descripcion` | Corregir un defecto del sistema. | `main` |
| `docs/descripcion` | Actualizar la documentación del proyecto. | `main` |

Ejemplos: `feature/hu01-registro-pacientes`, `feature/hu02-inicio-sesion` y `docs/manual-instalacion`.

### Secuencia de trabajo

1. Actualizar la copia local de `main` antes de comenzar una tarea.
2. Crear una rama con un nombre que identifique la tarea o historia de usuario.
3. Implementar y comprobar cambios pequeños y coherentes.
4. Registrar cada cambio mediante un commit atómico con un mensaje descriptivo.
5. Publicar la rama y abrir un **pull request** hacia `main`.
6. Solicitar la revisión de otro integrante del grupo.
7. Resolver los comentarios y los conflictos, y comprobar la compilación y las pruebas aplicables.
8. Obtener al menos una aprobación de un integrante que no sea autor de los cambios.
9. Integrar el pull request mediante **Create a merge commit**, para conservar los commits originales y sus autores.
10. Eliminar la rama temporal después de fusionarla y actualizar las copias locales.

La publicación inicial de la documentación y del archivo de exclusiones sirve para inicializar el repositorio. Los cambios posteriores en `main` se integrarán mediante pull requests. Las reglas anteriores son el acuerdo de colaboración; la protección automática de la rama se configura por separado en GitHub.

### Actualización de una rama de trabajo

Antes de solicitar la revisión, incorporar los cambios recientes de `main` a la rama de trabajo y volver a comprobar el resultado. Si aparece un conflicto, resolverlo antes de integrar.

En ramas compartidas se utilizará `merge` para incorporar cambios, conservando el historial publicado. El equipo evitará reescribir los commits de otros integrantes.

## Ejemplo de trabajo con Git

Comandos para Git Bash:

```bash
git clone https://github.com/alonsodla/historias-clinicas-clinica.git
cd historias-clinicas-clinica
git switch main
git pull --ff-only origin main
git switch -c feature/hu01-registro-pacientes
```

Después de implementar y comprobar un cambio sobre archivos existentes:

```bash
git status
git diff
git add -p
git diff --cached
git commit -m "feat(pacientes): valida DNI y campos obligatorios"
git push -u origin feature/hu01-registro-pacientes
```

Para archivos nuevos, utilizar `git add ruta/al/archivo`, sustituyendo la ruta por la del archivo correspondiente. Después se abrirá el pull request hacia `main`.

Para actualizar una rama con cambios recientes de la principal:

```bash
git fetch origin
git merge origin/main
# Resolver conflictos si los hubiera y ejecutar las pruebas.
git push
```

Una vez fusionado el pull request:

```bash
git switch main
git pull --ff-only origin main
git fetch --prune
git branch -d feature/hu01-registro-pacientes
```

## Convención de commits

Formato:

```text
tipo(modulo): accion concreta
```

| Tipo | Uso | Ejemplo |
| --- | --- | --- |
| `feat` | Nueva funcionalidad. | `feat(pacientes): agrega búsqueda por DNI` |
| `fix` | Corrección de un defecto. | `fix(pacientes): rechaza DNI duplicados` |
| `test` | Incorporación o ajuste de pruebas. | `test(pacientes): verifica registros duplicados` |
| `docs` | Cambios en documentación. | `docs(readme): documenta el flujo de ramas` |
| `chore` | Configuración y mantenimiento. | `chore(repo): agrega reglas de exclusión` |

Un commit debe representar un cambio coherente que pueda revisarse y revertirse de forma independiente. Cada integrante confirmará sus cambios con su propia identidad y un correo asociado a su cuenta de GitHub.

## Criterios para integrar un pull request

- El cambio cumple la tarea o historia de usuario indicada en su descripción.
- La aplicación compila o inicia, cuando corresponda.
- Las pruebas del cambio y de los módulos afectados finalizan correctamente.
- Se han resuelto los conflictos y los comentarios de revisión.
- Otro integrante ha revisado y aprobado la versión final del cambio.

Si se modifica el código después de recibir una aprobación, se solicitará una nueva revisión.

## Organización prevista

Las siguientes carpetas se incorporarán cuando contengan archivos:

- `src/`: código fuente.
- `tests/`: pruebas y datos ficticios.
- `docs/`: documentación técnica y de uso.
- `database/migrations/`: scripts versionados de base de datos.

## Archivos excluidos

El archivo `.gitignore` excluye resultados de compilación, configuración personal del editor, variables de entorno, registros temporales, bases de datos locales y archivos cargados por usuarios.

Se versionarán el código fuente, las pruebas, la documentación y los scripts de base de datos. La plantilla `.env.example`, si se incorpora, contendrá nombres de variables y ejemplos sin credenciales. Los datos de prueba serán ficticios; los archivos clínicos reales se mantendrán fuera del repositorio.

## Instalación y pruebas

Los requisitos del entorno y los comandos de compilación, inicio y pruebas se documentarán cuando el equipo elija la tecnología e incorpore el primer módulo ejecutable.
