contacs = {
    "Alice": "555-1234",
    "Bob": "555-5678",
    "Charlie": "555-9999"
}
print(f"Alice's number: {contacs["Alice"]}")
contacs["Diana"] = "555-4321"
print(f"Contact after adding Diana: {contacs}")
contacs["Bob"] = "555-0000"
print(f"Contacs after updating Bob: {contacs}")
del contacs["Charlie"]
print(f"Contacs after deleting Charlie: {contacs}")
print(f"All names {contacs.keys()}")
print(f"All numbers {contacs.values()}")
print(f"Total contacs {len(contacs)}")
