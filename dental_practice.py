from models.medical_appointment import MedicalAppointment


class DentalPractice:
    client_types = ["Particular", "EPS", "Prepagada"]
    attention_types = ["Limpieza", "Calza", "Extracción", "Diagnóstico"]
    attention_priority = ["Normal", "Urgente"]
    
    particular_cleaning= MedicalAppointment(client_types[0], attention_types[0], 80000, 60000)
    particular_calza= MedicalAppointment(client_types[0], attention_types[1], 80000, 80000)
    particular_extraction= MedicalAppointment(client_types[0], attention_types[2], 80000, 100000)
    particular_diagnosis= MedicalAppointment(client_types[0], attention_types[3], 80000, 50000)
    
    eps_cleaning= MedicalAppointment(client_types[1], attention_types[0], 5000, 0)
    eps_calza= MedicalAppointment(client_types[1], attention_types[1], 5000, 40000)
    eps_extraction= MedicalAppointment(client_types[1], attention_types[2], 5000, 40000)
    eps_diagnosis= MedicalAppointment(client_types[1], attention_types[3], 5000, 0)
    
    prepaid_cleaning= MedicalAppointment(client_types[2], attention_types[0], 30000, 0)
    prepaid_calza= MedicalAppointment(client_types[2], attention_types[1], 30000, 10000)
    prepaid_extraction= MedicalAppointment(client_types[2], attention_types[2], 30000, 10000)
    prepaid_diagnosis= MedicalAppointment(client_types[2], attention_types[3], 30000, 0)
    
    medical_appointments = [
        particular_cleaning,
        particular_calza,
        particular_extraction,
        particular_diagnosis,
        eps_cleaning,
        eps_calza,
        eps_extraction,
        eps_diagnosis,
        prepaid_cleaning,
        prepaid_calza,
        prepaid_extraction,
        prepaid_diagnosis
    ]
    
    def get_value_by_client_type_attention_type(self, client_type, attention_type, quantity):
            total_value = 0
            for appointment in self.medical_appointments:
                if appointment.client_type == client_type and appointment.attention_type == attention_type:
                    total_value += appointment.appointment_value + (appointment.attention_value * quantity)
                    break
            return total_value

    def calculate_appointment_value(self, pacient):
        total_value = self.get_value_by_client_type_attention_type(pacient.client_type, pacient.attention_type, pacient.quantity)
        return total_value