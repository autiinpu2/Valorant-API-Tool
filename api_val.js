// fetch_account_value.js
function fetchValorantAccountValue() {
    fetch('votre_script.py')  // Remplacez 'votre_script.py' par le chemin vers votre script Python
        .then(response => response.json())
        .then(data => {
            // Sélectionnez un élément du DOM pour afficher les informations
            document.getElementById('accountValue').innerText = JSON.stringify(data);
        })
        .catch(error => console.error('Erreur:', error));
}

// Assurez-vous que le code ci-dessus soit exécuté une fois le DOM chargé
document.addEventListener('DOMContentLoaded', fetchValorantAccountValue);
