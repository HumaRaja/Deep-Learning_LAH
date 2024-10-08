from fastai.vision.all import *
import pathlib

# Stel het pad in naar je afbeeldingen
data_dir = pathlib.Path("../Liesa")

# DataBlock voor het verwerken van afbeeldingen
dblock = DataBlock(
    blocks=(ImageBlock, CategoryBlock),  # We classificeren afbeeldingen
    get_items=get_image_files,           # Alle afbeeldingsbestanden ophalen
    splitter=RandomSplitter(valid_pct=0.2, seed=123),  # 20% voor validatie
    get_y=parent_label,                  # Labels worden gebaseerd op mappenamen
    item_tfms=Resize(180),               # Afbeeldingen worden geschaald naar 180x180
    batch_tfms=aug_transforms(size=180)  # Basisaugmentatie en schaling
)

# Maak een DataLoaders object
dls = dblock.dataloaders(data_dir, bs=32)

# Het model trainen met een vooraf getrainde ResNet-architectuur
learn = cnn_learner(dls, resnet18, metrics=accuracy)

# Samenvatting van het model
learn.model

# Optionele callback voor vroegtijdig stoppen
early_stopping_cb = EarlyStoppingCallback(monitor='valid_loss', patience=8)

# Train het model
learn.fit_one_cycle(20, cbs=[early_stopping_cb])

# Bewaar het getrainde model
learn.export('ad-model.pkl')
