import dearpygui.dearpygui as dpg
import ctypes  # Para obtener tamaño de pantalla en Windows

# Obtener tamaño de pantalla (Windows)
user32 = ctypes.windll.user32
pantalla_ancho = user32.GetSystemMetrics(0)
pantalla_alto = user32.GetSystemMetrics(1)

# Tamaño deseado de la ventana
ventana_ancho = 400
ventana_alto = 200

# Calcular coordenadas para centrar la ventana
x_centro = (pantalla_ancho - ventana_ancho) // 2
y_centro = (pantalla_alto - ventana_alto) // 2

# Diccionario de usuarios válidos
USUARIOS = {
    "admin": "1Admin1!.",
    "usuario": "1Usuario1!."
}

# Validación del login
def validar_login():
    usuario = dpg.get_value("input_usuario")
    contrasena = dpg.get_value("input_contraseña")

    if usuario in USUARIOS and USUARIOS[usuario] == contrasena:
        dpg.set_value("resultado", f"Bienvenido, {usuario}")
    else:
        dpg.set_value("resultado", "Usuario o contraseña incorrectos")

# Crear GUI
dpg.create_context()
dpg.create_viewport(title="Login Dear PyGui", width=ventana_ancho, height=ventana_alto,
                    x_pos=x_centro, y_pos=y_centro)

with dpg.window(label="Login", width=ventana_ancho - 20, height=ventana_alto - 20):
    dpg.add_input_text(label="Usuario", tag="input_usuario")
    dpg.add_input_text(label="Contraseña", password=True, tag="input_contraseña")
    dpg.add_button(label="Ingresar", callback=validar_login)
    dpg.add_text("", tag="resultado")

dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()