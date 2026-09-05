print("===== HOSPITAL PATIENT APPOINTMENT SYSTEM =====")
patient_name = input("Enter patient name: ")

requested_input = input(
    "Enter requested departments separated by commas: "
)
requested_departments = [dept.strip() for dept in requested_input.split(",")]

previous_input = input(
    "Enter previously visited departments separated by commas: "
)
previous_departments = [dept.strip() for dept in previous_input.split(",")]

preferred_input = input(
    "Enter preferred doctors separated by commas: "
)
preferred_doctors = [doctor.strip() for doctor in preferred_input.split(",")]

available_input = input(
    "Enter available departments separated by commas: "
)
available_departments = [dept.strip() for dept in available_input.split(",")]

doctor_input = input(
    "Enter available doctors separated by commas: "
)
available_doctors = [doctor.strip() for doctor in doctor_input.split(",")]

emergency_input = input(
    "Enter emergency departments separated by commas: "
)
emergency_departments = [dept.strip() for dept in emergency_input.split(",")]
print("\n===== LIST OPERATIONS =====")
if requested_departments:
    print("First requested department:", requested_departments[0])
print("First two requested departments:", requested_departments[:2])
requested_copy = requested_departments.copy()
requested_copy.append("General Medicine")
print("After adding General Medicine:", requested_copy)
if "General Medicine" in requested_copy:
    requested_copy.remove("General Medicine")
print("After removing General Medicine:", requested_copy)
requested_set = set(requested_departments)
available_set = set(available_departments)
previous_set = set(previous_departments)
preferred_doctors_set = set(preferred_doctors)
available_doctors_set = set(available_doctors)
emergency_set = set(emergency_departments)
duplicate_requests = []

for dept in requested_departments:
    if requested_departments.count(dept) > 1:
        if dept not in duplicate_requests:
            duplicate_requests.append(dept)
common_departments = requested_set.intersection(available_set)
unavailable_departments = requested_set.difference(available_set)
previously_requested = requested_set.intersection(previous_set)
immediate_attention = requested_set.intersection(emergency_set)
all_related_departments = requested_set.union(
    available_set,
    previous_set,
    emergency_set
)
available_preferred_doctors = preferred_doctors_set.intersection(
    available_doctors_set
)
membership_results = []

for dept in requested_departments:
    if dept in available_set:
        membership_results.append(dept + " is available.")
    else:
        membership_results.append(dept + " is not available.")
all_requests_available = requested_set.issubset(available_set)
recommended_department = "No department available"

for dept in requested_departments:
    if dept in emergency_set and dept in available_set:
        recommended_department = dept
        break
if recommended_department == "No department available":
    for dept in requested_departments:
        if dept in available_set:
            recommended_department = dept
            break
if len(common_departments) == 0:
    appointment_status = "Appointment cannot be scheduled."

elif immediate_attention:
    appointment_status = "Emergency appointment requires immediate attention."

elif all_requests_available:
    appointment_status = "Appointment confirmed for all requested departments."

else:
    appointment_status = (
        "Appointment partially confirmed. "
        "Some requested departments are unavailable."
    )
print("\n" + "=" * 60)
print("           PATIENT APPOINTMENT REPORT")
print("=" * 60)

print("\nPatient Name:")
print(patient_name)

print("\nRequested Departments:")
print(requested_departments)

print("\nAvailable Departments:")
print(available_departments)

print("\nCommon Departments (Requested & Available):")
print(list(common_departments))

print("\nUnavailable Requested Departments:")
print(list(unavailable_departments))

print("\nDuplicate Department Requests:")
if duplicate_requests:
    print(duplicate_requests)
else:
    print("No duplicate requests.")

print("\nPreviously Visited Departments:")
print(previous_departments)

print("\nPreviously Visited & Requested Again:")
print(list(previously_requested))

print("\nEmergency Departments:")
print(emergency_departments)

print("\nRequested Departments Requiring Immediate Attention:")
if immediate_attention:
    print(list(immediate_attention))
else:
    print("None")

print("\nPreferred Doctors:")
print(preferred_doctors)

print("\nAvailable Doctors:")
print(available_doctors)

print("\nPreferred Doctors Currently Available:")
if available_preferred_doctors:
    print(list(available_preferred_doctors))
else:
    print("No preferred doctor is currently available.")

print("\nAll Related Departments (Union):")
print(list(all_related_departments))

print("\nMembership Checking:")
for result in membership_results:
    print("-", result)

print("\nAre all requested departments available?")
print(all_requests_available)

print("\nRecommended Department:")
print(recommended_department)

print("\nFinal Appointment Status:")
print(appointment_status)

print("\n" + "=" * 60)
print("                 END OF REPORT")
print("=" * 60)
