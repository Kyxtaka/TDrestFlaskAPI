# TP restAPI Questionnaire et client Jquery
#### Lien repo git : https://github.com/Kyxtaka/TDrestFlaskAPI
### Prérequis
- Python 3.x doit être installé sur votre machine.
- Chrome ou Firefox possédant une version récente.

### Étapes d'installation

1. **Créer un environnement virtuel Python** :
   Ouvrez un terminal et naviguez jusqu'au répertoire de votre projet. Ensuite, exécutez la commande suivante pour créer un environnement virtuel :

   ```sh
   python -m venv venv
   ```
    ou bien 
    ```sh
   python3 -m venv venv
   ```

2. **Activer l'environnement virtuel** :

    Sur Windows, exécutez la commande suivante :

    ```sh
    .\venv\Scripts\activate
    ```

    Sur Linux ou Mac
    ```sh 
    source venv/bin/activate
    ```

3. **Lancement de l'API Rest Flask** : 
    Se déplacer dans le répertoire `flaskRestAPI` et lancer le server flask 

    ```sh
    cd ./flaskRestAPI
    flask run
    ```

4. Ouvrez votre le Client JQuery en ouvrant le repertoire `questionnireJQueryClient`
   puis le fichier `todo.html` avec un navigateur **Chrome** ou **Firefox**

## Contenu de l'API

Cette API met disposition la gestion de deux ressource : 

### Les Quizs 'Questionnaire' 

Disponible depuis l'endpoint `/todo/api/v1.0/quiz` vous pouvez effectuer différentes requêtes : 

- **GET** : permet la recupération des questionnaire
- **POST** : permet l'ajout d'un questionnaire 
- **PUT** : permet la mise à jour des information d'un questionnaire
- **DELETE** : permet la suppression d'un questionnaire

### Les Question 

Disponible depuis l'endpoint `/todo/api/v1.0/question` vous pouvez effectuer différentes requêtes :

- **GET** : permet la recupération des question
- **POST** : permet l'ajout d'un questionnaire
- **PUT** : permet la mise à jour des information d'un question
- **DELETE** : permet la suppression d'un question

Une question est dépendante de son questionnaire si le questionnaire est supprimé, la question l'est aussi

## Contenu du client Jquery

rappel : Pour accéder ou client sur votre navigateur ouvrez le fichier `questionnireJQueryClient\todo.html`

Le client vous permet de récuprer tous les **questionnaires** et les **question** de la base de données 
mais aussi de les modifier (propriéter pouvant être modifier uniquement)

Le client se répartie en 3 différentes partie : 

1. La tableau des différents questionnaires. Il affiche tout les questionnaire présent dans la BD sous form d'une liste. 
Pour accéder au information d'un questionnaire vous n'avez juste qu'a clicker dessus.

2. Le formulaire d'édition de questionnaire. Il se divise en 2 partie
   
   - Les information du question (cf : nom). Vous pouver modifier le nom du questionnaire comme vous le voulez. 
   Il sufit d'appuyer sur modify questionnaire pour valider les modifications. Vous pouvez également créer un questionnaire 
   en appuyant sur le boutton "+" puis save questionnaire pour l'envoyer dans la BD
   - La listes des questions. Appuyer sur le boutton récupérer question pour l'optenir. Pour consulter ou éditer les informations
   d'une question il suffit juste de clicker sur celle-ci

3. Le fomulaire d'edition de question. Vous pouvez consulter et éditer les information de la même manière que les questionnaire deplus 
   que choisir le type de question si vous en créer une, le formulaire se mettra à jour en fonction.