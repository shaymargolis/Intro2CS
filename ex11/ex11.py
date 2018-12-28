############################################################
# FILE : ex11.py
# WRITER : shay margolis , 211831136
# EXERCISE : intro2cs1 ex11 2018-2019
# DESCRIPTION : A class containing implementation of the ex
#############################################################

import itertools


class Node:
    def __init__(self, data, pos = None, neg = None):
        self.data = data
        self.positive_child = pos
        self.negative_child = neg

    def __str__(self, depth=0):
        ret = ""

        # Print right branch
        if self.positive_child != None:
            ret += self.positive_child.__str__(depth + 1)

        # Print own value
        ret += "\n" + ("    "*depth) + str(self.data)

        # Print left branch
        if self.negative_child != None:
            ret += self.negative_child.__str__(depth + 1)

        return ret


class Record:
    def __init__(self, illness, symptoms):
        self.illness = illness
        self.symptoms = symptoms

    def __str__(self):
        return self.illness


def parse_data(filepath):
    with open(filepath) as data_file:
        records = []
        for line in data_file:
            words = line.strip().split()
            records.append(Record(words[0], words[1:]))
        return records


class Diagnoser:
    def __init__(self, root):
        self.root = root

    def diagnose_helper(self, tree, symptoms):
        """
        Returns the diagnosis, the ilennes for symptoms
        starting from a specific node in the tree "root"
        :param tree: The starting node in the tree
        :param symptoms: Array of symptoms
        :return: The name of the ilness
        """
        #  Check if the answer is positive - if
        #  root is in symptoms
        if tree.data in symptoms:
            #  If we have no positive child then
            #  we are the answer
            if tree.positive_child is None:
                return tree.data

            #  Else return the result of the diagnose for the next
            #  child
            return self.diagnose_helper(tree.positive_child, symptoms)

        #  If root.data is not in symptoms then
        #  run the diagnose for the next child
        if tree.negative_child is not None:
            return self.diagnose_helper(tree.negative_child, symptoms)

        #  Else then we are the answer
        return tree.data

    def diagnose(self, symptoms):
        """
        Returns the guesses illenes for the symptoms
        according to the decision tree
        :param symptoms:
        :return:
        """
        return self.diagnose_helper(self.root, symptoms)

    def calculate_success_rate(self, records):
        """
        Calculates the success rate of the decision tree
        for the records.
        :param records: Array of Records with symptoms
            and right ilennes for them
        :return: ratio between good gueesses and count of
            records
        """

        passed = 0

        #  For every record, check if our guess was right
        #  and if yes, add one to "passed"
        for record in records:
            guess = self.diagnose(record.symptoms)

            #  If the illenes is right
            if guess == record.illness:
                passed += 1

        return passed/len(records)

    def all_illenesses_helper(self, tree):
        """
        Returns all leaves of the tree that is starting
        at tree
        :param tree: Node
        :return: array of all leaves (illenesses of the tree)
        """

        if tree is None:
            return []

        if tree.positive_child is None and tree.negative_child is None:
            return [tree.data]

        return self.all_illenesses_helper(tree.positive_child) \
            + self.all_illenesses_helper(tree.negative_child)

    def all_illnesses(self):
        """
        Returns all leaves of the tree that is starting
        at self.root
        :return: array of all leaves
        """

        return self.all_illenesses_helper(self.root)

    def most_rare_illness(self, records):
        """
        Makes a diagnose for all recors, and
        returns the ilness that appears the least
        number of times.
        :param records: List of Record
        :return: name of rarest illness
        """

        #  Ilnesses will contains all found ilnesses
        #  and the number of appeareances
        illnesses = dict()

        #  For every record, make a diagnose and add it to
        #  the dict
        for record in records:
            diagnose = self.diagnose(record.symptoms)

            if illnesses.get(diagnose) is None:
                illnesses[diagnose] = 1
            else:
                illnesses[diagnose] += 1

        #  Find the ilennes that appeared the least
        #  number of times in the dict
        #  minimum holds the current minimum and the
        #  number of times it was diagnosed by our
        #  algoritm
        #  The maximum is len(records) because every ilennes
        #  will appear less times than that
        minimum = (None, len(records))

        for key, value in illnesses.items():
            if value < minimum[1]:
                minimum = (key, value)

        return minimum[0]

    def paths_to_illness_helper(self, tree, illness):
        """
        Returns all the routes from root Node to illness
        leave, as array.
        :param tree: starting Node
        :param illness: the name of the illness
        :return: array of all routes
        """

        #  If we are on a leave return an empty route
        if tree.positive_child is None and tree.negative_child is None:
            #  There is a way
            if illness == tree.data:
                return [[]]

            #  There is not a way
            return []

        #  Search for a way from the right and left
        way_right = self.paths_to_illness_helper(tree.positive_child, illness)
        way_left = self.paths_to_illness_helper(tree.negative_child, illness)

        #  Create the final ways from "tree"
        ways = []
        for way in way_right:
            ways.append([True] + way)

        for way in way_left:
            ways.append([False] + way)

        return ways

    def paths_to_illness(self, illness):
        """
        Returns all paths to illness from self.root
        to the nodes with illness.
        :param illness: Name of illness
        :return:
        """

        return self.paths_to_illness_helper(self.root, illness)


def build_tree_symptoms(symptoms, index):
    """
    Builds a decision tree for specific symptoms,
    by their order (of course the order
    does not matter as we saw in the instructions)
    :param symptoms: Array of symptoms
    :return: Root node of tree
    """

    #  If we reached end of symptoms, just create
    #  the ending node and return it
    if index == len(symptoms) - 1:
        root = Node(symptoms[index], None, None)
        return root

    #  Else, create left and right node, and
    #  build a node that connects them
    right = build_tree_symptoms(symptoms, index+1)
    left  = build_tree_symptoms(symptoms, index+1)

    root = Node(symptoms[index], right, left)
    return root


def define_leaves(records, tree, list):
    """
    Defines the leaves from the records
    the illnesses
    :param records: List of Records
    :param tree: Root node
    :param list: The current nodes that
        passed the filter of the symptoms
        in the route
    :return: nothing
    """

    #  Filters the list to RIGHT and LEFT
    #  lists: according to the illnesses
    #  that match the symptom and the ones
    #  that no.
    temp_right_list = []
    temp_left_list = []
    for record in list:
        #  If data matches the symptom, add it to the
        #  right list, and another to the left list.
        if tree.data in record.symptoms:
            r = Record(record.illness, record.symptoms.copy())
            r.symptoms.remove(tree.data)
            temp_right_list.append(r)
        else:
            temp_left_list.append(record)

    #  If we got to a leave, put the right and left leave result
    #  , the one that best fits the data.
    if tree.positive_child is None and tree.positive_child is None:
        #  find the min in each list
        min_right = Record("", [])
        min_left = Record("", [])

        for i in range(0, len(temp_right_list)):
            if len(min_right.symptoms) == 0 or len(temp_right_list[i].symptoms) < len(min_right.symptoms):
                min_right = temp_right_list[i]

        for i in range(0, len(temp_left_list)):
            if len(min_left.symptoms) == 0 or len(temp_left_list[i].symptoms) < len(min_left.symptoms):
                min_left = temp_left_list[i]

        #  Get the right and left new Nodes, and if they do not
        #  exist, add a random node (first from records)
        right_node = records[0] if len(min_right.symptoms) == 0 else min_right
        left_node = records[0] if len(min_left.symptoms) == 0 else min_left

        tree.positive_child = Node(right_node.illness, None, None)
        tree.negative_child = Node(left_node.illness, None, None)
        return

    define_leaves(records, tree.positive_child, temp_right_list)
    define_leaves(records, tree.negative_child, temp_left_list)


def build_tree(records, symptoms):
    """
    Builds a tree from records to ilnesses, and
    the symptoms to create the tree with.
    Maximized the hit percents of the records for
    the tree.
    :param records: Array of illness Records
    :param symptoms: Array of symptoms to create
        the tree with.
    :return:
    """

    #  Create a tree with the symptoms
    root = build_tree_symptoms(symptoms, 0)

    #  Add the illnesses to it by the record
    define_leaves(records, root, records)

    return root


def optimal_tree(records, symptoms, depth):
    """
    Returns the optimal tree (The tree with the best
    guessing rates for records) for different subsets
    of symptoms with size of depth.
    :param records: Array of Records
    :param symptoms: Array of symptoms
    :param depth: the size of the subset of symptoms
    :return:
    """

    #  Iterates on all of the subsets in size of depth
    #  of symptoms and for each builds a tree, gets the
    #  success rates, and updates the current maximum.
    maximum = (None, 0)

    for x in itertools.combinations(symptoms, depth):
        #  Build a tree with subset x
        root = build_tree(records, x)

        #  Checks the success rates for records
        diagn = Diagnoser(root)
        success_rates = diagn.calculate_success_rate(records)

        #  If the success rates of this tree are bigger
        #  than the maximum, update it.
        if success_rates >= maximum[1]:
            maximum = (root, success_rates)

    return maximum[0]

if __name__ == "__main__":

    # Manually build a simple tree.
    #                cough
    #          Yes /       \ No
    #        fever           healthy
    #   Yes /     \ No
    # influenza   cold

    flu_leaf = Node("influenza", None, None)
    cold_leaf = Node("cold", None, None)
    inner_vertex = Node("fever", flu_leaf, cold_leaf)
    healthy_leaf = Node("healthy", None, None)
    root = Node("cough", inner_vertex, healthy_leaf)

    diagnoser = Diagnoser(root)

    # Simple test
    diagnosis = diagnoser.diagnose(["cough"])
    if diagnosis == "cold":
        print("Test passed")
    else:
        print("Test failed. Should have printed cold, printed: ", diagnosis)

    # Add more tests for sections 2-7 here.
    #  Test for success_rates
    records = []

    records.append(Record("cold", ["cough"]))
    records.append(Record("influenza", ["cough", "fever"]))
    records.append(Record("influenza", ["cough"]))
    records.append(Record("healthy", []))

    rates = diagnoser.calculate_success_rate(records)

    if rates == 3/4:
        print("Test passed")
    else:
        print("Test failed. Should have printed 3/4, printed: ", rates)

    #  Test for all ilnesses
    all = diagnoser.all_illnesses()

    if all == ["influenza", "cold", "healthy"]:
        print("Test passed")
    else:
        print("Test failed. Should have printed 'influenza', 'cold', 'healthy', printed: ", all)

    #  Test paths to illness
    path = diagnoser.paths_to_illness("cold")

    if path == [[True, False]]:
        print("Test passed")
    else:
        print("Test failed. Should have printed [[True, False]] printed: ", path)

    #  Test create tree
    record1 = Record("influenza", ["cough","fever"])
    record2 = Record("cold", ["cough"])
    records = [record1, record2]

    root = build_tree(records, ["fever"])

    #  print(root)

    #  Test optimal tree
    root = optimal_tree(records, ["cough", "fever"], 1)

    #  print(root)