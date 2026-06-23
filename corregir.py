"""
Corrector automatico — Evaluacion Final de Python

Ejecuta todos los tests, muestra resultados por modulo
y calcula la nota final.

Uso:
    python corregir.py
"""

import sys
import pytest


MODULOS = [
    {
        "nombre": "Modulo 1 — procesar.py",
        "archivo": "tests/test_procesar.py",
        "archivo_alumno": "procesar.py",
        "tests": 12,
        "temas": "for, if, print, listas, indices, float()",
    },
    {
        "nombre": "Modulo 2 — analisis.py",
        "archivo": "tests/test_analisis.py",
        "archivo_alumno": "analisis.py",
        "tests": 17,
        "temas": "funciones, return, parametros, dict, formulas",
    },
    {
        "nombre": "Modulo 3 — procesador.py",
        "archivo": "tests/test_procesador.py",
        "archivo_alumno": "procesador.py",
        "tests": 19,
        "temas": "clases, __init__, self, csv.DictReader",
    },
]


class ColectorResultados:
    """Captura los resultados de pytest por archivo de test."""

    def __init__(self):
        self.por_modulo = {}
        self.errores = {}

    def pytest_collection_modifyitems(self, items):
        pass

    def pytest_runtest_logreport(self, report):
        if report.when == "call":
            archivo = report.nodeid.split("::")[0]
            if archivo not in self.por_modulo:
                self.por_modulo[archivo] = {"pasaron": 0, "fallaron": 0, "total": 0}
                self.errores[archivo] = []
            if report.passed:
                self.por_modulo[archivo]["pasaron"] += 1
            elif report.failed:
                self.por_modulo[archivo]["fallaron"] += 1
                self.errores[archivo].append(report.nodeid)
            self.por_modulo[archivo]["total"] += 1

    def resultado_modulo(self, archivo_test):
        r = self.por_modulo.get(archivo_test, {"pasaron": 0, "fallaron": 0, "total": 0})
        return r["pasaron"], r["total"], self.errores.get(archivo_test, [])


def barra(pasaron, total, ancho=30):
    """Dibuja una barra de progreso tipo [#####·····]."""
    proporcion = pasaron / total if total > 0 else 0
    llenos = int(proporcion * ancho)
    vacios = ancho - llenos
    return "[" + "#" * llenos + "·" * vacios + "]"


def main():
    print("=" * 60)
    print("  CORRECTOR AUTOMATICO — Evaluacion Final de Python")
    print("=" * 60)
    print()

    # Verificar archivos del alumno
    print("--- Verificando archivos del alumno ---")
    todos_existen = True
    for m in MODULOS:
        archivo = m["archivo_alumno"]
        existe = False
        try:
            with open(archivo):
                existe = True
        except FileNotFoundError:
            existe = False
        marca = "✓" if existe else "✗ FALTA"
        if not existe:
            todos_existen = False
        print(f"  {marca}  {archivo}")
    print()

    if not todos_existen:
        print("  FALTAN ARCHIVOS. Crea los archivos marcados con ✗ y volve a ejecutar.")
        print()
        sys.exit(1)

    # Ejecutar tests
    print("--- Ejecutando tests ---")
    colector = ColectorResultados()
    archivos_test = [m["archivo"] for m in MODULOS]
    args = ["--tb=line", "-q"] + archivos_test

    exit_code = pytest.main(args, plugins=[colector])
    print()
    print()

    # Mostrar resultados por modulo
    print("--- Resultados por modulo ---")
    print()
    puntaje_total = 0
    tests_totales = 0
    modulos_aprobados = 0

    for m in MODULOS:
        pasaron, total, errores = colector.resultado_modulo(m["archivo"])
        puntaje_total += pasaron
        tests_totales += total

        estado = "APROBADO" if pasaron == total else "INCOMPLETO"
        if pasaron == total:
            modulos_aprobados += 1

        print(f"  {m['nombre']}")
        print(f"  Temas: {m['temas']}")
        print(f"  Tests: {barra(pasaron, total)} {pasaron}/{total}")
        print(f"  Estado: {estado}")
        if errores:
            print(f"  Tests que fallan ({len(errores)}):")
            for e in errores[:5]:
                nombre_test = e.split("::")[-1]
                print(f"    · {nombre_test}")
            if len(errores) > 5:
                print(f"    ... y {len(errores) - 5} mas")
        print()
        print()

    # Nota final
    print("--- NOTA FINAL ---")
    print()

    if modulos_aprobados == 3:
        print(f"  {puntaje_total}/{tests_totales} tests pasando")
        print(f"  Modulos: {modulos_aprobados}/3")
        print()
        print("  ★ ★ ★ ★ ★  EXCELENTE  ★ ★ ★ ★ ★")
        print("  Todos los modulos completados.")
    elif modulos_aprobados == 2:
        print(f"  {puntaje_total}/{tests_totales} tests pasando")
        print(f"  Modulos: {modulos_aprobados}/3")
        print()
        print("  ★ ★ ★ ☆ ☆  MUY BIEN")
        print("  Te falta 1 modulo para completar la evaluacion.")
    elif modulos_aprobados == 1:
        print(f"  {puntaje_total}/{tests_totales} tests pasando")
        print(f"  Modulos: {modulos_aprobados}/3")
        print()
        print("  ★ ★ ☆ ☆ ☆  EN PROCESO")
        print("  Segui avanzando, ya arrancaste.")
    else:
        print(f"  {puntaje_total}/{tests_totales} tests pasando")
        print(f"  Modulos: {modulos_aprobados}/3")
        print()
        print("  ☆ ☆ ☆ ☆ ☆  INTENTALO DE NUEVO")
        print("  Revisa los mensajes de error y volve a intentar.")

    print()
    print("=" * 60)


if __name__ == "__main__":
    main()
