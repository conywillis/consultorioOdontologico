from models.pacient import Pacient
from dental_practice import DentalPractice


def main():
    practice = DentalPractice()

    pacients = [
        Pacient(1, "Carlos Ramirez", "3001234567", practice.client_types[0], practice.attention_types[0], 1, practice.attention_priority[1], "2026-09-28"),
        Pacient(2, "Laura Gomez", "3009876543", practice.client_types[1], practice.attention_types[1], 2, practice.attention_priority[0], "2026-09-29"),
        Pacient(3, "Andres Torres", "3005551234", practice.client_types[2], practice.attention_types[2], 1, practice.attention_priority[0], "2026-09-30"),
        Pacient(4, "Sofia Martinez", "3001112222", practice.client_types[0], practice.attention_types[3], 1, practice.attention_priority[1], "2026-10-01"),
    ]

    for pacient in pacients:
        total = practice.calculate_appointment_value(pacient)
        print(pacient)
        print(f"Valor total a pagar: {total}")
        print("-" * 60)


if __name__ == "__main__":
    main()
