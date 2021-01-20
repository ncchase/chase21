import random, collections

class Statistics(object):
    def __init__(self):
        self.tags = collections.defaultdict(int)

    def account(self, tags):
        for tag in tags:
            self.tags[tag] += 1

    def tags_value(self, tags):
        return sum(1./self.tags[tag] for tag in tags)

    def most_disjoined(self, tags, groups):
        return max(
            groups.items(),
            key=lambda kv: (
                -self.tags_value(kv[0] & tags),
                len(kv[1]),
                self.tags_value(tags - kv[0]) - self.tags_value(kv[0] - tags),
            )
        )

def secret_santa(people_and_their_tags):
    """Secret santa algorithm.

    The lottery function expects a sequence of:
    (name, tags)

    For example:

    [
        ("person1", ("male", "company1")),
        ("person2", ("female", "company2")),
        ("person3", ("male", "company1")),
        ("husband1", ("male", "company2", "marriage1")),
        ("wife1", ("female", "company1", "marriage1")),
        ("husband2", ("male", "company3", "marriage2")),
        ("wife2", ("female", "company2", "marriage2")),
    ]
    The algorithm will try to match people with the least common characteristics
    between them, to maximize entrop— ehm, mingling!
    Have fun."""

    # let's split the persons into groups

    groups = collections.defaultdict(list)
    stats = Statistics()

    for person, tags in people_and_their_tags:
        tags = frozenset(tag.lower() for tag in tags)
        stats.account(tags)
        person= "%s [%s]" % (person, ",".join(tags))
        groups[tags].append(person)

    # shuffle all lists
    for group in groups.values():
        random.shuffle(group)

    output_chain = []
    prev_tags = frozenset()
    while 1:
        next_tags, next_group = stats.most_disjoined(prev_tags, groups)
        output_chain.append(next_group.pop())
        if not next_group:  # it just got empty
            del groups[next_tags]
            if not groups: break
        prev_tags = next_tags

    return output_chain

if __name__ == "__main__":
    example_sequence= [
    ("person1", ("A")),
    ("person2", ("B")),
    ("person3", ("C")),
    ("person4", ("A")),
    ("person5", ("A")),
    ("person6", ("C")),
    ("person7", ("C")),
]
    print("suggested chain (each person gives present to next person)")
    print(secret_santa(example_sequence))

