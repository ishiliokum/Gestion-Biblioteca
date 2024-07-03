import json
import datetime

def cargar_datos():
    """Carga los datos de la biblioteca desde el archivo JSON."""
    try:
        with open("biblioteca.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def guardar_datos(libros):
    """Guarda los datos de la biblioteca en el archivo JSON."""
    with open("biblioteca.json", "w") as f:
        json.dump(libros, f)

def registrar_libro(libros):
    """Solicita los datos de un libro al usuario y lo registra en la biblioteca."""
    titulo = input("Título del libro: ")
    autor = input("Autor del libro: ")
    while True:
        try:
            anio_publicacion = int(input("Año de publicación: "))
            if anio_publicacion > 0:
                break
            else:
                print("El año debe ser un número positivo.")
        except ValueError:
            print("Ingrese un año válido.")
    genero = input("Género del libro: ")
    libro = {"titulo": titulo, "autor": autor, "anio_publicacion": anio_publicacion, "genero": genero}
    libros.append(libro)
    guardar_datos(libros)
    print("Libro registrado exitosamente.")

def buscar_libro_por_autor(libros):
    """Busca libros por autor y muestra los resultados."""
    autor_buscado = input("Ingrese el autor a buscar: ")
    libros_encontrados = [libro for libro in libros if libro["autor"].lower() == autor_buscado.lower()]
    if libros_encontrados:
        print("Libros encontrados:")
        for libro in libros_encontrados:
            print(f"- {libro['titulo']} ({libro['genero']}), publicado en {libro['anio_publicacion']}")
    else:
        print("No se encontraron libros de ese autor.")

def mostrar_lista_libros(libros):
    """Muestra la lista completa de libros registrados."""
    if libros:
        print("Lista de libros:")
        for libro in libros:
            print(f"- {libro['titulo']} ({libro['genero']}) por {libro['autor']}, publicado en {libro['anio_publicacion']}")
    else:
        print("No hay libros registrados en la biblioteca.")

def main():
    """Función principal que ejecuta el menú y las opciones de la aplicación."""
    libros = cargar_datos()

    while True:
        print("\n--- Menú ---")
        print("1. Registrar libro")
        print("2. Buscar libro por autor")
        print("3. Mostrar lista de libros")
        print("4. Salir")

        opcion = input("Elija una opción: ")

        if opcion == '1':
            registrar_libro(libros)
        elif opcion == '2':
            buscar_libro_por_autor(libros)
        elif opcion == '3':
            mostrar_lista_libros(libros)
        elif opcion == '4':
            guardar_datos(libros)  
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida. Intente nuevamente.")

if __name__ == "__main__":
    main()
