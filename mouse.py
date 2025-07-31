import serial
import pyautogui
import time

bluetooth_port = 'COM5'  # Cambia por tu puerto Bluetooth real
baud_rate = 9600

# Ajusta esta ganancia para controlar la sensibilidad del movimiento del cursor
sensitivity = 0.2

def main():
    try:
        ser = serial.Serial(bluetooth_port, baud_rate, timeout=1)
        print(f"Conectado a {bluetooth_port} a {baud_rate} baudios.")
        time.sleep(2)  # Espera a que el puerto esté listo
    except serial.SerialException as e:
        print(f"No se pudo abrir el puerto serial: {e}")
        return

    screenWidth, screenHeight = pyautogui.size()
    lastX, lastY = pyautogui.position()

    while True:
        line = ser.readline().decode('utf-8').strip()
        if line:
            try:
                moveX_str, moveY_str = line.split(':')

                moveX = float(moveX_str) * sensitivity
                moveY = float(moveY_str) * sensitivity

                # Calcula nueva posición del cursor
                newX = lastX + moveX
                newY = lastY - moveY  # eje Y invertido

                # Asegura que esté dentro de la pantalla
                newX = max(0, min(screenWidth - 1, newX))
                newY = max(0, min(screenHeight - 1, newY))

                pyautogui.moveTo(newX, newY)
                lastX, lastY = newX, newY

            except ValueError:
                print(f"Error parseando línea: {line}")

if __name__ == "__main__":
    main()
