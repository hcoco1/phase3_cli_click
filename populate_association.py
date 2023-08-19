from sqlalchemy import Table, Column, Integer, ForeignKey, text
from termcolor import colored
from helpers import Session  # Assuming you have the Session class defined in lib.helpers
from db.models import association_table 

def populate_city_facility_association(values_list):
    """Populate the association table between cities and facilities."""
    sql = text(
        "INSERT INTO CityFacilityAssociation (city_id, facility_id) VALUES (:city_id, :facility_id)"
    )

    with Session() as session:
        try:
            # Use bulk insert mechanism for better performance
            session.execute(
                sql,
                [
                    {"city_id": city_id, "facility_id": facility_id}
                    for city_id, facility_id in values_list
                ],
            )
            session.commit()
            print(colored("Association data populated successfully.", "green"))
        except Exception as e:
            session.rollback()
            print(
                colored(
                    f"Error occurred while populating CityFacilityAssociation: {e}",
                    "red",
                )
            )


if __name__ == "__main__":
    # Define the values_list here or load it from wherever you want
    values_list = [
    (1, 1),
    (1, 2),
    (1, 3),
    (1, 4),
    (1, 5),
    (1, 6),
    (1, 7),
    (1, 8),
    (1, 9),
    (1, 10),
    (2, 1),
    (2, 2),
    (2, 3),
    (2, 4),
    (2, 5),
    (2, 6),
    (2, 7),
    (2, 8),
    (2, 9),
    (2, 10),
    (3, 1),
    (3, 2),
    (3, 3),
    (3, 4),
    (3, 5),
    (3, 6),
    (3, 7),
    (3, 8),
    (3, 9),
    (3, 10),
    (4, 1),
    (4, 2),
    (4, 3),
    (4, 4),
    (4, 5),
    (4, 6),
    (4, 7),
    (4, 8),
    (4, 9),
    (4, 10),
    (5, 1),
    (5, 2),
    (5, 3),
    (5, 4),
    (5, 5),
    (5, 6),
    (5, 7),
    (5, 8),
    (5, 9),
    (5, 10),
    (6, 1),
    (6, 2),
    (6, 3),
    (6, 4),
    (6, 5),
    (6, 6),
    (6, 7),
    (6, 8),
    (6, 9),
    (6, 10),
    (7, 1),
    (7, 2),
    (7, 3),
    (7, 4),
    (7, 5),
    (7, 6),
    (7, 7),
    (7, 8),
    (7, 9),
    (7, 10),
    (8, 1),
    (8, 2),
    (8, 3),
    (8, 4),
    (8, 5),
    (8, 6),
    (8, 7),
    (8, 8),
    (8, 9),
    (8, 10),
    (9, 1),
    (9, 2),
    (9, 3),
    (9, 4),
    (9, 5),
    (9, 6),
    (9, 7),
    (9, 8),
    (9, 9),
    (9, 10),
]  # Example values
    populate_city_facility_association(values_list)
