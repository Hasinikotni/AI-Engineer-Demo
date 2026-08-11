from rapidfuzz import fuzz


def normalize_name(name):
    name = name.lower()

    replacements = {
        "incorporated": "inc",
        "corporation": "corp",
        "limited": "ltd",
        "company": "co",
    }

    words = name.replace(".", "").split()

    words = [replacements.get(word, word) for word in words]

    return " ".join(words)


def calculate_similarity(name1, name2):
    name1 = normalize_name(name1)
    name2 = normalize_name(name2)

    return fuzz.ratio(name1, name2)


def is_same_entity(name1, name2, threshold=80):
    score = calculate_similarity(name1, name2)

    return score >= threshold


if __name__ == "__main__":

    name1 = input("Name 1: ")
    name2 = input("Name 2: ")

    score = calculate_similarity(name1, name2)
    same = is_same_entity(name1, name2)

    print("Normalized Name 1:", normalize_name(name1))
    print("Normalized Name 2:", normalize_name(name2))
    print("Similarity:", score)
    print("Same Entity:", same)