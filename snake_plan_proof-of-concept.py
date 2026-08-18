# Snake method for both Anziani and Sorelle
import pandas as pd

# Load dataset
environment = pd.read_csv("test_environment.csv")

# Split into Anziani and Sorelle Subsets
anziani_environment = environment[environment["is_male"] == True].copy()
sorelle_environment = environment[environment["is_male"] == False].copy()


def snake_method(df, start_name):
    """
    Traces a snake chain through the dataset starting from "start_name",
    following destination areas to resident missionaries until the chain ends.
    Returns the list chain and the set of visited missionaries.
    """
    current_name = start_name
    chain = []
    visited = set()
    
    # The main loop
    while current_name and current_name not in visited:
        visited.add(current_name)
        chain.append(current_name)
        
        # Get the row for the current missionary
        match = df[df["missionary_name"] == current_name]
        if match.empty:
            break
            
        missionary = match.iloc[0]
        next_area = missionary["next_area"]
        
        # Find who is currently in the next_area
        residents = df[(df["current_area"] == next_area) & (df["missionary_name"] != current_name)]
        
        if residents.empty:
            break
        else:
            next_row = residents.iloc[0]
            current_name = next_row["missionary_name"]
            
    return chain, visited


def get_display_companion(row):
    """
    If new missionary, their companion was OFFICE.
    If going home, their companion will be OFFICE.
    """
    if row["new_missionary"]:
        return "OFFICE"
    elif row["going_home"]:
        return "OFFICE"
    else:
        c1 = row["companion_1_name"]
        c2 = row["companion_2_name"]
        comps = [c for c in [c1, c2] if pd.notna(c)]
        return ", ".join(comps) if comps else "None"


def print_alternating_horizontal_chain(df, chain):
    """
    Prints the chain horizontally with alternating arrows between the top row 
    (missionaries) and bottom row (companions/Office) to reflect travel paths.
    """
    tops = []
    bots = []
    
    for name in chain:
        row = df[df["missionary_name"] == name].iloc[0]
        comp_str = get_display_companion(row)
        
        tops.append(name)
        bots.append(comp_str)
        
    widths = [max(len(t), len(b)) for t, b in zip(tops, bots)]
    
    padded_tops = [t.ljust(w) for t, w in zip(tops, widths)]
    padded_bots = [b.ljust(w) for b, w in zip(bots, widths)]
    
    dash_arrow = "  --->  "
    space_gap = " " * len(dash_arrow)
    
    top_line_parts = []
    bot_line_parts = []
    
    print("\n --- SNAKE CHAIN ---")
    
    for i in range(len(chain)):
        top_line_parts.append(padded_tops[i])
        bot_line_parts.append(padded_bots[i])
        
        if i < len(chain) - 1:
            if i % 2 == 0:
                top_line_parts.append(dash_arrow)
                bot_line_parts.append(space_gap)
            else:
                top_line_parts.append(space_gap)
                bot_line_parts.append(dash_arrow)
                
    print("".join(top_line_parts))
    print("".join(bot_line_parts))


def process_missionaries(df, label):
    """
    Runs the snake chain generation across priority groups for either anziani or sorelle.
    """
    print(f"PROCESSING: {label}")
    
    new_group = df[df["new_missionary"] == True]
    going_home_group = df[df["going_home"] == True]
    remaining_group = df[(df["new_missionary"] == False) & (df["going_home"] == False)]
    
    print(f"Found {len(new_group)} new, {len(going_home_group)} going home, and {len(remaining_group)} remaining.")
    
    all_assigned = set()
    priority_groups = [
        ("New Missionaries", new_group["missionary_name"].tolist()),
        ("Going Home Missionaries", going_home_group["missionary_name"].tolist()),
        ("Remaining Missionaries", remaining_group["missionary_name"].tolist())
    ]

    for group_name, names in priority_groups:
        if not names:
            continue
        print(f"\n--- Group: {group_name} ---")
        for name in names:
            if name not in all_assigned:
                chain, visited = snake_method(df, name)
                all_assigned.update(visited)
                print_alternating_horizontal_chain(df, chain)

    print(f"\nTotal {label.lower()} accounted for: {len(all_assigned)} / {len(df)}")


# This part runs it for both!
process_missionaries(anziani_environment, "ANZIANI")
process_missionaries(sorelle_environment, "SORELLE")