class HistorialConversacion:
    """Clase encargada de gestionar el historial de mensajes de la conversación actual."""
    
    def __init__(self):
        # Inicializa la lista de mensajes vacía
        self.mensajes = []

    def agregar_mensaje(self, rol, contenido):
        # Añade un mensaje al historial siguiendo el formato esperado por la API de Ollama
        self.mensajes.append({"role": rol, "content": contenido})

    def obtener_historial(self):
        # Devuelve la lista completa de mensajes para enviarla al modelo
        return self.mensajes

    def limpiar_historial(self):
        # Vacía el historial cuando se cambia de experto o se solicita un reinicio
        self.mensajes = []