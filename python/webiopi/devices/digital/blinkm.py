from webiopi.devices.i2c import I2C
from webiopi.utils.types import toint
from webiopi.decorators.rest import request, response

class BlinkM(I2C):
    GO_TO_RGB = 0x6e
    GET_CURRENT_RGB = 0x67
    STOP_SCRIPT = 0x6f

    def __init__(self, slave=0x0a):
        I2C.__init__(self, toint(slave))
        I2C.writeRegister(self, self.slave, self.STOP_SCRIPT)

    def __str__(self):
        return "BlinkM(slave=0x%02X)" % self.slave

    def __family__(self):
        return "BlinkM"

    @request("GET", "rgb")
    @response("%d,%d,%d")
    def getRGB(self):
        I2C.writeRegister(self, self.slave, self.GET_CURRENT_RGB)
        r, g, b = I2C.readRegisters(self, self.slave, 3)
        return r, g, b

    @request("GET", "rgb/%(value)d")
    @response("%d,%d,%d")
    def setRGB(self, value):
        r = (value>>16) & 0xff
        g = (value>>8) & 0xff
        b = value & 0xff
        I2C.writeRegisters(self, self.slave, bytes([self.GO_TO_RGB, r, g, b]))
        return r, g, b
