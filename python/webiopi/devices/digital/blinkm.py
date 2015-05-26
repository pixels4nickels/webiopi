from webiopi.devices.i2c import I2C
from webiopi.utils.types import toint

class BlinkM(BlinkMAPI):
    GO_TO_RGB = 0x6e
    GET_CURRENT_RGB = 0x67

    def __init__(self, slave=0x09):
        I2C.__init__(self, toint(slave))
        
    def __str__(self):
        return "BlinkM(slave=0x%02X)" % self.slave
        
    def __getRGB__(self, addr):
        return I2C.readRegister(self, addr, GET_CURRENT_RGB)

    def __setRGB__(self, addr, value):
        I2C.writeRegisters(self, addr, GO_TO_RGB)
        return I2C.writeRegisters(self, addr, value)
