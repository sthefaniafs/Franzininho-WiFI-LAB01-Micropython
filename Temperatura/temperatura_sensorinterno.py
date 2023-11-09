import esp32
from machine import Pin, SoftI2C
import ssd1306

# Franzininho Pin assignment 
i2c = SoftI2C(scl=Pin(9), sda=Pin(8))

oled_width = 128
oled_height = 64
oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c)

temp= esp32.raw_temperature() # read the internal temperature of the MCU, in Fahrenheit
esp32.ULP()             # access to the Ultra-Low-Power Co-processor

oled.text('Temperatura: ', 0, 0)
oled.text(temp, 20, 0)
oled.text('Hello, World 3!', 0, 40)
        
oled.show()