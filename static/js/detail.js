document.addEventListener("DOMContentLoaded", function() {
    const voteButton = document.getElementById('btn-vote');
    const voteMessage = document.getElementById('vote-message');
    const radioButtons = document.querySelectorAll('input[type="radio"]');

    voteButton.addEventListener('click', function() {
        let selectedOption;
        radioButtons.forEach(radio => {
            if (radio.checked) {
                selectedOption = radio.value;
            }
        });

        if (selectedOption) {

            fetch('/vote', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ vote: selectedOption })
            })
            .then(response => response.json())
            .then(data => {
                voteMessage.innerText = "¡Gracias por votar!";
            })
            .catch(error => {
                voteMessage.innerText = "Hubo un error al procesar tu voto.";
            });
        } else {
            voteMessage.innerText = "Por favor selecciona una opción antes de votar.";
        }
    });
});
