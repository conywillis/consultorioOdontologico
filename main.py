from models.pacient import Pacient
from models.medical_appointment import MedicalAppointment
from dental_practice import DentalPractice
from utilities.constants import Constants
from collections import deque

from utilities.custom_utils import customUtils

pacient_list = deque()
custom_utils = customUtils()
practice = DentalPractice()


def was_cancelled(value):
    if value is None:
        print("Operación cancelada. Volviendo al menú principal.")
        return True
    return False

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
        Pacient(1053001516, "Maria Rodriguez", "3005556666", Constants.CLIENT_TYPES[2], deque([
            MedicalAppointment(Constants.ATTENTION_TYPES[1], 1, Constants.ATTENTION_PRIORITY[1], "2026-10-03"),
        ])),
        Pacient(1053001718, "Pedro Sanchez", "3007778888", Constants.CLIENT_TYPES[0], deque([
            MedicalAppointment(Constants.ATTENTION_TYPES[2], 1, Constants.ATTENTION_PRIORITY[0], "2026-10-04"),
        ])),
        Pacient(1053001920, "Ana Torres", "3009990000", Constants.CLIENT_TYPES[1], deque([
            MedicalAppointment(Constants.ATTENTION_TYPES[3], 1, Constants.ATTENTION_PRIORITY[1], "2026-10-05"),
        ])),
        Pacient(1053002122, "Luis Fernandez", "3002223333", Constants.CLIENT_TYPES[2], deque([
            MedicalAppointment(Constants.ATTENTION_TYPES[0], 1, Constants.ATTENTION_PRIORITY[0], "2026-10-06"),
        ])),
    ])

    for pacient in pacient_list:
        print(f"Nombre: {pacient.name} con cédula número: {pacient.id_pacient}")
        for appointment in pacient.medical_appointments:
            total = practice.get_value_by_client_type_attention_type(
                pacient.client_type, appointment.attention_type, appointment.quantity
            )
            print(f"  Cita: {appointment.attention_type} el {appointment.date} -> Valor a pagar: {total}")
        print("-" * 60)
        
def run_menu():
    option = "0"
    while option != "11":
        option = custom_utils.print_menu()
        if option == "1":
            id_pacient = custom_utils.read_valid_cedula()
            if was_cancelled(id_pacient):
                continue
            pacient = custom_utils.get_patient_by_id(pacient_list, id_pacient)
            if not pacient:
                try:
                    pacient = custom_utils.read_input_create_pacient(id_pacient)
                    if was_cancelled(pacient):
                        continue
                    pacient_list.append(pacient)
                    print(f"Paciente {pacient.name} agregado exitosamente.")
                except ValueError as e:
                    print(f"No se pudo agregar el paciente: {e}")
            else:
                print(f"El paciente ya existe: {pacient.name} (ID: {pacient.id_pacient}, "
                    f"teléfono: {pacient.phone}, tipo de cliente: {pacient.client_type})")
        elif option == "2":
            id_pacient = custom_utils.read_valid_cedula()
            if was_cancelled(id_pacient):
                continue
            pacient = custom_utils.get_patient_by_id(pacient_list, id_pacient)
            if pacient:
                print(f"Nombre: {pacient.name} con cédula número: {pacient.id_pacient} "
                    f"teléfono: {pacient.phone} tipo de cliente: {pacient.client_type}")
            else:
                print(f"Paciente no encontrado: {id_pacient}")
        elif option == "3":
            id_pacient = custom_utils.read_valid_cedula()
            if was_cancelled(id_pacient):
                continue
            attention_type = custom_utils.read_valid_choice("Ingrese el tipo de atención", Constants.ATTENTION_TYPES)
            if was_cancelled(attention_type):
                continue
            quantity = custom_utils.read_valid_quantity(attention_type)
            if was_cancelled(quantity):
                continue
            attention_priority = custom_utils.read_valid_choice("Ingrese la prioridad de atención", Constants.ATTENTION_PRIORITY)
            if was_cancelled(attention_priority):
                continue
            date = custom_utils.read_valid_date()
            if was_cancelled(date):
                continue
            try:
                custom_utils.create_medical_appointment(
                    pacient_list, id_pacient, attention_type, quantity, attention_priority, date
                )
                pacient = custom_utils.get_patient_by_id(pacient_list, id_pacient)
                total = practice.get_value_by_client_type_attention_type(pacient.client_type, attention_type, quantity)
                print(f"Cita médica asignada exitosamente. Valor a pagar por esta cita: {total}")
            except ValueError as e:
                print(f"No se pudo asignar la cita: {e}")
        elif option == "4":
            id_pacient = custom_utils.read_valid_cedula()
            if was_cancelled(id_pacient):
                continue
            pacient = custom_utils.get_patient_by_id(pacient_list, id_pacient)
            if pacient:
                total = practice.calculate_appointment_value(pacient)
                print(f"El usuario {pacient.name} tiene {len(pacient.medical_appointments)} citas asignadas "
                    f"y su valor total a pagar es {total}")
                for appointment in pacient.medical_appointments:
                    valor_cita = practice.get_value_by_client_type_attention_type(
                        pacient.client_type, appointment.attention_type, appointment.quantity
                    )
                    print(f"  Cita de {appointment.attention_type} el {appointment.date}, "
                        f"cantidad: {appointment.quantity}, prioridad: {appointment.attention_priority} -> Valor: {valor_cita}")
            else:
                print(f"Paciente no encontrado: {id_pacient}")
        elif option == "5":
            sorted_pacients = practice.sort_pacients_by_total_value(pacient_list)
            for pacient in sorted_pacients:
                total = practice.calculate_appointment_value(pacient)
                print(f"Nombre: {pacient.name} con cédula número: {pacient.id_pacient} valor total: {total}")
        elif option == "6":
            total_revenue = practice.calculate_total_revenue(pacient_list)
            print(f"Ingresos totales recibidos: {total_revenue}")
        elif option == "7":
            count = practice.count_pacients_by_attention_type(pacient_list, Constants.ATTENTION_TYPES[2])
            print(f"Número de clientes que van para extracción de dientes: {count}")
        elif option == "8":
            print(f"Total de clientes: {len(pacient_list)}")
        elif option == "9":
            sorted_pacients = practice.sort_pacients_by_total_value(pacient_list)
            print("=== Clientes ordenados por valor a pagar (desc) ===")
            for pacient in sorted_pacients:
                print(f"Nombre: {pacient.name} - Cédula: {pacient.id_pacient}")
            id_pacient = custom_utils.read_valid_cedula("Ingrese la cédula del paciente a buscar en la lista ordenada")
            if was_cancelled(id_pacient):
                continue
            pacient = None
            posicion = None
            for indice, candidato in enumerate(sorted_pacients, start=1):
                if candidato.id_pacient == id_pacient:
                    pacient = candidato
                    posicion = indice
                    break
            if pacient:
                total = practice.calculate_appointment_value(pacient)
                print(f"Encontrado en la posición {posicion} de {len(sorted_pacients)}: "
                    f"Nombre: {pacient.name} valor total: {total}")
            else:
                print(f"Paciente no encontrado en la lista ordenada: {id_pacient}")
        elif option == "10":
            sorted_by_date = practice.sort_pacients_by_date(pacient_list)
            for pacient in sorted_by_date:
                fecha = customUtils.earliest_date(pacient)
                print(f"Nombre: {pacient.name} con cédula número: {pacient.id_pacient} "
                    f"- Fecha de la cita: {fecha}")
        elif option == "11":
            print("Saliendo del programa...")
            return
def main():
    run_sample_data()
    run_menu()

if __name__ == "__main__":
    main()

# Hallazgos:
# 1. No se válida la fecha en el pasado
# 2. La fecha no tiene la hora, debería tener la hora porque es cita médica
# 3. No valida que la opción del menú sea correcta, si el usuario ingresa un número que no está en el menú, debería mostrar un mensaje de error y volver a mostrar el menú.
# 4. Se están mostrando los sample data. La sample data no debería mostrarse
# 5. El tipo de antención es case sensitive
# 6. Cuando el paciente no tiene citas, aparece en la opcion 10 con fecha de cita 9999-99-99