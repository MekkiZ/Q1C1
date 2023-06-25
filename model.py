class Home:
    """Creat DATAS for best handling."""

    def __init__(self, property, building_id, owner_acquisition_date, street1, city, zip, lastname, firstname, email):
        self.property = property
        self.building_id = building_id
        self.owner_acquisition_date = owner_acquisition_date
        self.street1 = street1
        self.city = city
        self.zip = zip
        self.lastname = lastname
        self.firstname = firstname
        self.email = email

    def __str__(self):
        return f"{self.property}," \
               f" {self.building_id}," \
               f" {self.owner_acquisition_date}," \
               f" {self.street1}," \
               f" {self.city}," \
               f" {self.zip}," \
               f" {self.lastname}," \
               f" {self.firstname}," \
               f" {self.email}"

    def __repr__(self):
        return f"{self.property}," \
               f" {self.building_id}," \
               f" {self.owner_acquisition_date}," \
               f" {self.street1}," \
               f" {self.city}," \
               f" {self.zip}," \
               f" {self.lastname}," \
               f" {self.firstname}," \
               f" {self.email}"

    def __eq__(self, other):
        if isinstance(self, other.__class__):
            return self.property == other.property and self.building_id == other.building_id
        else:
            NotImplemented

    def __hash__(self):
        return hash(('property', self.property,
                     'building_id', self.building_id))

    def __getitem__(self, item):
        return f"{self.property[item]}" \
               f"{self.building_id[item]}" \
               f"{self.owner_acquisition_date[item]}" \
               f"{self.street1[item]}" \
               f"{self.city[item]}" \
               f"{self.zip[item]}" \
               f"{self.lastname[item]}" \
               f"{self.firstname[item]}" \
               f"{self.email[item]}"
