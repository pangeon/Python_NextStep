def calculate_paint(efficency_ltr_per_m2, **rooms_surface):
    total_surface = 0
    for key in rooms_surface.keys():
        total_surface += rooms_surface[key]

    return efficency_ltr_per_m2 * total_surface



amount_of_paint_1 = calculate_paint(2.2, bedroom = 22, living_room = 30, kitchen = 15)
print(amount_of_paint_1)

rooms_names_with_surfaces = {"bedroom": 22, "living_room": 30, "kitchen": 15}
amount_of_paint_2 = calculate_paint(2.2, **rooms_names_with_surfaces)
print(amount_of_paint_2)