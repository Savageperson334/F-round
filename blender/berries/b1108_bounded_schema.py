# bounded_schema
#
# Copied verbatim from https://github.com/ashtonwallen/ShipwreckHunter
#   file backend/mcp_server.py, line 63
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Shipwrecks and maritime ghosts
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import copy


def bounded_schema(schema):
    """Keep the shared assistant schemas, with bounded MCP inputs."""
    schema = copy.deepcopy(schema)
    def visit(node):
        if node.get('type') == 'string':
            node.setdefault('minLength', 1)
            node.setdefault('maxLength', 12000)
        if node.get('type') == 'array':
            node.setdefault('maxItems', 100)
            visit(node['items'])
        for child in node.get('properties', {}).values():
            visit(child)
    visit(schema)
    return schema
