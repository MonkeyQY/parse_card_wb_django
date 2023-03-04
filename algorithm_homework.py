import asyncio


class Solution:
    """
    Time complexity алгоритма будет O(N + M), где N - количество пользователей,
     а M - количество связей между ними


    Space complexity для этого алгоритма будет O(N + M),
     где N - количество пользователей, а M - количество связей между ними.
    """

    def check_relation(self, net, first, second):
        users = {}
        for connection in net:
            if connection[0] not in users:
                users[connection[0]] = set()
            if connection[1] not in users:
                users[connection[1]] = set()
            users[connection[0]].add(connection[1])
            users[connection[1]].add(connection[0])

        # Обходим граф в глубину, начиная с первого пользователя
        visited = set()
        stack = [first]
        while stack:
            user = stack.pop()
            if user == second:
                return True
            visited.add(user)
            for friend in users[user]:
                if friend not in visited:
                    stack.append(friend)

        return False


async def main():
    obj = Solution()
    net = (
        ("Ваня", "Лёша"), ("Лёша", "Катя"),
        ("Ваня", "Катя"), ("Вова", "Катя"),
        ("Лёша", "Лена"), ("Оля", "Петя"),
        ("Стёпа", "Оля"), ("Оля", "Настя"),
        ("Настя", "Дима"), ("Дима", "Маша")
    )
    assert obj.check_relation(net, "Петя", "Стёпа") is True
    assert obj.check_relation(net, "Маша", "Петя") is True
    assert obj.check_relation(net, "Ваня", "Дима") is False
    assert obj.check_relation(net, "Лёша", "Настя") is False
    assert obj.check_relation(net, "Стёпа", "Маша") is True
    assert obj.check_relation(net, "Лена", "Маша") is False
    assert obj.check_relation(net, "Вова", "Лена") is True


if __name__ == '__main__':
    asyncio.run(main())