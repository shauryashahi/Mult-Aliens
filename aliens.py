import config


def want_to_add_another():
    while True:
        want_another = raw_input("Want to add another alien? [Y/N] >")
        if want_another.lower() == "y":
            return True
        if want_another.lower() == "n":
            return False
        print "Error: Please enter only Y or N"


def format_report(data):
    plugin_names = config.available_plugins.keys()
    num_plugins = len(plugin_names)
    print "Here are available report format"
    for counter in range(num_plugins):
        print "[{}] {}".format(counter, plugin_names[counter])
    while True:
        selection = raw_input("select format number >")
        try:
            selection_int = int(selection)
        except:
            print "Error: Please enter an integer"
            continue
        if selection_int >= 0 and selection_int < num_plugins:
            formatter = config.available_plugins[plugin_names[int(selection)]]
            formatter(data)
            return
        else:
            print "Error: Please select a number between 0 and {}"\
                .format(counter)


def get_user_input():
    data = [
        (
            "Serial No.",
            "Code-Name",
            "Blood-Color",
            "No. of Antennas",
            "No. of Legs",
            "Home Planet"
        )
    ]
    serial_no = 0
    while True:
        serial_no += 1
        code_name = raw_input("code name >")
        blood_color = raw_input("blood color >")
        num_antennas = raw_input("number of antennas >")
        num_legs = raw_input("number of legs >")
        home_planet = raw_input("home planet >")
        data.append(
            (
                str(serial_no),
                code_name,
                blood_color,
                num_antennas,
                num_legs,
                home_planet
            )
        )
        if not want_to_add_another():
            return data


def main():
    data = get_user_input()
    format_report(data)


if __name__ == "__main__":
    main()
