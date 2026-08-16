#!/usr/bin/env python3
"""
verificar_ejercicio.py — plantilla base para el agente verificador-numerico.

Este archivo es un ESQUELETO que el agente verificador-numerico completa y
adapta por cada síntesis con ejercicios calculables: agrega una función
resolver_<nombre_ejercicio>() por cada ejercicio, con el cálculo hecho desde
cero a partir del enunciado (sin mirar la resolución del documento).

IMPORTANTE: una copia de la versión final y comentada de este script se
entrega también al usuario junto con la síntesis — no es solo uso interno
del pipeline. El objetivo es que el usuario pueda correrlo sobre sus propias
resoluciones y aprender a verificar resultados sin depender de nadie más.

Uso: python3 verificar_ejercicio.py
"""

import sympy as sp


def resolver_ejemplo():
    """
    EJEMPLO — reemplazar/duplicar esta función por cada ejercicio real
    de la síntesis. Mantener el patrón: variables simbólicas, cálculo
    explícito paso a paso, resultado final impreso con contexto.
    """
    x = sp.symbols("x")
    ecuacion = sp.Eq(2 * x + 3, 7)
    solucion = sp.solve(ecuacion, x)
    print(f"Ejemplo: 2x + 3 = 7  ->  x = {solucion[0]}")
    return solucion[0]


def main():
    print("=== Verificación independiente de ejercicios ===\n")
    resolver_ejemplo()
    # El agente verificador-numerico agrega acá una llamada por cada
    # función resolver_<ejercicio>() que defina para esta síntesis puntual.
    print("\n=== Fin de la verificación ===")
    print("Compará estos resultados contra los que aparecen en el documento.")
    print("Si no coinciden, revisá tu resolución paso a paso antes de asumir")
    print("que el documento tiene el error — el objetivo es que aprendas a")
    print("detectar vos mismo dónde está la discrepancia.")


if __name__ == "__main__":
    main()
