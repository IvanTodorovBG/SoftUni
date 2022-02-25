dwarfs_data = {}
hat_phys_groups = {}
index_entry = 0

while True:
    data = input()
    if "Once upon a time" in data:
        break
    dwarf_name, dwarf_hat_color, dwarf_physics = data.split(" <:> ")
    dwarf_physics = int(dwarf_physics)
    dwarf_id = dwarf_hat_color + dwarf_name
    group_id = dwarf_hat_color
    index_entry += 1
    if dwarf_id not in dwarfs_data:
        dwarfs_data[dwarf_id] = (dwarf_hat_color, dwarf_name, dwarf_physics, index_entry)
        if group_id not in hat_phys_groups:
            hat_phys_groups[group_id] = 0
        hat_phys_groups[group_id] += 1
    elif dwarfs_data[dwarf_id][2] <= dwarf_physics:
        old_group_id = dwarf_hat_color
        hat_phys_groups[old_group_id] -= 1
        dwarfs_data[dwarf_id] = (dwarf_hat_color, dwarf_name, dwarf_physics, index_entry)
        if group_id not in hat_phys_groups:
            hat_phys_groups[group_id] = 0
        hat_phys_groups[group_id] += 1


sorted_dwarfs = sorted(dwarfs_data.items(), key=lambda kvp: (-kvp[1][2], -hat_phys_groups[kvp[1][0]]))
for k, v in sorted_dwarfs:
    print(f"({v[0]}) {v[1]} <-> {v[2]}")