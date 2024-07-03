from prescription_data import *

trail_patients = ["Denise", "Eddie", "Frank", "Georgia", "Kenny"]

# Remove warfarin and add Edoxaban
for patient in trail_patients:
    prescription = patients[patient]
    if warfarin in prescription:
        prescription.remove(warfarin)
        prescription.add(edoxaban)
    else:
        print(f"Patient {patient} is not taking warfarin."
              f" Please remove {patient} from the trail")
    print(patient, prescription)
