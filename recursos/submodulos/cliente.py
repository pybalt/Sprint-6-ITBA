# Class CLIENTE
#! Mi idea seria que en la ejecucion del script sql podamos introducir una instancia de la clase cliente y
#! La misma tenga predefinidas los campos a introducirse en su respectiva tabla
class Cliente():
    def __init__(self,
                dictionary):
        self.numeroCliente = dictionary['numeroCliente']
        self.nombre = dictionary['nombre']
        self.apellido = dictionary['apellido']
        self.dni = dictionary['dni']
        self.tipoCliente = dictionary['tipoCliente']
        self.calle = dictionary['direccion']['calle']
        self.numeroCalle = dictionary['direccion']['numeroCalle']
        self.ciudad = dictionary['direccion']['ciudad']
        self.provincia = dictionary['direccion']['provincia']
        self.pais = dictionary['direccion']['pais']
        self.transacciones = dictionary['transacciones']
        if self.tipoCliente== 'BLACK':
            self.tarjeta_de_credito=True
            self.limite_tarjetas_de_credito=5
            self.tarjeta_de_debito=False
            self.limite_tarjetas_de_debito=False
            self.chequeras=True
            self.maximo_chequeras=2
            self.maximo_retiro_diario=100000
            self.comision_transferencias=1 #Valor transferencia * comision(1) = Transferencia
            self.cuenta_corriente=True
            self.cuenta_corriente_descubierto=10000
            self.maximo_valor_transferencia=False
            self.caja_de_ahorro_en_dolares=True
            self.caja_de_ahorro_en_pesos=True
        if self.tipoCliente== 'GOLD':
            self.tarjeta_de_credito=True
            self.limite_tarjetas_de_credito=1
            self.tarjeta_de_debito=True
            self.limite_tarjetas_de_debito=1
            self.chequeras=True
            self.maximo_chequeras=1
            self.maximo_retiro_diario=20000
            self.comision_transferencias=0.995 #Valor transferencia * comision(0.995) = Transferencia - 0.5%
            self.cuenta_corriente=True
            self.cuenta_corriente_descubierto=10000
            self.maximo_valor_transferencia=500000
            self.caja_de_ahorro_en_dolares=True
            self.caja_de_ahorro_en_pesos=False
        if self.tipoCliente== 'CLASSIC':
            self.tarjeta_de_credito=False
            self.limite_tarjetas_de_credito=False
            self.tarjeta_de_debito=True
            self.limite_tarjetas_de_debito=1
            self.chequeras=False
            self.maximo_chequeras=False
            self.maximo_retiro_diario=10000
            self.comision_transferencias=0.99 #Valor transferencia * comision(0.99) = Transferencia - 1%
            self.maximo_valor_transferencia=150000
            self.cuenta_corriente=True
            self.cuenta_corriente_descubierto=False
            self.caja_de_ahorro_en_dolares=False
            self.caja_de_ahorro_en_pesos=True

            #* Aca se podria usar un decorador classmethod que cree una clase por cada obj dentro del json. 

    def __repr__(self) -> str:
        return f'{self.nombre} {self.apellido}'