def broadcast_transaction(self, transaction):
    self.request_nodes_from_all()
    bad_nodes = set()
    data = {
        "transaction": transaction
    }

    for node in self.full_nodes:
        url = TRANSACTIONS_URL.format(node, FULL_NODE_PORT)
        try:
            response = requests.post(url, data)
        except requests.exceptions.RequestException as re:
            bad_nodes.add(node)
    for node in bad_nodes:
        self.remove_node(node)
    bad_nodes.clear()
    return