charts_colors = ["red", "orange", "green", "violet", "blue", "yellow"]

def slice_list(colors_list, end):
    charts_colors_copy = charts_colors.copy()
    sliced_charts_colors_copy = charts_colors_copy[:end]
    return sliced_charts_colors_copy

for i in range(1, len(charts_colors)+1):
    print(slice_list(charts_colors, i))

korpo = "Korporacja (z łac. corpo – ciało, ratus – szczur; pol. ciało szczura) – organizacja, która pod przykrywką prowadzenia biznesu włada dzisiejszym światem. Wydawać się może utopijnym miejscem realizacji pasji zawodowych. W rzeczywistości jednak nie jest wcale tak kolorowo. Korporacja służy do wyzyskiwania człowieka w imię postępu. Rządzi w niej prawo dżungli."

print(korpo[korpo.index('(')+1:korpo.index(')')])