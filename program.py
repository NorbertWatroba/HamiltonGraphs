import argparse
from graph import Graph

parser = argparse.ArgumentParser()
group = parser.add_mutually_exclusive_group()
group.add_argument('--hamilton', action='store_true', help='With Hamilton cycle')
group.add_argument('--non-hamilton', action='store_true', help='Without Hamilton cycle')

args = parser.parse_args()

if args.hamilton:
    from creators import hamilton_data
    nodes = int(input('     nodes> '))
    saturation = int(input('saturation> '))
    while saturation not in (30, 70):
        print('saturation can only be equal to 30 or 70 percent!\n')
        saturation = int(input('saturation> '))
    graph = Graph(hamilton_data(nodes, saturation))

elif args.non_hamilton:
    from creators import non_hamilton_data
    nodes = int(input(' nodes> '))
    graph = Graph(non_hamilton_data(nodes))

else:
    raise Exception("Must provide program's working mode!")


while True:
    action = input('action> ')
    match action.strip().lower():
        case 'print' | 'p':
            print(graph)
        case 'hamilton' | 'h':
            pass
        case 'euler' | 'e':
            pass
        case 'help' | '?':
            print('''
+=========================================================================+
|  Help       | ? |   Show this message                                   |
|  Print      | p |   Print matrix representation                         |
|  Hamilton   | h |   Find Hamilton cycle                                 |
|  Euler      | e |   Find Euler cycle                                    |
|  Exit       | q |   Exits the program (same as ctrl+D)                  |
+=========================================================================+''')
        case 'exit' | 'q':
            break
        case _:
            print('command not found! type help')
