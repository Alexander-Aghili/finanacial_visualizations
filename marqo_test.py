import marqo
import glob
import pprint

mq = marqo.Client(url='http://localhost:8882')

mq.index("images-index").delete()
mq.create_index(
        "images-index",
        treat_urls_and_pointers_as_images=True,
        model="open_clip/ViT-B-32/laion2b_s34b_b79k",
)

images = []
for path in glob.glob('images/*png'):
    images.append({"Title": path, "image": "http://host.docker.internal:8222/" + path})
    
print(images)


mq.index("images-index").add_documents(
        images,
        mappings={
            "images": {
                "type": "multimodal_combination",
                "weights": {
                    "Title": 0.3,
                    "image": 0.7
                }
            }
        },
        tensor_fields=["captioned_image"]
)

results = mq.index("images-index").search(
    q="Nividia's lastest earnings"
)

pprint.pprint(results)
