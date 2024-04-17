# Communication entre conteneurs / avec l'hôte

> Ce repo montre 
> - Comment lier un conteneur qui contient un serveur à l'hôte (conteneur 'web')
> - Comment contacter un serveur dans un conteneur ('webshahaf') depuis un autre conteneur ('web')

### Meilleure commande

```shell
docker compose up --build [optionel: nom du container à rebuild (évite de tout rebuild)]
```