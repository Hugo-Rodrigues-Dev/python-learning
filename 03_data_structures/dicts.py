# Dictionaries: key-value mappings (unordered, mutable)

# Creating dictionaries
person = {"name": "Alice", "age": 25}
scores = dict(math=90, physics=88)
empty = {}

print("person:", person)
print("scores:", scores)
print("empty:", empty)

# Accessing values
print("person['name']:", person["name"])  # raises KeyError if missing
print("person.get('city'):", person.get("city"))  # returns None if missing
print("person.get('city', 'Unknown'):", person.get("city", "Unknown"))

# Adding and updating
person["city"] = "Paris"  # add new key
person["age"] = 26  # update existing key
print("After add/update:", person)

# update() merges another mapping
person.update({"job": "Engineer", "age": 27})
print("After update():", person)

# Removing items
removed_age = person.pop("age")  # remove by key, return value
print("Removed age:", removed_age)
print("After pop('age'):", person)

last_key, last_value = person.popitem()  # remove and return an arbitrary last item
print("popitem ->", (last_key, last_value))
print("After popitem():", person)

del person["name"]  # delete key
print("After del person['name']:", person)

# Iteration
user = {"id": 101, "name": "Bob", "active": True}
print("Keys:", list(user.keys()))
print("Values:", list(user.values()))
print("Items:", list(user.items()))

print("Loop keys:")
for k in user:
    print(k)

print("Loop items:")
for k, v in user.items():
    print(k, "->", v)

print("Contains 'name'?:", "name" in user)

# Dict comprehension
nums = [1, 2, 3, 4]
square_map = {n: n * n for n in nums}
even_map = {n: (n % 2 == 0) for n in nums}
print("square_map:", square_map)
print("even_map:", even_map)

# Nested dictionaries and safe access
profile = {
    "username": "hugo",
    "stats": {"followers": 120, "following": 85},
}
print("profile:", profile)
followers = profile.get("stats", {}).get("followers", 0)
print("followers via get():", followers)

# setdefault: get a key or set it if missing
settings = {"theme": "dark"}
settings.setdefault("language", "en")
settings.setdefault("theme", "light")  # won't overwrite existing key
print("settings after setdefault:", settings)

# fromkeys: create dict with default value
keys = ["a", "b", "c"]
defaults = dict.fromkeys(keys, 0)
print("fromkeys:", defaults)

# Copy vs reference
original = {"x": 1}
alias = original
clone = original.copy()
original["x"] = 2
print("original:", original)
print("alias (same object):", alias)
print("clone (separate):", clone)

# Clearing a dictionary
tmp = {"k": 1, "v": 2}
tmp.clear()
print("After clear():", tmp)

