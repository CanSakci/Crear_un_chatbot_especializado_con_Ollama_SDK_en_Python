import sys
from core.chatbot import ChatbotExpertos

def mostrar_menu():
    # Muestra las opciones disponibles en la interfaz de consola
    print("\n" + "="*45)
    print("   MENÚ DE SELECCIÓN DE EXPERTO TEMÁTICO")
    print("="*45)
    print("1. 💻 Experto en Programación de Software")
    print("2. 📈 Experto en Marketing y Estrategia")
    print("3. ⚖️  Experto Jurídico-Legal")
    print("4. 🔄 Reiniciar conversación actual")
    print("5. ❌ Salir de la aplicación")
    print("="*45)

def main():
    # Mensaje de bienvenida informativo
    print("\nIniciando sistema...")
    print("Bienvenido al Chatbot Multiexperto (Conexión Offline - Modelo: gemma3:1b)")
    
    bot = ChatbotExpertos(modelo="gemma3:1b")
    
    # Diccionario para mapear la entrada numérica a la clave del experto correspondiente
    opciones_expertos = {
        "1": "programacion",
        "2": "marketing",
        "3": "juridico"
    }

    while True:
        mostrar_menu()
        opcion = input("\nSelecciona una opción introduciendo un número (1-5): ").strip()

        if opcion == "5":
            print("\nFinalizando el sistema. ¡Hasta pronto!")
            sys.exit(0)
            
        elif opcion == "4":
            # Permite vaciar la memoria de la conversación sin cambiar de especialidad
            if bot.experto_actual:
                bot.establecer_experto(bot.experto_actual)
                print("\n[INFO] El historial de la conversación ha sido reiniciado con éxito.")
            else:
                print("\n[ADVERTENCIA] Aún no has seleccionado a ningún experto para reiniciar.")
            continue
            
        elif opcion in opciones_expertos:
            clave_experto = opciones_expertos[opcion]
            bot.establecer_experto(clave_experto)
            print(f"\n[INFO] Conectado exitosamente con el experto: {clave_experto.upper()}")
            
            # Bucle de interacción continua con el experto seleccionado
            while True:
                print(f"\n[{clave_experto.capitalize()}] | (Escribe 'menu' para cambiar o 'salir' para cerrar)")
                entrada_usuario = input("Tú: ").strip()
                
                # Opciones de salida del bucle interno
                if entrada_usuario.lower() == 'salir':
                    print("\nFinalizando el sistema. ¡Hasta pronto!")
                    sys.exit(0)
                elif entrada_usuario.lower() == 'menu':
                    print("\nRegresando al menú principal...")
                    break
                elif not entrada_usuario:
                    continue
                
                # Proceso de generación y muestra de respuesta
                print("\nAnalizando consulta...")
                respuesta = bot.enviar_mensaje(entrada_usuario)
                print(f"\n🤖 Experto: {respuesta}")
                
        else:
            print("\n[ERROR] Opción no válida. Por favor, asegúrate de introducir un número del 1 al 5.")

if __name__ == "__main__":
    main()