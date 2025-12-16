from pyscript import document, display

previous_data = {}

def general_weighted_average(e):
    global previous_data

    first_name = document.querySelector("#first_name").value.strip()
    last_name = document.querySelector("#last_name").value.strip()
    english = document.querySelector("#english").value.strip()
    filipino = document.querySelector("#filipino").value.strip()
    math = document.querySelector("#math").value.strip()
    geometry = document.querySelector("#geometry").value.strip()
    science = document.querySelector("#science").value.strip()
    ss = document.querySelector("#ss").value.strip()

    current_data = {
        "first_name": first_name,
        "last_name": last_name,
        "english": english,
        "filipino": filipino,
        "math": math,
        "geometry": geometry,
        "science": science,
        "ss": ss
    }

    if current_data == previous_data:
        return
    previous_data = current_data.copy()

    try:
        english = float(english)
        filipino = float(filipino)
        math = float(math)
        geometry = float(geometry)
        science = float(science)
        ss = float(ss)

        units = {
            "english": 5,
            "filipino": 3,
            "math": 5,
            "geometry": 4,
            "science": 4,
            "ss": 3
        }

        weighted_sum = (
            english * units["english"]
            + filipino * units["filipino"]
            + math * units["math"]
            + geometry * units["geometry"]
            + science * units["science"]
            + ss * units["ss"]
        )
        total_units = sum(units.values())
        gwa = weighted_sum / total_units

        summary = f"""
English: {english:.2f}
Filipino: {filipino:.2f}
Mathematics: {math:.2f}
Geometry: {geometry:.2f}
Science: {science:.2f}
Social Studies: {ss:.2f}
        """

        display(f"Name: {first_name} {last_name}", target="student_info")
        display(summary, target="summary")
        display(f"📊 General Weighted Average: {gwa:.2f}", target="output")

    except Exception:
        display("⚠️ Please enter valid numeric grades for all subjects.", target="output")