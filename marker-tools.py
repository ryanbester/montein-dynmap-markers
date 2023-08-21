import argparse
import json

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--file', default='markers.json', help='Markers JSON file')
    
    subparsers = parser.add_subparsers(dest='subparser')
    
    parser_id_check = subparsers.add_parser('idcheck')
    parser_sort = subparsers.add_parser('sort')

    args = parser.parse_args()
    
    cmd = args.subparser

    markers = parse_markers_file(args.file)
    
    if cmd == 'idcheck':
        duplicates = 0

        print('Checking set IDs')
        found_ids = set()
        for marker_set in markers['sets']:
            if marker_set['id'] in found_ids:
                duplicates += 1
                print('\tSet ID "{}" already used'.format(marker_set['id']))
            else:
                found_ids.add(marker_set['id'])

        for marker_set in markers['sets']:
            print('Checking marker IDs for set "{}"'.format(marker_set['id']))
            found_ids.clear()
            for marker in marker_set['markers']:
                if marker['id'] in found_ids:
                    duplicates += 1
                    print('\tMarker ID "{}" already used in set "{}"'.format(marker['id'], marker_set['id']))
                else:
                    found_ids.add(marker['id'])

            print('Checking area marker IDs for set "{}"'.format(marker_set['id']))
            found_ids.clear()
            for marker in marker_set['areas']:
                if marker['id'] in found_ids:
                    duplicates += 1
                    print('\tArea marker ID "{}" already used in set "{}"'.format(marker['id'], marker_set['id']))
                else:
                    found_ids.add(marker['id'])

        if duplicates == 0:
            print('No duplicates found!')
        else:
            print('{} duplicates found'.format(duplicates))

    elif cmd == 'sort':
        # Create backup
        save_markers_file(args.file + '.bak', markers)

        for marker_set in markers['sets']:
            print('Sorting set "{}"'.format(marker_set['id']))

            print('Sorting markers')
            sorted_markers = sorted(marker_set['markers'], key=lambda x: x['id'])
            marker_set['markers'] = sorted_markers

            print('Sorting area markers')
            sorted_areas = sorted(marker_set['areas'], key=lambda x: x['id'])
            marker_set['areas'] = sorted_areas

        save_markers_file(args.file, markers)


def parse_markers_file(markers_file):
    with open(markers_file) as f:
        data = json.load(f)
        return data
    
def save_markers_file(markers_file, data):
    with open(markers_file, 'w') as f:
        json.dump(data, f, indent=4)

if __name__ == '__main__':
    main()
