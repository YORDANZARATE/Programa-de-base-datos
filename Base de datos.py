import sqlite3

# Conectar a la base de datos (o crearla si no existe)
conn = sqlite3.connect('usuarios.db')
cursor = conn.cursor()

# Crear tabla de usuarios
cursor.execute('''
CREATE TABLE IF NOT EXISTS usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    edad INTEGER NOT NULL
)
''')


def agregar_usuario(nombre, edad):
    cursor.execute('INSERT INTO usuarios (nombre, edad) VALUES (?, ?)', (nombre, edad))
    conn.commit()


def obtener_usuarios():
    cursor.execute('SELECT * FROM usuarios')
    return cursor.fetchall()


def actualizar_usuario(user_id, nombre, edad):
    cursor.execute('UPDATE usuarios SET nombre = ?, edad = ? WHERE id = ?', (nombre, edad, user_id))
    conn.commit()


def eliminar_usuario(user_id):
    cursor.execute('DELETE FROM usuarios WHERE id = ?', (user_id,))
    conn.commit()


def main():
    while True:
        print("\nOpciones:")
        print("1. Agregar usuario")
        print("2. Ver usuarios")
        print("3. Actualizar usuario")
        print("4. Eliminar usuario")
        print("5. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == '1':
            nombre = input("Nombre: ")
            edad = int(input("Edad: "))
            Celular=int(input("Celular: "))
            agregar_usuario(nombre, edad)
            print("Usuario agregado.")

        elif opcion == '2':
            usuarios = obtener_usuarios()
            for usuario in usuarios:
                print(usuario)

        elif opcion == '3':
            user_id = int(input("ID del usuario a actualizar: "))
            nombre = input("Nuevo nombre: ")
            edad = int(input("Nueva edad: "))
            actualizar_usuario(user_id, nombre, edad)
            print("Usuario actualizado.")

        elif opcion == '4':
            user_id = int(input("ID del usuario a eliminar: "))
            eliminar_usuario(user_id)
            print("Usuario eliminado.")

        elif opcion == '5':
            break

        else:
            print("Opción no válida.")


# Cerrar la conexión antes de salir
try:
    main()
finally:
    conn.close()
