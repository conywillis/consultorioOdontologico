from collections import deque
from datetime import datetime

from models.medical_appointment import MedicalAppointment
from models.pacient import Pacient
from utilities.constants import Constants

class customUtils:

    CANCEL_KEYWORDS = {"cancelar", "c"}

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
    def validate_quantity_by_attention_type(attention_type, quantity):
        if not customUtils.validate_quantity(quantity):
            return False
        if (attention_type == Constants.ATTENTION_TYPES[0]
            or attention_type == Constants.ATTENTION_TYPES[3]):
            return quantity == 1
        return True
        
    @staticmethod
    def _read_until_valid(prompt, is_valid, error_message):
        value = input(f"{prompt}: ").strip()
        while value.lower() not in customUtils.CANCEL_KEYWORDS and not is_valid(value):
            value = input(f"{error_message}. Ingrese un valor válido o escriba 'Cancelar' "
                          f"para volver al menú principal: ").strip()
        if value.lower() in customUtils.CANCEL_KEYWORDS:
            return None
        return value

    @staticmethod
    def read_valid_cedula(prompt="Ingrese la cédula del paciente"):
        value = customUtils._read_until_valid(
            prompt, str.isdigit, "Cédula inválida, debe contener solo números"
        )
        return int(value) if value is not None else None

    @staticmethod
    def read_valid_quantity(attention_type, prompt="Ingrese la cantidad"):
        if attention_type in (Constants.ATTENTION_TYPES[0], Constants.ATTENTION_TYPES[3]):
            error_message = f"Cantidad inválida, para {attention_type} la cantidad debe ser exactamente 1"
        else:
            error_message = "Cantidad inválida, debe ser un número entero mayor que cero"
        value = customUtils._read_until_valid(
            prompt,
            lambda v: v.isdigit() and customUtils.validate_quantity_by_attention_type(attention_type, int(v)),
            error_message
        )
        return int(value) if value is not None else None

    @staticmethod
    def read_valid_date(prompt="Ingrese la fecha (YYYY-MM-DD)"):
        def is_valid_date(value):
            try:
                datetime.strptime(value, "%Y-%m-%d")
                return True
            except ValueError:
                return False

        return customUtils._read_until_valid(
            prompt, is_valid_date, "Fecha inválida, use el formato YYYY-MM-DD (ejemplo: 2026-10-05)"
        )

    @staticmethod
    def read_valid_name(prompt="Ingrese el nombre del paciente"):
        return customUtils._read_until_valid(
            prompt, lambda v: v.replace(" ", "").isalpha(), "Nombre inválido, debe contener solo letras"
        )

    @staticmethod
    def read_valid_phone(prompt="Ingrese el teléfono del paciente"):
        return customUtils._read_until_valid(
            prompt, str.isdigit, "Teléfono inválido, debe contener solo números"
        )

    @staticmethod
    def read_valid_choice(prompt, valid_options):
        options_text = ', '.join(valid_options)
        return customUtils._read_until_valid(
            f"{prompt} ({options_text})",
            lambda v: v in valid_options,
            f"Valor inválido, las opciones válidas son: {options_text}"
        )

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
        if not self.validate_quantity_by_attention_type(attention_type, quantity):
            raise ValueError(f"Cantidad inválida para el tipo de atención {attention_type}: {quantity}")
        if not self.validate_attention_priority(attention_priority):
            raise ValueError(f"Prioridad de atención inválida: {attention_priority}")
        
        pacient.medical_appointments.append(MedicalAppointment(attention_type, quantity, attention_priority, date))

    def read_input_create_pacient(self, id_pacient_input):
        name = self.read_valid_name()
        if name is None:
            return None
        phone = self.read_valid_phone()
        if phone is None:
            return None
        client_type = self.read_valid_choice("Ingrese el tipo de cliente", Constants.CLIENT_TYPES)
        if client_type is None:
            return None

        return self.create_pacient(id_pacient_input, name, phone, client_type)
    
    def print_menu(self):
        options = ["1. Agregar paciente",
                "2. Buscar paciente por cédula y mostrar su información",
                "3. Asignar cita médica a un paciente",
                "4. Buscar todas las citas médicas de un paciente por cédula y mostrarlas",
                "5. Ver pacientes ordenados por valor total a pagar (desc)",
                "6. Ver ingresos totales recibidos",
                "7. Ver número de clientes que van para extracción de dientes",
                "8. Ver total de clientes",
                "9. Ordenar clientes por valor y buscar uno por cédula",
                "10. Ver pacientes ordenados por Fecha de la cita",
                "11. Salir"]
        print("=== Menú de Opciones ===")
        for option in options:
            print(option)
        option = input("Seleccione una opción: ")
        return option