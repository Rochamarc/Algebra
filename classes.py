
class Relation:
    def __init__(self, name: str, input_set: list[any], relation_set: list[any]) -> None:
        self.name = name 
        self.input_set = input_set
        self.relation_set = relation_set

    @property
    def reflective(self) -> bool:
        """If all elements in the ´relation_set´ relate to themselves
        
        Returns 
        -------
        bool : True
        """
        for el in self.relation_set:
            if not el[::-1] in self.relation_set:
                return False
        return True 
    
    @property
    def symmetrical(self) -> bool:
        """For each relation in the ´relation_set´, there must be an opposite relation
        
        Returns
        -------
        bool : True
        """
        symmetrical_relations = [ [el, el] for el in self.input_set ]

        for el in symmetrical_relations:
            if el not in self.relation_set:
                return False 
        return True    

    @property
    def transitive(self) -> bool:
        """For each x that relates to y AND y that relates to z, x necessarily has to relate to z
        
        Returns 
        -------
        bool : True
        """
        rel = [ el for el in self.relation_set if el[0] != el[-1] ]

        for el in rel:
            # now we get all the elements in rel that starts with the image of el
            elements = [ i for i in rel if i != el ]
            
            for el_2 in elements:
                if [el[-1], el_2[-1]] not in self.relation_set:
                    return False
        
        return True
        
    def report(self) -> str:
        """Show all the characteristics of the relation
        
        Returns
        -------
        str : describe the relation
        """
        s = f"A = {self.input_set} => R = {self.relation_set}\n\n"
        s += "Symmetrycal\n" if self.symmetrical else "Anti Symmetric\n"
        s += "Reflective\n" if self.reflective else "Anti Reflective\n"
        s += "Transitive" if self.transitive else "Intransitive"

        return s 
    