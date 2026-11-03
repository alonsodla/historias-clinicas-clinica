"""Pruebas del contrato público del registro de pacientes."""

import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from src.pacientes import RegistroPacientes


ROOT = Path(__file__).resolve().parents[1]


class PruebasRegistroPacientes(unittest.TestCase):
    def setUp(self):
        self.directorio = tempfile.TemporaryDirectory()
        self.addCleanup(self.directorio.cleanup)
        self.base = Path(self.directorio.name) / "pacientes.sqlite3"
        self.registro = RegistroPacientes(self.base)
        self.addCleanup(self.registro.cerrar)

    def test_registra_paciente_y_genera_codigo(self):
        paciente = self.registro.registrar(
            " 00123456 ", " Ana ", " Prueba ", " 900000001 ", " ana@example.test "
        )
        self.assertEqual(paciente.dni, "00123456")
        self.assertEqual(paciente.nombres, "Ana")
        self.assertEqual(paciente.apellidos, "Prueba")
        self.assertEqual(paciente.telefono, "900000001")
        self.assertEqual(paciente.correo, "ana@example.test")
        self.assertEqual(paciente.codigo_historia, "HC-000001")
        self.assertEqual(self.registro.buscar_por_dni("00123456"), paciente)

    def test_persiste_al_abrir_otra_conexion(self):
        esperado = self.registro.registrar("00123456", "Ana", "Prueba")
        with RegistroPacientes(self.base) as segunda:
            self.assertEqual(segunda.buscar_por_dni("00123456"), esperado)

    def test_dni_duplicado_no_reemplaza_datos(self):
        original = self.registro.registrar("00123456", "Ana", "Prueba")
        with self.assertRaisesRegex(ValueError, "existe un paciente"):
            self.registro.registrar("00123456", "Otra", "Persona")
        self.assertEqual(self.registro.buscar_por_dni("00123456"), original)
        segundo = self.registro.registrar("00876543", "Diego", "Prueba")
        self.assertNotEqual(segundo.codigo_historia, original.codigo_historia)

    def test_rechaza_formatos_invalidos_de_dni(self):
        for dni in ("", "123", "123456789", "123A5678", "１２３４５６７８", 12345678):
            with self.subTest(dni=dni):
                with self.assertRaises(ValueError):
                    self.registro.registrar(dni, "Ana", "Prueba")

    def test_rechaza_nombres_y_apellidos_vacios(self):
        for nombres, apellidos in (("", "Prueba"), ("   ", "Prueba"), ("Ana", "\t")):
            with self.subTest(nombres=nombres, apellidos=apellidos):
                with self.assertRaisesRegex(ValueError, "obligatorio"):
                    self.registro.registrar("00123456", nombres, apellidos)
        self.assertIsNone(self.registro.buscar_por_dni("00123456"))

    def test_dos_pacientes_conservan_datos_independientes(self):
        primero = self.registro.registrar("00123456", "Ana", "Prueba")
        segundo = self.registro.registrar("00876543", "Diego", "Prueba")
        self.assertNotEqual(primero.codigo_historia, segundo.codigo_historia)
        self.assertEqual(self.registro.buscar_por_dni("00123456"), primero)
        self.assertEqual(self.registro.buscar_por_dni("00876543"), segundo)

    def test_nombre_con_apostrofo_se_guarda_completo(self):
        paciente = self.registro.registrar("00123456", "Ana", "D'Prueba")
        self.assertEqual(self.registro.buscar_por_dni("00123456"), paciente)
        self.assertEqual(paciente.apellidos, "D'Prueba")

    def test_busqueda_sin_coincidencia_devuelve_none(self):
        self.assertIsNone(self.registro.buscar_por_dni("00123456"))

    def test_datos_opcionales_pueden_omitirse(self):
        paciente = self.registro.registrar("00123456", "Ana", "Prueba")
        self.assertEqual((paciente.telefono, paciente.correo), ("", ""))


class PruebasLineaComandos(unittest.TestCase):
    def setUp(self):
        self.directorio = tempfile.TemporaryDirectory()
        self.addCleanup(self.directorio.cleanup)
        self.base = Path(self.directorio.name) / "clinica.sqlite3"

    def ejecutar(self, *argumentos):
        return subprocess.run(
            [sys.executable, "-m", "src.pacientes", "--base-datos", str(self.base),
             *argumentos],
            cwd=ROOT, capture_output=True, text=True, encoding="utf-8",
        )

    def alta(self):
        return self.ejecutar(
            "registrar", "--dni", "00123456", "--nombres", "Ana",
            "--apellidos", "Prueba",
        )

    def test_alta_y_busqueda_en_procesos_distintos(self):
        alta = self.alta()
        self.assertEqual(alta.returncode, 0, alta.stderr)
        consulta = self.ejecutar("buscar", "--dni", "00123456")
        self.assertEqual(consulta.returncode, 0, consulta.stderr)
        self.assertEqual(json.loads(consulta.stdout), json.loads(alta.stdout))

    def test_duplicado_informa_error_sin_confirmacion_de_exito(self):
        self.assertEqual(self.alta().returncode, 0)
        duplicado = self.alta()
        self.assertEqual(duplicado.returncode, 2)
        self.assertEqual(duplicado.stdout, "")
        self.assertIn("existe un paciente", duplicado.stderr)

    def test_busqueda_sin_resultado_tiene_estado_identificable(self):
        consulta = self.ejecutar("buscar", "--dni", "00123456")
        self.assertEqual(consulta.returncode, 1)
        self.assertEqual(consulta.stdout, "")
        self.assertIn("no encontrado", consulta.stderr)


if __name__ == "__main__":
    unittest.main()
