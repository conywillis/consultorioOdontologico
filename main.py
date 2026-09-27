from models.pacient import Pacient
from models.medical_appointment import MedicalAppointment
from dental_practice import DentalPractice
from utilities.constants import Constants
from collections import deque

from utilities.custom_utils import customUtils

pacient_list = deque()
custom_utils = customUtils()
practice = DentalPractice()

def run_sample_data():

    pacient_list.extend([
        Pacient(1053000123, "Carlos Ramirez", "3001234567", Constants.CLIENT_TYPES[0], deque([
            MedicalAppointment(Constants.ATTENTION_TYPES[0], 1, Constants.ATTENTION_PRIORITY[1], "2026-09-28"),
        ])),
        Pacient(1053000456, "Laura Gomez", "3009876543", Constants.CLIENT_TYPES[1], deque([
            MedicalAppointment(Constants.ATTENTION_TYPES[1], 2, Constants.ATTENTION_PRIORITY[0], "2026-09-29"),
        ])),
        Pacient(1053000789, "Andres Torres", "3005551234", Constants.CLIENT_TYPES[2], deque([
            MedicalAppointment(Constants.ATTENTION_TYPES[2], 1, Constants.ATTENTION_PRIORITY[0], "2026-09-30"),
        ])),
        Pacient(1053001012, "Sofia Martinez", "3001112222", Constants.CLIENT_TYPES[0], deque([
            MedicalAppointment(Constants.ATTENTION_TYPES[3], 1, Constants.ATTENTION_PRIORITY[1], "2026-10-01"),
        ])),
        Pacient(1053001314, "Juan Perez", "3003334444", Constants.CLIENT_TYPES[1], deque([
            MedicalAppointment(Constants.ATTENTION_TYPES[0], 1, Constants.ATTENTION_PRIORITY[0], "2026-10-02"),
        ])),
    ])

    for pacient in pacient_list:
        print(f"Nombre: {pacient.name} con Cédula número: {pacient.id_pacient}")
        for appointment in pacient.medical_appointments:
            total = practice.get_value_by_client_type_attention_type(
                pacient.client_type, appointment.attention_type, appointment.quantity
            )
            print(f"  Cita: {appointment.attention_type} el {appointment.date} -> Valor a pagar: {total}")
        print("-" * 60)
        
def run_menu():
    option = "0"
    while option != "6":
        option = custom_utils.print_menu()
        if option == "1":
            id_pacient = int(input("Ingrese la cédula del paciente: "))
            pacient = custom_utils.get_patient_by_id(pacient_list, id_pacient)
            if not pacient:
                pacient = custom_utils.read_input_create_pacient(id_pacient)
                pacient_list.append(pacient)
                print(f"Paciente {pacient.name} agregado exitosamente.")
            else:
                print(f"El paciente ya existe: {pacient.name} (ID: {pacient.id_pacient}, "
                    f"teléfono: {pacient.phone}, tipo de cliente: {pacient.client_type})")
        elif option == "2":
            id_pacient = int(input("Ingrese la cédula del paciente: "))
            pacient = custom_utils.get_patient_by_id(pacient_list, id_pacient)
            if pacient:
                print(f"Nombre: {pacient.name} con Cédula número: {pacient.id_pacient} "
                    f"teléfono: {pacient.phone} tipo de cliente: {pacient.client_type}")
            else:
                print(f"Paciente no encontrado: {id_pacient}")
        elif option == "3":
            id_pacient = int(input("Ingrese la cédula del paciente: "))
            attention_type = input(f"Ingrese el tipo de atención ({', '.join(Constants.ATTENTION_TYPES)}): ")
            quantity = int(input("Ingrese la cantidad: "))
            attention_priority = input(f"Ingrese la prioridad de atención ({', '.join(Constants.ATTENTION_PRIORITY)}): ")
            date = input("Ingrese la fecha (YYYY-MM-DD): ")
            custom_utils.create_medical_appointment(
                pacient_list, id_pacient, attention_type, quantity, attention_priority, date
            )
            print("Cita médica asignada exitosamente.")
        elif option == "4":
            id_pacient = int(input("Ingrese la cédula del paciente: "))
            pacient = custom_utils.get_patient_by_id(pacient_list, id_pacient)
            if pacient:
                for appointment in pacient.medical_appointments:
                    print(appointment)
            else:
                print(f"Paciente no encontrado: {id_pacient}")
        elif option == "5":
            sorted_pacients = practice.sort_pacients_by_total_value(pacient_list)
            for pacient in sorted_pacients:
                total = practice.calculate_appointment_value(pacient)
                print(f"Nombre: {pacient.name} con Cédula número: {pacient.id_pacient} valor total: {total}")
        elif option == "6":
            print("Saliendo del programa...")
            return
def main():
    run_sample_data()
    run_menu()

if __name__ == "__main__":
    main()
