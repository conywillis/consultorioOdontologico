class Pacient:
    def __init__(self, id_pacient, name, phone, client_type, attention_type, quanty, attention_priority, date):
        self.id_pacient = id_pacient
        self.name = name
        self.phone = phone
        self.client_type = client_type
        self.attention_type = attention_type
        self.quanty = quanty
        self.attention_priority = attention_priority
        self.date = date

    def __repr__(self):
        return (
            f"Pacient(id_pacient={self.id_pacient}, name={self.name}, "
            f"phone={self.phone}, client_type={self.client_type}, "
            f"attention_type={self.attention_type}, quanty={self.quanty}, "
            f"attention_priority={self.attention_priority}, date={self.date})"
        )