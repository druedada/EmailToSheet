import os
import gspread
from dotenv import load_dotenv

# Cargar las variables definidas en el .env
load_dotenv()

spreadsheet_id = os.getenv("GOOGLE_SPREADSHEET_ID")
credentials_file = os.getenv("GOOGLE_APPLICATION_CREDENTIALS")

def probar_conexion():
    try:
        print("🔐 Autenticando con Google Cloud Service Account...")
        # gspread usa automáticamente las credenciales del archivo JSON
        gc = gspread.service_account(filename=credentials_file)

        print("📊 Abriendo la hoja de Google Sheets por ID...")
        sh = gc.open_by_key(spreadsheet_id)
        worksheet = sh.sheet1

        print("✍️ Escribiendo fila de prueba...")
        worksheet.append_row(["Test Autenticación", "OK", "Conexión Exitosa"])
        
        print("✅ ¡Éxito! La autenticación y la conexión con la hoja funcionan perfectamente.")

    except Exception as e:
        print(f"❌ Error durante la conexión: {e}")

if __name__ == "__main__":
    probar_conexion()