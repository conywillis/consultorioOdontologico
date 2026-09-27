from collections import deque

from models.medical_appointment import MedicalAppointment
from models.pacient import Pacient
from utilities.constants import Constants

class customUtils:
    
    @staticmethod
    def validate_client_type(client_type):
        return client_type in Constants.CLIENT_TYPES

    @staticmethod
    def validate_attention_type(attention_type):
        return attention_type in Constants.ATTENTION_TYPES

    @staticmethod
    def validate_attention_priority(attention_priority):
        return attention_priority in Constants.ATTENTION_PRIORITY
    
    @staticmethod
    def validate_quantity(quantity):
        return isinstance(quantity, int) and quantity > 0
    
    @staticmethod
    def validate_quantity_by_attention_type(self, attention_type, quantity):
        if (attention_type == Constants.ATTENTION_TYPES[0] 
            or attention_type == Constants.ATTENTION_TYPES[3]):
            return self.validate_quantity(quantity) and quantity == 1
        
    @staticmethod
    def earliest_date(pacient):
                dates = [appointment.date for appointment in pacient.medical_appointments]
                return min(dates) if dates else "9999-99-99"
            
        
    def create_pacient(self, id_pacient, name, phone, client_type):
        if not id_pacient or not isinstance(id_pacient, int):
            raise ValueError(f"Cédula de paciente inválida: {id_pacient}")
        if not self.validate_client_type(client_type):
            raise ValueError(f"Tipo de cliente inválido: {client_type}")
        return Pacient(id_pacient, name, phone, client_type, deque())
    

    def get_patient_by_id(self, pacient_list, id_pacient):
        for pacient in pacient_list:
            if pacient.id_pacient == id_pacient:
                return pacient
        return None

    def create_medical_appointment(self, pacient_list, id_pacient, attention_type, quantity, attention_priority, date):
        pacient = self.get_patient_by_id(pacient_list, id_pacient)
        if not pacient:
            raise ValueError(f"Paciente no encontrado: {id_pacient}")
        if not self.validate_attention_type(attention_type):
            raise ValueError(f"Tipo de atención inválido: {attention_type}")
        if not self.validate_quantity(quantity):
            raise ValueError(f"Cantidad inválida: {quantity}")
        if not self.validate_attention_priority(attention_priority):
            raise ValueError(f"Prioridad de atención inválida: {attention_priority}")
        
        pacient.medical_appointments.append(MedicalAppointment(attention_type, quantity, attention_priority, date))

    def read_input_create_pacient(self, id_pacient_input):
        id_pacient = id_pacient_input
        name = input("Ingrese el nombre del paciente: ")
        phone = input("Ingrese el teléfono del paciente: ")
        client_type = input(f"Ingrese el tipo de cliente ({', '.join(Constants.CLIENT_TYPES)}): ")

        return self.create_pacient(id_pacient, name, phone, client_type)
    
    def print_menu(self):
        options = ["1. Agregar paciente", 
                "2. Buscar paciente por cédula y mostrar su información",
                "3. Asignar cita médica a un paciente",
                "4. Buscar todas las citas médicas de un paciente por cédula y mostrarlas",  
                "5. Ver pacientes ordenados por valor total a pagar (desc)", 
                "6. Salir"]
        print("=== Menú de Opciones ===")
        for option in options:
            print(option)
        option = input("Seleccione una opción: ")
        return option