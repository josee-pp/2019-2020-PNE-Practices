for k, v in all_species_dict.items():
    if k == "species":
        for element in v:
            for k1, v1 in element.items():
                if k1 == "display_name":
                    species = v1
                    all_species_list.append(species)
contents = f"""
                                <!DOCTYPE html>
                                <html lang = "en">
                                <head>
                                <meta charset = "utf-8" >
                                    <title>List of species</title >
                                </head >
                                <body>
                                <h1>All species:</h1>
                                <p>{species}</p>
                                <a href="/">Main page</a>
                                </body>
                                </html>
                                """
