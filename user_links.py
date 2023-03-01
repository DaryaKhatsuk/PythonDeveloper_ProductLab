# Часть №1
# Дан массив связей пользователей. Вам необходимо реализовать функцию, которая принимает на вход три аргумента:
# информация о связях, как кортеж (tuple)  кортежей, первое имя (str), второе имя (str). Функция должна возвращать True,
# если связь между любыми двумя заданными пользователями существует, например, если у двух пользователей есть общие
# друзья или у их друзей есть общие друзья и т.д., иначе  False.

def check_relation(net, first, second):
    connections = {}
    for person1, person2 in net:
        if person1 not in connections:
            connections[person1] = set()
        if person2 not in connections:
            connections[person2] = set()
        connections[person1].add(person2)
        connections[person2].add(person1)

    # Recursive depth-first search to find a path between the two people
    def dfs(person, target, visited):
        if person == target:
            return True
        visited.add(person)
        for neighbor in connections[person]:
            if neighbor not in visited:
                if dfs(neighbor, target, visited):
                    return True
        return False

    # Call dfs starting from the first person
    return dfs(first, second, set())


if __name__ == '__main__':
    net = (
        ("Ваня", "Лёша"), ("Лёша", "Катя"),
        ("Ваня", "Катя"), ("Вова", "Катя"),
        ("Лёша", "Лена"), ("Оля", "Петя"),
        ("Стёпа", "Оля"), ("Оля", "Настя"),
        ("Настя", "Дима"), ("Дима", "Маша"),
    )

    assert check_relation(net, "Петя", "Стёпа") is True
    assert check_relation(net, "Маша", "Петя") is True
    assert check_relation(net, "Ваня", "Дима") is False
    assert check_relation(net, "Лёша", "Настя") is False
    assert check_relation(net, "Стёпа", "Маша") is True
    assert check_relation(net, "Лена", "Маша") is False
    assert check_relation(net, "Вова", "Лена") is True
