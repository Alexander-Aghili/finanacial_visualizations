import glob

from PIL import Image

from txtai.embeddings import Embeddings
from txtai.pipeline import Caption

def images():
    for path in glob.glob('images/*png'):
        image = Image.open(path)
        yield (path, {"object": image, "format": image.format, "width": image.width, "height": image.height})

embeddings = Embeddings({"method": "sentence-transformers", "path": "sentence-transformers/clip-ViT-B-32", "content": True, "objects": "image"})
embeddings.index(images())
print(embeddings.count())
print(embeddings.search("select id, object, format, width, height from images"))
#print(embeddings.load(embeddings.search("select id, object, format, width, height from images")[0]['id']))

images, labels = [], []
for query in ["Microsoft Profits", "Google Net Income Report", "Nvidia lastest earnings"]:
  result = embeddings.search(f"select object from images where similar(\"{query}\")", 1)[0]
  print(result)
  images.append(result["object"])
  labels.append(query)

import ipyplot
from PIL import Image

def resize(images):
  results = []
  for image in images:
    results.append(image.resize((350, int(image.height * (350 / image.width))), Image.Resampling.LANCZOS))

  return results


ipyplot.plot_images(resize(images), labels, img_width=350, force_b64=True)

