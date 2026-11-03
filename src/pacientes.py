"""Registro inicial de pacientes con persistencia en SQLite."""

from __future__ import annotations

import argparse
import json
import re
import sqlite3
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Sequence


@dataclass(frozen=True)
class Paciente:
    id: int
    codigo_historia: str
    dni: str
    nombres: str
    apellidos: str
    telefono: str = ""
    correo: str = ""


def _dni_valido(dni: str) -> str:
    if not isinstance(dni, str):
        raise ValueError("El DNI debe ingresarse como texto de ocho dígitos.")
    dni = dni.strip()
    if re.fullmatch(r"[0-9]{8}", dni) is None:
        raise ValueError("El DNI debe tener exactamente ocho dígitos.")
    return dni


def _texto(valor: str, campo: str, obligatorio: bool = False) -> str:
    if not isinstance(valor, str):
        raise ValueError(f"El campo {campo} debe ser texto.")
    valor = valor.strip()
    if obligatorio and not valor:
        raise ValueError(f"El campo {campo} es obligatorio.")
    return valor


class RegistroPacientes:
    """Almacena pacientes; el control de acceso se integrará en HU02."""

    def __init__(self, base_datos: str | Path = "data/local/clinica.sqlite3"):
        ruta = str(base_datos)
        if ruta != ":memory:":
            Path(ruta).parent.mkdir(parents=True, exist_ok=True)
        self._conexion = sqlite3.connect(ruta)
        self._conexion.row_factory = sqlite3.Row
        try:
            with self._conexion:
                self._conexion.execute(
                    """
                    CREATE TABLE IF NOT EXISTS pacientes (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        dni TEXT NOT NULL UNIQUE
                            CHECK(length(dni) = 8 AND dni NOT GLOB '*[^0-9]*'),
                        nombres TEXT NOT NULL CHECK(trim(nombres) <> ''),
                        apellidos TEXT NOT NULL CHECK(trim(apellidos) <> ''),
                        telefono TEXT NOT NULL DEFAULT '',
                        correo TEXT NOT NULL DEFAULT ''
                    )
                    """
                )
        except Exception:
            self._conexion.close()
            raise

    def __enter__(self) -> RegistroPacientes:
        return self

    def __exit__(self, exc_type, exc_value, traceback) -> None:
        self.cerrar()

    def cerrar(self) -> None:
        self._conexion.close()

    @staticmethod
    def _paciente(fila: sqlite3.Row) -> Paciente:
        return Paciente(
            id=fila["id"],
            codigo_historia=f"HC-{fila['id']:06d}",
            dni=fila["dni"],
            nombres=fila["nombres"],
            apellidos=fila["apellidos"],
            telefono=fila["telefono"],
            correo=fila["correo"],
        )

    def registrar(
        self,
        dni: str,
        nombres: str,
        apellidos: str,
        telefono: str = "",
        correo: str = "",
    ) -> Paciente:
        dni = _dni_valido(dni)
        nombres = _texto(nombres, "nombres", obligatorio=True)
        apellidos = _texto(apellidos, "apellidos", obligatorio=True)
        telefono = _texto(telefono, "teléfono")
        correo = _texto(correo, "correo")
        try:
            with self._conexion:
                cursor = self._conexion.execute(
                    """INSERT INTO pacientes
                    (dni, nombres, apellidos, telefono, correo)
                    VALUES (?, ?, ?, ?, ?)""",
                    (dni, nombres, apellidos, telefono, correo),
                )
                fila = self._conexion.execute(
                    "SELECT * FROM pacientes WHERE id = ?", (cursor.lastrowid,)
                ).fetchone()
        except sqlite3.IntegrityError as error:
            raise ValueError("Ya existe un paciente con ese DNI.") from error
        return self._paciente(fila)

    def buscar_por_dni(self, dni: str) -> Paciente | None:
        dni = _dni_valido(dni)
        fila = self._conexion.execute(
            "SELECT * FROM pacientes WHERE dni = ?", (dni,)
        ).fetchone()
        return None if fila is None else self._paciente(fila)


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Registro de pacientes de la clínica.")
    parser.add_argument(
        "--base-datos", default="data/local/clinica.sqlite3",
        help="Ruta del archivo SQLite; por defecto data/local/clinica.sqlite3.",
    )
    comandos = parser.add_subparsers(dest="comando", required=True)
    alta = comandos.add_parser("registrar", help="Registrar un paciente nuevo.")
    alta.add_argument("--dni", required=True)
    alta.add_argument("--nombres", required=True)
    alta.add_argument("--apellidos", required=True)
    alta.add_argument("--telefono", default="")
    alta.add_argument("--correo", default="")
    buscar = comandos.add_parser("buscar", help="Consultar un paciente por DNI.")
    buscar.add_argument("--dni", required=True)
    argumentos = parser.parse_args(argv)
    try:
        with RegistroPacientes(argumentos.base_datos) as registro:
            if argumentos.comando == "registrar":
                paciente = registro.registrar(
                    argumentos.dni, argumentos.nombres, argumentos.apellidos,
                    argumentos.telefono, argumentos.correo,
                )
            else:
                paciente = registro.buscar_por_dni(argumentos.dni)
                if paciente is None:
                    parser.exit(1, "Paciente no encontrado.\n")
    except (ValueError, sqlite3.Error, OSError) as error:
        parser.exit(2, f"Error: {error}\n")
    print(json.dumps(asdict(paciente), ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
