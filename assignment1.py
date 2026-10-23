
name = "Rehan"
age = 22
city = "Lahore"

skills = ["Python", "SQL", "Git"]

skills_string = "|".join(skills)

print(f"{name} | {age} | {city} | {skills_string}")





def check_eligibility(age, verified):
    if age >= 18 and verified:
        return "Eligible"
    else:
        return "Not eligible"


# Test cases
print(20, True, "->", check_eligibility(20, True))
print(17, True, "->", check_eligibility(17, True))
print(25, False, "->", check_eligibility(25, False))
print(18, True, "->", check_eligibility(18, True))





skills = ["Python", "python", " python ", "SQL", "excel", "git"]

# Remove extra spaces, convert to lowercase, remove duplicates, and sort
cleaned = sorted(set(skill.strip().lower() for skill in skills))

# Print each unique skill
for skill in cleaned:
    print("-", skill)

# Print the total number of unique skills
print("Unique skills:", len(cleaned))






import json

# Create a dictionary
record = {
    "customer_id": "C01",
    "name": "Ali Raza",
    "preferred_language": "Urdu",
    "active": True
}

# Convert dictionary to JSON string
text = json.dumps(record)

# Convert JSON string back to dictionary
parsed = json.loads(text)

# Print the JSON string and one parsed field
print(text)
print(parsed["preferred_language"])