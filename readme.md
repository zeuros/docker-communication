# Communication entre conteneurs / avec l'hôte

> Ce repo montre 
> - Comment lier un conteneur qui contient un serveur flask à l'hôte (conteneur 'web')
> - Comment contacter un serveur flask dans un conteneur ('webshahaf') depuis un autre conteneur ('web')

### Meilleure commande pour build / rebuild & lancer les conteneurs

```shell
docker compose up --build [optionel: nom du container modifié à rebuild (évite de tout rebuild à chaque fois)]
```
