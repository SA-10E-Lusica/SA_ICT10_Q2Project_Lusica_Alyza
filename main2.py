from pyscript import document, display

club_info = {
"chess": {
"name": "Chess Club",
"description": "A club for chess enthusiasts of all skill levels.",
"meeting_time": "Every Wednesday/3:30-5:00 PM",
"location": "Room 405",
"moderator": "Mr. Santos",
"members": 20,
"category": "Academic"
},
"dance": {
"name": "Dance Club",
"description": "For students interested in various dance styles and performances.",
"meeting_time": "Every Tuesday and Thursday/4:00-6:00 PM",
"location": "Dance Studio",
"moderator": "Mr. Sumaoang",
"members": 18,
"category": "Non-Academic"
},
"robot": {
"name": "Robotics Club",
"description": "Design, build, and program robots for competitions.",
"meeting_time": "Every Tuesday/3:45-5:30 PM",
"location": "Computer Lab",
"moderator": "Ms. Onofre",
"members": 18,
"category": "Academic"
},
"art": {
"name": "Art Club",
"description": "Explore various art mediums and techniques.",
"meeting_time": "Every Wednesday/3:45-5:15 PM",
"location": "Art Room",
"moderator": "Mr. Llanes",
"members": 20,
"category": "Non-Academic"
},
"badminton": {
"name": "Badminton Club",
"description": "Practice and compete in badminton tournaments.",
"meeting_time": "Every Monday/4:00-5:30 PM",
"location": "Gymnasium",
"moderator": "Mr. Deocareza",
"members": 15,
"category": "Non-Academic"
},
"bball": {
"name": "Basketball Club",
"description": "Train and compete in school basketball leagues.",
"meeting_time": "Every Wednesday/4:00-6:00 PM",
"location": "Gymnasium",
"moderator": "Mr. Mariano",
"members": 20,
"category": "Non-Academic"
},
"glee": {
"name": "Glee Club",
"description": "Singing, music, and performances for students.",
"meeting_time": "Every Thursday/3:30-5:30 PM",
"location": "Music Room",
"moderator": "Ms. Llanes",
"members": 18,
"category": "Non-Academic"
},
"vball": {
"name": "Volleyball Club",
"description": "Practice and compete in school volleyball games.",
"meeting_time": "Every Tuesday/3:30-5:00 PM",
"location": "Gymnasium",
"moderator": "Ms. Addams",
"members": 16,
"category": "Non-Academic"
},
"": {
"name": "",
"description": "",
"meeting_time": "",
"location": "",
"moderator": "",
"members": "",
"category": ""
}
}

def show_club_info(e):
    document.getElementById('club-info').innerHTML = ""
    selected_club = document.getElementById("club-select").value
    info = club_info.get(selected_club, club_info[""])
    
    if not info["name"]:
        display("⚠️ Please select a club.", target="club-info")
        return

    output = f"""
Name: {info['name']}
Description: {info['description']}
Meeting Time: {info['meeting_time']}
Location: {info['location']}
Moderator: {info['moderator']}
Number of Members: {info['members']}
Category: {info['category']}
    """
    display(output, target="club-info")