KEY_AUTOMATON = \
  {
          'Key_D'     : ('delete', '-'),
          'Key_E'     : ('explode', '-'),
          'Key_Escape': ('explore', 'reset'),
          'Key_I'     : ('insert', '-'),
          'Key_V'     : ('explore', '-')
          }
MOUSE_AUTOMATON = \
  {
          'explore': {
                  'ancestor&-:-'             : {
                          1       : ('-', '-'),
                          2       : ('-', '-'),
                          'cursor': '-'
                          },
                  'arc_edge.head&-:-'        : {
                          1       : ('-', '-'),
                          2       : ('-', '-'),
                          'cursor': '-'
                          },
                  'arc_edge.head&-:normal'   : {
                          1       : ('-', '-'),
                          2       : ('-', '-'),
                          'cursor': '-'
                          },
                  'arc_edge.head&-:open'     : {
                          1       : ('-', '-'),
                          2       : ('-', '-'),
                          'cursor': '-'
                          },
                  'arc_edge.head&-:selected' : {
                          1       : ('-', '-'),
                          2       : ('-', '-'),
                          'cursor': '-'
                          },
                  'arc_edge.tail&-:-'        : {
                          1       : ('-', '-'),
                          2       : ('-', '-'),
                          'cursor': '-'
                          },
                  'arc_edge.tail&-:normal'   : {
                          1       : ('-', '-'),
                          2       : ('-', '-'),
                          'cursor': '-'
                          },
                  'arc_edge.tail&-:open'     : {
                          1       : ('-', '-'),
                          2       : ('-', '-'),
                          'cursor': '-'
                          },
                  'arc_edge.tail&-:selected' : {
                          1       : ('-', '-'),
                          2       : ('-', '-'),
                          'cursor': '-'
                          },
                  'arc_info_knot&-:-'        : {
                          1       : ('-', '-'),
                          2       : ('-', '-'),
                          'cursor': '-'
                          },
                  'arc_info_knot&-:normal'   : {
                          1       : ('-', '-'),
                          2       : ('-', '-'),
                          'cursor': '-'
                          },
                  'arc_info_knot&-:open'     : {
                          1       : ('-', '-'),
                          2       : ('-', '-'),
                          'cursor': '-'
                          },
                  'arc_info_knot&-:selected' : {
                          1       : ('-', '-'),
                          2       : ('-', '-'),
                          'cursor': '-'
                          },
                  'arc_knot&-:-'             : {
                          1       : ('-', '-'),
                          2       : ('-', '-'),
                          'cursor': '-'
                          },
                  'arc_knot&-:normal'        : {
                          1       : ('-', '-'),
                          2       : ('-', '-'),
                          'cursor': '-'
                          },
                  'arc_knot&-:open'          : {
                          1       : ('-', '-'),
                          2       : ('-', '-'),
                          'cursor': '-'
                          },
                  'arc_knot&-:selected'      : {
                          1       : ('-', '-'),
                          2       : ('-', '-'),
                          'cursor': '-'
                          },
                  'node_composite&-:-'       : {
                          1       : ('-', '-'),
                          2       : ('-', '-'),
                          'cursor': '-'
                          },
                  'node_composite&-:normal'  : {
                          1       : ('-', '-'),
                          2       : ('-', '-'),
                          'cursor': '-'
                          },
                  'node_composite&-:selected': {
                          1       : ('-', '-'),
                          2       : ('-', '-'),
                          'cursor': '-'
                          },
                  'node_simple&-:-'          : {
                          1       : ('-', '-'),
                          2       : ('-', '-'),
                          'cursor': '-'
                          },
                  'node_simple&-:normal'     : {
                          1       : ('-', '-'),
                          2       : ('-', '-'),
                          'cursor': '-'
                          },
                  'node_simple&-:selected'   : {
                          1       : ('-', '-'),
                          2       : ('-', '-'),
                          'cursor': '-'
                          },
                  'node_viewed&-:-'          : {
                          1       : ('-', '-'),
                          2       : ('-', '-'),
                          'cursor': '-'
                          },
                  'sibling&-:-'              : {
                          1       : ('-', '-'),
                          2       : ('-', '-'),
                          'cursor': '-'
                          }
                  }
          }
DESIGNATED_KEYS = \
  {'modifier': 'Key_Shift', 'reset': 'Key_Escape', 'select': 'Key_S'}
