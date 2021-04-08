charts_colors = ["red", "orange", "green", "violet", "blue", "yellow"]

def slice_list(colors_list, start, end):
    charts_colors_copy = charts_colors.copy()
    sliced_charts_colors_copy = charts_colors_copy[start:end]
    print(sliced_charts_colors_copy)
    return sliced_charts_colors_copy


for i in range(7):
    if i == 0:
        for j in range(7):
            print(i, j)
            slice_list(charts_colors, 0, j)
    elif i == 1:
        for j in range(7):
            slice_list(charts_colors, 1, j)
    elif i == 2:
        for j in range(7):
            slice_list(charts_colors, 2, j)
    elif i == 3:
        for j in range(7):
            slice_list(charts_colors, 3, j)
    elif i == 4:
        for j in range(7):
            slice_list(charts_colors, 4, j)
    elif i == 5:
        for j in range(7):
            slice_list(charts_colors, 5, j)

korpo = "Korporacja (z łac. corpo – ciało, ratus – szczur; pol. ciało szczura) – organizacja, która pod przykrywką prowadzenia biznesu włada dzisiejszym światem. Wydawać się może utopijnym miejscem realizacji pasji zawodowych. W rzeczywistości jednak nie jest wcale tak kolorowo. Korporacja służy do wyzyskiwania człowieka w imię postępu. Rządzi w niej prawo dżungli."

print(korpo[-28:])