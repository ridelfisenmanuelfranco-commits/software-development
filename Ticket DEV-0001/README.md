# 🎬 Sistema de Gestión de Películas

> Proyecto desarrollado como parte de una simulación de una empresa de desarrollo de software, con el objetivo de fortalecer la lógica de programación y el desarrollo de aplicaciones de consola utilizando Python.

---

## 📖 Descripción

El **Sistema de Gestión de Películas** es una aplicación de consola que permite administrar una cartelera de películas mediante operaciones CRUD (Crear, Leer, Actualizar y Eliminar).

El proyecto implementa validaciones de datos, búsqueda por código, actualización de inventario y generación de estadísticas básicas, aplicando buenas prácticas de organización del código mediante funciones.

---

## 🎯 Objetivos del proyecto

- Practicar programación estructurada en Python.
- Implementar un sistema CRUD completo.
- Reforzar el uso de funciones.
- Trabajar con listas y diccionarios.
- Aplicar validaciones de entrada.
- Implementar búsqueda secuencial.
- Calcular estadísticas utilizando recorridos sobre listas.
- Mejorar la organización y legibilidad del código.

---

# ✨ Funcionalidades

El sistema permite:

- ✅ Registrar películas
- ✅ Mostrar todas las películas registradas
- ✅ Buscar películas por código
- ✅ Actualizar la cantidad de copias disponibles
- ✅ Eliminar películas
- ✅ Mostrar estadísticas generales
- ✅ Validar datos ingresados por el usuario

---

# 🛠 Tecnologías utilizadas

| Tecnología | Uso |
|------------|-----|
| Python 3 | Lenguaje principal |
| os | Limpieza de la consola |
| List | Almacenamiento de datos |
| Dictionary | Representación de cada película |

---

# 📂 Estructura del proyecto

```text
Sistema-Gestion-Peliculas/

│
├── main.py
└── README.md
```

---

# 📚 Datos almacenados

Cada película contiene la siguiente información:

| Campo | Descripción |
|---------|-------------|
| Código | Identificador único (PEL-001) |
| Título | Nombre de la película |
| Género | Género cinematográfico |
| Año | Año de lanzamiento |
| Cantidad | Copias disponibles |

---

# ⚙️ Menú principal

```text
1. Registrar Película
2. Mostrar Películas
3. Buscar Película
4. Actualizar Película
5. Eliminar Película
6. Mostrar Estadísticas
7. Salir
```

---

# 🚀 Instalación

Clonar el repositorio

```bash
git clone https://github.com/usuario/repositorio.git
```

Entrar al proyecto

```bash
cd Sistema-Gestion-Peliculas
```

Ejecutar

```bash
python main.py
```

---

# 📊 Estadísticas disponibles

El sistema calcula automáticamente:

- Total de películas registradas.
- Total de copias disponibles.
- Película con mayor cantidad de copias.
- Película con menor cantidad de copias.
- Cantidad de películas con más de cinco copias.
- Cantidad de películas con cinco copias o menos.

---

# 🧠 Conceptos de Python aplicados

Durante el desarrollo del proyecto se utilizaron:

- Variables
- Funciones
- Listas
- Diccionarios
- Condicionales
- Bucles `for`
- Bucles `while`
- Validaciones
- Manejo de excepciones (`try / except`)
- Recorridos secuenciales
- CRUD
- Parámetros y retorno de funciones
- Formateo de cadenas (`f-string`)

---

# 📈 Mejoras futuras

Algunas funcionalidades que podrían incorporarse en futuras versiones:

- Persistencia de datos mediante JSON.
- Edición completa de la información de una película.
- Búsqueda por título.
- Búsqueda por género.
- Ordenamiento por año.
- Ordenamiento alfabético.
- Eliminación lógica.
- Reportes más completos.
- Interfaz gráfica.
- Arquitectura modular.

---

# 📌 Estado del proyecto

🟢 Finalizado (Versión de aprendizaje)

Este proyecto cumple con los objetivos propuestos para practicar programación estructurada y la implementación de un sistema CRUD en Python.

---

# 👨‍💻 Autor

Desarrollado por **Ridelfis Enmanuel Franco** como parte de su proceso de aprendizaje y de una simulación de una empresa de desarrollo de software enfocada en la construcción de proyectos reales para fortalecer habilidades en desarrollo de software.

---