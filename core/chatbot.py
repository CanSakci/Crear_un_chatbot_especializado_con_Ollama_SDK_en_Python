import ollama
from core.conversation import HistorialConversacion
from experts.expert_prompts import PROMPTS_EXPERTOS

class ChatbotExpertos:
    """Clase principal que maneja la conexión offline con Ollama y la lógica del chat."""
    
    def __init__(self, modelo="gemma3:1b"):
        # Configuración inicial del modelo local
        self.modelo = modelo
        self.historial = HistorialConversacion()
        self.experto_actual = None

    def establecer_experto(self, clave_experto):
        # Valida que el experto exista, limpia el contexto anterior y aplica el nuevo prompt de sistema
        if clave_experto in PROMPTS_EXPERTOS:
            self.experto_actual = clave_experto
            self.historial.limpiar_historial()
            
            # El mensaje de rol "system" condiciona el comportamiento del modelo local
            prompt_sistema = PROMPTS_EXPERTOS[clave_experto]
            self.historial.agregar_mensaje("system", prompt_sistema)
            return True
        return False

    def enviar_mensaje(self, mensaje_usuario):
        # Se añade lo que el usuario ha escrito al historial
        self.historial.agregar_mensaje("user", mensaje_usuario)

        try:
            # Conexión local a través del SDK de Ollama usando el historial completo
            respuesta = ollama.chat(
                model=self.modelo,
                messages=self.historial.obtener_historial()
            )
            
            # Extracción del texto generado por el modelo
            contenido_respuesta = respuesta['message']['content']
            
            # Se guarda la respuesta del asistente para conservar la coherencia en futuros mensajes
            self.historial.agregar_mensaje("assistant", contenido_respuesta)
            return contenido_respuesta

        except ollama.ResponseError as e:
            # Manejo de error específico si el modelo no está disponible o no se ha descargado
            return f"[ERROR DEL MODELO]: {str(e)}. ¿Ejecutaste 'ollama pull {self.modelo}' en la terminal?"
            
        except Exception as e:
            # Manejo de error general (por ejemplo, si el servicio de Ollama no se está ejecutando)
            return f"[ERROR DE CONEXIÓN]: {str(e)}. Asegúrate de que Ollama se esté ejecutando localmente con 'ollama serve'."