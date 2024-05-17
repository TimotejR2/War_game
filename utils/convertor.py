def location_to_field(location, map):
        selected_field = None
        for cell in map.all_fields:
            if cell.location == location:
                return cell
        raise Exception('Field not found')