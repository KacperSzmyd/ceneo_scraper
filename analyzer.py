from pandas._config.config import options
from matplotlib import colors, pyplot as plt
from os import listdir
import pandas as pd
import numpy as np

pd.set_option("display.max_columns", None)


print(*[file_name.split(".")[0] for file_name in listdir("opinions")], sep="\n")

prduct_id = input("Podaj kod produktu: ")
opinions = pd.read_json("opinions/{}.json".format(prduct_id))


opinions_count = opinions.opinion_id.count()

pros_count = opinions.pros.astype(bool).sum()

cons_count = opinions.cons.astype(bool).sum()

opinions.stars = opinions.stars.map(lambda stars: float(stars.split("/")[0].replace(",", ".")))
average_score = opinions.stars.mean().round(2)

stars = opinions.stars.value_counts().reindex(np.arange(0,5.5,0.5), fill_value = 0)

"""stars.plot.bar(color = "red")
plt.title("Gwiazdki")
plt.xlabel("Liczba gwiazdek")
plt.ylabel("Liczba opinii")
plt.savefig("plots/{}.png".format(prduct_id))
plt.close()"""

recomm = opinions.recomm.value_counts(dropna = False).sort_index()
recomm.plot.pie(colors = ["crimson", "blue", "forestgreen"])

plt.show()

