class UnionFinder:

    def __init__(self, ids_vtx: list):
        '''
        Implements special data sctructure union find
        :param number_items: number of items to hold. MUst be larger than One.
        '''
        assert type(ids_vtx) == list
        assert len(ids_vtx) > 1
        self.ids_vtx = ids_vtx
        self.number_unions = len(ids_vtx)
        # original number items
        self._number_item = self.number_unions
        self._union_find = {vtx : (vtx, 0) for vtx in self.ids_vtx}

    def find(self, vtx):
        """
        find parent of vertex
        :param vtx:
        :return: the parent
        """
        #assert vtx in self.ids_vtx
        parent_vtx = self._union_find[vtx][0]
        previous_vtx = vtx
        while self._union_find[parent_vtx][0] != parent_vtx:
            self._union_find[previous_vtx] = (self._union_find[parent_vtx][0], self._union_find[previous_vtx][1])
            previous_vtx = parent_vtx
            parent_vtx = self._union_find[parent_vtx][0]
        return parent_vtx

    def connected(self, vtx_one: int, vtx_two: int):
        """
        checks if first  and second vertex are connected
        :param vtx_one: first vertex
        :param vtx_two: second vertex
        :return: bool, whether both are connected or  not
        """
        #assert vtx_two in self.ids_vtx
        #assert vtx_one in self.ids_vtx
        return self.find(vtx_one) == self.find(vtx_two)

    def union(self, vtx_one: int, vtx_two: int):
        """
        union both supplied vertices
        :param vtx_one: fist vertex
        :param vtx_two: second vertex
        :return: None
        """
        #assert vtx_one in self.ids_vtx
        #assert vtx_two in self.ids_vtx
        parent_one = self.find(vtx_one)
        parent_two = self.find(vtx_two)

        #union can be only be applied if they don´t have already a connected parent
        if parent_one != parent_two:
            # decreas number of items
            self.number_unions -= 1
            val_one = self._union_find[parent_one][1]
            val_two = self._union_find[parent_two][1]

            if val_one > val_two:
                self._union_find[parent_two] = (self._union_find[parent_one][0], self._union_find[parent_two][1])
            elif val_two > val_one:
                self._union_find[parent_one] = (self._union_find[parent_two][0], self._union_find[parent_one][1])
            else:
                self._union_find[parent_two] = self._union_find[parent_one]
                self._union_find[parent_one] = (parent_one, self._union_find[parent_one][1] + 1)
