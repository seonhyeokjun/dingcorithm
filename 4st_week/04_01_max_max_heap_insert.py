class MaxHeap:
    def __init__(self):
        self.items = [None]

    def insert(self, value):
        self.items.append(value)

        cur_index = len(self.items) - 1
        while cur_index > 1: # cur_index가 1이 되면 루트 노드에 도달한 것
            parent_index = cur_index // 2 # 부모 노드의 인덱스
            if self.items[cur_index] > self.items[parent_index]: # 부모 노드보다 자식 노드가 더 크다면
                self.items[cur_index], self.items[parent_index] = self.items[parent_index], self.items[cur_index] # 부모 노드와 자식 노드의 위치를 바꿔준다
                cur_index = parent_index # 부모 노드의 인덱스로 이동
            else:
                break

max_heap = MaxHeap()
max_heap.insert(3)
max_heap.insert(4)
max_heap.insert(2)
max_heap.insert(9)
print(max_heap.items)  # [None, 9, 4, 2, 3] 가 출력되어야 합니다!