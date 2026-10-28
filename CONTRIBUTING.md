# Guía de colaboración en el proyecto

## Gestión de ramas

La rama `main` se mantiene estable y no se utiliza para desarrollar directamente. Cada tarea debe comenzar creando una rama propia a partir de `main` mediante el comando `git switch -c nombre-de-la-rama`.

La rama `mejora-readme` está destinada a realizar modificaciones y mejoras en la documentación del proyecto, como actualizar el README.md o corregir su contenido.

## Normas para los commits

Los mensajes de commit deben tener el formato `tipo: descripción`. Se utilizarán los siguientes tipos según el cambio realizado:

- `feat`: añadir una nueva característica.
- `fix`: solucionar un fallo del programa.
- `docs`: actualizar archivos de documentación.
- `style`: realizar cambios de formato o estilo.
- `refactor`: mejorar la estructura del código sin alterar su comportamiento.
- `test`: incorporar o modificar pruebas.
- `chore`: realizar tareas auxiliares de mantenimiento.

## Procedimiento para colaborar

1. Cambia a la rama `main` y descarga las últimas actualizaciones.
2. Crea una rama independiente para tu tarea.
3. Desarrolla los cambios y registra cada avance con un commit.
4. Envía tu rama al repositorio remoto:

   `git push -u origin nombre-de-la-rama`

5. Abre una Pull Request en GitHub y explica las modificaciones realizadas.
6. Espera a que se revise la propuesta antes de integrar los cambios en `main`.

## Descargar y ejecutar el proyecto

Para trabajar con el repositorio en tu equipo, ejecuta los siguientes comandos:

```bash
git clone git@github.com:antonio12345678901234567890/ut2-git-python.git
cd ut2-git-python
python3 ej01_par_impar.py