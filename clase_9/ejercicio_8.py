tecnologias_por_grupo = {
    "Grupo 1": {"Python", "Git"},
    "Grupo 2": {"Python", "JSON"}
}

tecnologias_por_grupo["Grupo 3"] = {"SQL", "Power BI"}
print(tecnologias_por_grupo)

tecnologias_por_grupo["Grupo 1"].add("pytest")
print(tecnologias_por_grupo["Grupo 1"])

resultado = tecnologias_por_grupo.get("Grupo 4")
print(resultado)

for grupo, tecnologias in tecnologias_por_grupo.items():
    print(grupo, ":", sorted(tecnologias))