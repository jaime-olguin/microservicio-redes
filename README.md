# MICROSERVICIO DE MONITOREO DE REDES (DEVOPS)

este repositorio contiene la base de un microservicio desarolllado en python (Flask) para la consulta del estado de infraestructura de telecomunicaciones, preparado para la implmentacion de pipelines CI/CD.

## 1-. Justificación del modelo de ramificacion (GITFLOW)

para este proyecto se implemente GITFLOW como estrategia de ramificacion y control de versiones por las siguiente razones tecnicas:


* Separación de entornos y estabbilidad: Permite mantenes una rama de produccion (´main´) estable y auditada, mientras el trabajo de integracion continua se centraliza en "denvelop"
* Desarrollo modular y colaborativo: las ramas `feature/<nombre>` permiten aislar nuevas funcionalidades o módulos sin interferir con el trabajo de otros desarrolladores.
* respuesta a incidentes criticos: la existencia de ramas `hotfix/<nombre>` permite corregir errores urgentes directamente derivados de "main" y reintegrar la solucion tanto a produccion como al flujo de desarrollo sin arrastrar codigo experimental.
* Compatibilidad con pipelines CI/CD: Facilita la automatizacion de pruebas y despliegues por etapas: validaciones rapidas en "DEVELOP" y despliegus finales o empaquetado seguro en "main".

## 2-. Guía de buenas prácticas y convenciones

### Naming de ramas

* `main`: Código en prudccion, version estable y etiquetada (tags).
* `develop`: Rama principal de integración donde convergen las características terminadas.
* `feature/<nombre-tarea>`: Ramas temporales para nuevas funcionalidades
* `hotflix/<nombre-bug>`: Ramas de correcion crítica que nacen de `main`

### Convención de Commits (Conventional Commits)
Los mensajes deben ser descriptivos, en minúsculas y utilizando prefijos estandarizados:
* `feat:` Nueva característica o funcionalidad añadida.
* `fix:` Corrección de un error o bug en el código.
* `docs:` Cambios o adiciones en la documentación (ej. README).
* `ci:` Ajustes en archivos de configuración de pipelines (GitHub Actions).
* `refactor:` Modificación de código que no añade funcionalidades ni corrige bugs.

# Flujo de Trabajo y Merges
1. Ningún cambio se sube directamente a `main` o `develop`.
2. Todo cambio debe realizarse en su rama específica (`feature/` o `hotfix/`).
3. La integración se realiza exclusivamente mediante **Pull Requests (PR)**.
4. Se requiere revisión previa de código y validación exitosa de las comprobaciones automáticas (GitHub Actions) antes de fusionar.

### Estructura del Proyecto
```text
microservicio-redes/
├── .github/
│   └── workflows/
│       └── pipeline.yml       # Definición de CI/CD con GitHub Actions
├── app.py                     # Código fuente del microservicio Flask
├── requirements.txt           # Dependencias del proyecto
└── README.md                  # Documentación técnica del repositorio