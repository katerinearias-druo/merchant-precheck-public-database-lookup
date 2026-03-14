# Contributing — Merchant Precheck Public Database Lookup

## Gitflow simplificado

Este proyecto usa un modelo de branching simplificado con 3 tipos de branches:

```
main          ← codigo estable, releases taggeadas
  └── develop ← integracion de features, staging
       └── feature/*  ← desarrollo de features individuales
       └── fix/*      ← correccion de bugs
```

### Branches

| Branch | Proposito | Se mergea a |
|--------|-----------|-------------|
| `main` | Produccion. Cada merge genera un release automatico. | — |
| `develop` | Integracion. Aqui se juntan features antes de ir a main. | `main` |
| `feature/*` | Desarrollo de una feature nueva. | `develop` |
| `fix/*` | Correccion de un bug. | `develop` |

### Flujo de trabajo

1. **Crear branch** desde `develop`:
   ```bash
   git checkout develop
   git pull origin develop
   git checkout -b feature/mi-feature
   ```

2. **Desarrollar** y hacer commits siguiendo Conventional Commits.

3. **Abrir PR** hacia `develop`. El CI corre automaticamente (lint + tests).

4. **Code review** + merge a `develop`.

5. **Release**: cuando `develop` esta listo, abrir PR de `develop` → `main`. Al mergear, se crea un tag y release automaticamente.

## Conventional Commits

Todos los commits deben seguir el formato:

```
<tipo>: <descripcion corta>
```

### Tipos permitidos

| Tipo | Cuando usarlo |
|------|---------------|
| `feat` | Nueva funcionalidad |
| `fix` | Correccion de bug |
| `refactor` | Refactorizacion sin cambio funcional |
| `docs` | Cambios en documentacion |
| `test` | Agregar o modificar tests |
| `chore` | Mantenimiento, dependencias, CI/CD |
| `style` | Formato, espacios, sin cambio de logica |

### Ejemplos

```
feat: add RUES lookup for Colombian NIT
fix: handle timeout in RUES scraping
docs: update API endpoint documentation
chore: upgrade playwright to 1.45.0
test: add unit tests for NIT validator
```

## Versionamiento (SemVer)

Usamos [Semantic Versioning](https://semver.org/):

```
MAJOR.MINOR.PATCH
```

| Componente | Cuando incrementar |
|------------|-------------------|
| **MAJOR** | Cambio incompatible en la API (breaking change) |
| **MINOR** | Nueva funcionalidad compatible hacia atras |
| **PATCH** | Correccion de bug compatible hacia atras |

### Como actualizar la version

1. Editar el archivo `VERSION` en la raiz del proyecto.
2. Incluir el cambio de version en el mismo PR o en uno dedicado.
3. Al mergear a `main`, el CI crea automaticamente el tag `v{VERSION}` y el GitHub Release.

**Archivo VERSION** es el single source of truth. `app/main.py` lo lee automaticamente.

## Setup local

```bash
# Clonar e instalar
git clone https://github.com/katerinearias-druo/merchant-precheck-public-database-lookup.git
cd merchant-precheck-public-database-lookup
pip install -r requirements.txt
playwright install --with-deps chromium

# Correr tests
pytest tests/ -v

# Correr servidor
API_KEY=test uvicorn app.main:app --reload
```

## Checklist antes de abrir un PR

- [ ] Los tests pasan: `pytest tests/ -v`
- [ ] El codigo esta formateado
- [ ] El commit message sigue Conventional Commits
- [ ] Si es un cambio de version, el archivo `VERSION` fue actualizado
- [ ] La descripcion del PR explica el "por que" del cambio
