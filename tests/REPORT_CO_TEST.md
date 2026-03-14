# Reporte Test Colombia — Representante Legal

**Fecha:** 2026-03-14
**Servidor:** localhost:8000
**Timeout scraping:** 45s
**Total empresas testeadas:** 70

---

## Metricas generales

| Metrica | Valor | % |
|---------|-------|---|
| Encontradas en RUES | 45 | 64% |
| No encontradas en RUES | 25 | 36% |
| Con representante legal | 18 | 40% (de encontradas) |
| Sin representante legal | 27 | 60% (de encontradas) |

---

## Empresas con representante legal extraido (18)

| # | NIT | Empresa | Representante Legal |
|---|-----|---------|---------------------|
| 1 | 860025900 | Alpina | Lina Maria Prieto |
| 2 | 830095213 | Organizacion Terpel | Monica Maria Soler |
| 3 | 860500480 | Almacenes Corona | Jained Leo (parcial) |
| 4 | 860002130 | Nestle de Colombia | Felipe Gustavo Gonzalez Bustamante |
| 5 | 890300546 | Colgate Palmolive | Carlos Alberto (nombre parcial) |
| 6 | 800153993 | Comcel / Claro | Alvaro Jose Tovar Reyes |
| 7 | 900341086 | Comercial Nutresa | (nombre parcial — incluye texto extra) |
| 8 | 830063506 | Transmilenio | Maria Fernanda Ortiz Carrascal |
| 9 | 900103877 | Kinco | Juan David Hernandez Betancur |
| 10 | 900926147 | Grupo Quincena | Juan Felipe Rodriguez Cuervo |
| 11 | 901987605 | Aihuevos | Daniel Cardona Gonzalez |
| 12 | 900276962 | Koba Colombia / D1 | Luis Felipe Rincon |
| 13 | 900092385 | UNE EPM Telecomunicaciones | (nombre parcial — incluye texto extra) |
| 14 | 800209179 | Colombiana de Encomiendas | Buitrago Silva Henry Eduardo |
| 15 | 811036875 | Servicios Generales Suramericana | Maira Alejandra Mazo Vahos |
| 16 | 900433032 | Terpel Combustibles | Alfonso Ibarra Castillo |
| 17 | 830095262 | Qmax Solutions Colombia | Juan Pablo Nicolas |
| 18 | 830130106 | Soenergy International Colombia | Alfredo Botta Espinosa |

> **Nota:** 3 empresas tienen nombres parciales o con texto extra — indica patrones que matchean pero capturan datos incorrectos.

---

## Empresas encontradas SIN representante legal (27)

| # | NIT | Empresa | Error |
|---|-----|---------|-------|
| 1 | 890903938 | Bancolombia | No se pudo extraer informacion del Gerente |
| 2 | 860034313 | Davivienda | No se pudo extraer informacion del Gerente |
| 3 | 890903939 | Postobon | No se pudo extraer informacion del Gerente |
| 4 | 890900608 | Almacenes Exito | No se pudo extraer informacion del Gerente |
| 5 | 900017447 | Falabella de Colombia | No se encontro contenido de Representante legal |
| 6 | 890107487 | Olimpica | No se pudo extraer informacion del Gerente |
| 7 | 890100577 | Avianca | No se pudo extraer informacion del Gerente |
| 8 | 830002366 | Bimbo de Colombia | No se encontro pestana de Representante legal |
| 9 | 890105526 | Promigas | No se pudo extraer informacion del Gerente |
| 10 | 811030322 | Celsia | No se pudo extraer informacion del Gerente |
| 11 | 890900308 | Fabricato | No se pudo extraer informacion del Gerente |
| 12 | 890903407 | Seguros Generales Suramericana | No se pudo extraer informacion del Gerente |
| 13 | 900539730 | Carvajal S.A.S | No se pudo extraer informacion del Gerente |
| 14 | 860004871 | Curacao de Colombia | No se encontro pestana de Representante legal |
| 15 | 890903790 | Seguros de Vida Suramericana | No se pudo extraer informacion del Gerente |
| 16 | 830047819 | Coca-Cola Servicios Colombia | No se pudo extraer informacion del Gerente |
| 17 | 900047981 | Banco Falabella | No se pudo extraer informacion del Gerente |
| 18 | 860068182 | Credicorp Capital Colombia | No se pudo extraer informacion del Gerente |
| 19 | 800250328 | Transejes Colombia | No se pudo extraer informacion del Gerente |
| 20 | 900154405 | Global Sales Solutions Colombia | No se pudo extraer informacion del Gerente |
| 21 | 900158160 | Comercializadora Nacional Colombia | No se pudo extraer informacion del Gerente |
| 22 | 900943243 | Suramerica Comercial | No se pudo extraer informacion del Gerente |
| 23 | 900058954 | Suramericana de Partes | No se pudo extraer informacion del Gerente |
| 24 | 890301163 | Distribuidora Colombina | No se pudo extraer informacion del Gerente |
| 25 | 900102022 | Lifecycle Solutions Colombia | No se pudo extraer informacion del Gerente |
| 26 | 901125212 | Seisa Technologies | No se pudo extraer informacion del Gerente |
| 27 | 900330855 | Laboratorios OSA | No se encontro contenido de Representante legal |

### Tipos de error

| Error | Cantidad | Causa probable |
|-------|----------|----------------|
| No se pudo extraer informacion del Gerente | 23 | Patron de texto no reconocido |
| No se encontro pestana de Representante legal | 2 | La empresa no tiene esa pestana en RUES |
| No se encontro contenido de Representante legal | 2 | Pestana existe pero sin contenido parseable |

---

## Empresas NO encontradas en RUES (25)

| # | NIT | Empresa | Causa probable |
|---|-----|---------|----------------|
| 1 | 899999068 | Ecopetrol | NIT incorrecto o timeout |
| 2 | 860005224 | Bavaria | NIT incorrecto o timeout |
| 3 | 890100251 | Cementos Argos | NIT incorrecto o timeout |
| 4 | 890921974 | Alkosto / Corbeta | NIT incorrecto o timeout |
| 5 | 890900076 | Cine Colombia | NIT incorrecto o timeout |
| 6 | 860512249 | Yanbal de Colombia | NIT incorrecto o timeout |
| 7 | 890301884 | Colombina | NIT incorrecto o timeout |
| 8 | 830114921 | Colombia Movil / Tigo | NIT incorrecto o timeout |
| 9 | 811019012 | Suramericana | NIT incorrecto o timeout |
| 10 | 890504493 | Mussi Zapatos | Timeout (funciona con mas tiempo) |
| 11 | 901216768 | Adelante Soluciones Financieras | Timeout (funciona con mas tiempo) |
| 12 | 890900943 | Colombiana de Comercio | NIT incorrecto o timeout |
| 13 | 800088702 | EPS Suramericana | NIT incorrecto o timeout |
| 14 | 860006764 | Provincia Ntra Sra Gracia | NIT incorrecto o timeout |
| 15 | 890935493 | Mapei Colombia | NIT incorrecto o timeout |
| 16 | 900169804 | Fermax Electronica Colombia | NIT incorrecto o timeout |
| 17 | 900494355 | Supertechos Colombia | NIT incorrecto o timeout |
| 18 | 900284878 | Importadora Comercializadora Tecnologia | NIT incorrecto o timeout |
| 19 | 800216181 | Grupo Aval Acciones y Valores | NIT incorrecto o timeout |
| 20 | 807009444 | Cooperativa Suramericana Transportes | NIT incorrecto o timeout |
| 21 | 800182390 | Suramericana de Guantes | NIT incorrecto o timeout |
| 22 | 860059294 | Leasing Bancolombia | NIT incorrecto o timeout |
| 23 | 800095254 | American Airlines Sucursal Colombia | NIT incorrecto o timeout |
| 24 | 890101815 | Johnson & Johnson de Colombia | NIT incorrecto o timeout |
| 25 | 860000762 | Ladrillera Santafe | NIT incorrecto o timeout |

---

## Patrones de representante legal soportados

| Formato | Descripcion | Ejemplo |
|---------|-------------|---------|
| A | `Representante <Nombre> C.C. No. <ID> Legal (Gerente)` | Adelante Soluciones Financieras |
| B | `GERENTE PRINCIPAL <Nombre> <ID con puntos>` | Grupo Quincena |
| C | `REPRESENTACION LEGAL (PRINCIPALES) **** <ID> - <Nombre>` | Mussi Zapatos |
| D | `REPRESENTANTE LEGAL <Nombre> C.C. <ID con puntos> PRINCIPAL <Apellido>` | Kinco |
| E | `Gerente General <Nombre> C.C. No. <ID>` | Transmilenio |

---

## Siguiente paso

Scrappear el texto de representante legal de las 23 empresas con error "No se pudo extraer" para identificar nuevos patrones y subir la tasa de exito del 40% actual.
