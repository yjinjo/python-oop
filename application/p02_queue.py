from typing import Optional, Generic, TypeVar

T = TypeVar("T")


class Node(Generic[T]):
    # pointer의 경우 다음 Node를 가리키는데, 없을 수도 있으므로 Optional로 타입을 정한다.
    def __init__(self, item: T, pointer: Optional["Node"] = None):
        self.item = item
        self.pointer: Optional["Node"] = pointer


class LinkedList(Generic[T]):
    def __init__(self):
        self.head: Optional[Node[T]] = None

    @property
    def length(self) -> int:
        # 만약 head가 존재하지 않는다는 것은 하나도 없다는 것이므로,
        if self.head is None:
            return 0

        cur_node = self.head
        count: int = 1  # 현재 노드인 head 노드는 바로 위에서 한 번 셋으므로,
        while cur_node.pointer is not None:
            cur_node = cur_node.pointer
            count += 1

        return count

    def __str__(self) -> str:
        result: str = ""
        if self.head is None:
            return result

        cur_node = self.head
        result += f"{cur_node.item}"

        while cur_node.pointer is not None:
            cur_node = cur_node.pointer
            result += f", {cur_node.item}"

        return result


class Stack(Generic[T], LinkedList[T]):
    def push(self, item: T) -> None:
        new_node: Node[T] = Node[T](item=item)

        # 노드가 하나도 없는 경우,
        if self.head is None:
            self.head = new_node
            return
        # 이미 노드가 있는 경우, 현재 노드에 head 노드를 넣고,
        cur_node: Node = self.head
        # 노드의 마지막을 가리킬 떄까지 계속해서 cur_node를 다음 노드로 이동시킨다.
        while cur_node.pointer is not None:
            cur_node = cur_node.pointer
        # 제일 마지막에 왔을 때는 새로 추가한 노드를 현재 노드의 pointer가 가리키게 한다.
        cur_node.pointer = new_node

    def pop(self) -> T:
        if self.head is None:
            raise ValueError("stack is empty")
        else:
            cur_node = self.head

        # 그 다음 포인터가 None이면 지금 현재 1개밖에 없다는 것이다.
        # 그럼 pop할 경우 None이 될 것이다.
        if cur_node.pointer is None:
            self.head = None
            return cur_node.item

        # 계속 움직이면서 뽑을 것인데,
        while cur_node.pointer.pointer is not None:
            cur_node = cur_node.pointer

        # 만약 그 다음다음 Node가 None이라면 그다음 노드가 이제 마지막을 의미하므로 하나 뽑는 것이다.
        result = cur_node.pointer

        # 그리고 위에서 뽑은 다음 그다음 노드를 None으로 만들어준다.
        cur_node.pointer = None

        return result.item


class Queue(Generic[T], LinkedList[T]):
    def enqueue(self, item: T) -> None:
        # Stack의 push 메서드와 같다.
        new_node: Node[T] = Node[T](item=item)
        if self.head is None:
            self.head = new_node
            return
        cur_node: Node = self.head
        while cur_node.pointer is not None:
            cur_node = cur_node.pointer
        cur_node.pointer = new_node

    def dequeue(self) -> T:
        if self.head is None:
            raise ValueError("queue is empty")

        cur_node = self.head
        if cur_node.pointer is None:
            self.head = None
            return cur_node.item

        result = cur_node.item
        self.head = cur_node.pointer

        return result


if __name__ == "__main__":
    stack = Stack[int]()
    stack.push(12)
    stack.push(2)
    stack.push(3)
    stack.push(4)
    stack.pop()
    print(stack.length)

    print(stack)

    queue = Queue[int]()
    queue.enqueue(12)
    queue.enqueue(1)
    queue.enqueue(13)
    queue.enqueue(16)

    print(queue.dequeue())

    print(queue)  # 1, 13, 16
    print(queue.length)  # 3
