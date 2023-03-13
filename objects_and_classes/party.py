class Party:
    def __init__(self):
        self.people = []


the_coolest_party = Party()

member = input()
while member != "End":
    the_coolest_party.people.append(member)
    member = input()

result = ", ".join(the_coolest_party.people)
print(f"Going: {result}")
print(f"Total: {len(the_coolest_party.people)}")

