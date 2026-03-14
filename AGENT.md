# AGENT.md — Merchant Precheck Public Database Lookup

## Rol

Agente de **generacion de codigo** para construir un servicio REST desplegable en Railway que consulta bases de datos publicas oficiales de empresas por identificador tributario.

## Descripcion

Dado un identificador tributario (NIT para Colombia, RUC para Peru) y el pais, el servicio hace web scraping a la fuente publica oficial correspondiente y retorna un JSON estructurado con la informacion relevante de la empresa o persona.

### Fuentes publicas por pais

| Pais | Identificador | Fuente oficial |
|------|---------------|----------------|
| Colombia | NIT | RUES (Registro Unico Empresarial y Social) |
| Peru | RUC | SUNAT (Superintendencia Nacional de Aduanas y de Administracion Tributaria) |

## Input

- Descripcion funcional o tecnica de lo que se necesita implementar.
- Pais y fuente publica objetivo (si aplica).
- Bugs, mejoras o features solicitadas.

## Output

- Codigo fuente listo para ejecutar y desplegar.
- Archivos de configuracion (Dockerfile, requirements/package.json, .env.example, etc.).
- Tests cuando aplique.

## Reglas

1. **Lenguaje:** Node.js (TypeScript preferido) o Python (FastAPI). Decidir segun la complejidad del scraping.
2. **Estructura clara:** Separar rutas, logica de scraping, modelos de respuesta y configuracion.
3. **Scraping robusto:** Manejar cambios en el DOM de las fuentes oficiales con selectores resilientes. Incluir reintentos y timeouts.
4. **Respuesta estandar:** Siempre retornar un JSON con estructura consistente independientemente del pais consultado.
5. **Variables de entorno:** Toda configuracion sensible o variable por ambiente debe ir en env vars.
6. **Despliegue Railway-ready:** Incluir Dockerfile o configuracion compatible con Railway.
7. **Sin dependencias innecesarias:** Solo instalar lo estrictamente necesario.
8. **Conventional Commits:** Seguir el formato `<tipo>: <descripcion>`.
9. **Gitflow:** Branches `main` y `develop`. Features en `feature/*`, fixes en `fix/*`.

## Instrucciones de ejecucion

1. El usuario describe que necesita (nuevo endpoint, nuevo pais, bugfix, mejora).
2. El agente analiza la solicitud y propone un plan de implementacion.
3. Con la confirmacion del usuario, el agente genera el codigo.
4. El agente indica como probar y desplegar los cambios.
