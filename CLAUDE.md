# CLAUDE.md — Merchant Precheck Public Database Lookup

## Que es este proyecto

Microservicio REST que consulta bases de datos publicas oficiales de empresas dado un identificador tributario (NIT para Colombia, RUC para Peru) y el pais. Hace web scraping a la fuente publica correspondiente y retorna un JSON estructurado con la informacion de la empresa.

## Tech Stack

Por definir en la primera iteracion de desarrollo. Candidatos:

- **Opcion A:** Python 3.12+ / FastAPI / Uvicorn / Playwright o httpx + BeautifulSoup4
- **Opcion B:** Node.js / TypeScript / Express o Fastify / Puppeteer o Cheerio

## Estructura del proyecto

```
(por definir durante la implementacion)
```

## Endpoints

| Metodo | Ruta | Auth | Descripcion |
|--------|------|------|-------------|
| GET | `/healthz` | No | Liveness probe |
| POST | `/v1/lookup` | Bearer token | Consulta de empresa por identificador tributario |

## Variables de entorno

| Variable | Default | Requerida | Descripcion |
|----------|---------|-----------|-------------|
| `API_KEY` | `""` | Si (prod) | Bearer token para auth |
| `PORT` | `8000` | No | Puerto del servidor |

## Paises soportados

| Pais | Identificador | Fuente oficial |
|------|---------------|----------------|
| Colombia | NIT | RUES |
| Peru | RUC | SUNAT |

## Gitflow y versionamiento

### Branching (Gitflow simplificado)

```
main <- produccion
  └── develop <- integracion de features
       └── feature/* <- desarrollo
       └── fix/* <- correcciones
```

- **PRs siempre**: `feature/*` -> `develop` -> `main`. Nunca push directo a `main` o `develop`.

### Versionamiento (SemVer)

- Archivo `VERSION` en la raiz es el single source of truth.
- Formato: `MAJOR.MINOR.PATCH` (ej. `0.1.0`).

### Conventional Commits

Formato: `<tipo>: <descripcion>` — tipos: `feat`, `fix`, `refactor`, `docs`, `test`, `chore`, `style`.

## Git

- Branch principal: `main`, integracion: `develop`
- Este proyecto es un repo git independiente dentro de `agents-hub/projects/`
- Remote: `https://github.com/katerinearias-druo/merchant-precheck-public-database-lookup.git`
