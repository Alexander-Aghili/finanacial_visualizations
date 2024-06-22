
images, labels = [], []
for query in ["Microsoft Profits", "Google Net Income Report", "Nvidia lastest earnings"]:
  result = embeddings.search(f"select object from txtai where similar(\"{query}\")", 1)[0]
  images.append(result["object"])
  labels.append(query)
