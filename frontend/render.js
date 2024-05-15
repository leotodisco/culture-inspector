// Dichiarazione della variabile selectedOptions
let selectedOptions = [];
const selectedOptionMap = new Map();
// Ricevi la lista di paesi dal processo principale
window.addEventListener('DOMContentLoaded', () => {
    // Funzione per ricevere la lista dei paesi dal processo principale
    window.electronAPI.riceviListaPaesi((righe) => {
        // Se il modulo è stato correttamente ricevuto
        if (righe && righe.length > 0) {
            const selectElement = document.getElementById('countriesSelect');
            const optionsContainer = document.querySelector('.options');
            const selectedValuesContainer = document.querySelector('.selected-values');

            // Funzione per aprire la modale
            // Funzione per aprire la modale
// Funzione per aprire la modale
function openModal(countryName) {
    const modal = document.getElementById('myModal');
    const modalContent = document.querySelector('.modal-content');
    
    

    // Imposta il contenuto della modale
    modalContent.innerHTML = `
        <p>Paese selezionato: ${countryName}</p>
        <p>Seleziona il numero di partecipanti:</p>
        <input type="number" id="participantsInput" min="1" max="10" value="1">
        <span id="participantsDisplay">1</span> partecipanti
        <button id="okButton">OK</button>
    `;

    // Mostra la modale
    modal.style.display = 'block';
    const okButton = document.getElementById('okButton'); // Seleziona il pulsante "OK"
    // Gestisci il cambiamento nel numero di partecipanti
    const participantsInput = document.getElementById('participantsInput');
    const participantsDisplay = document.getElementById('participantsDisplay');
    participantsInput.addEventListener('input', () => {
        participantsDisplay.textContent = participantsInput.value;
    });

    

    // Chiudi la modale quando l'utente clicca sul pulsante "OK"
    okButton.addEventListener('click', () => {
        const selectedNumber = participantsInput.value; // Ottieni il numero selezionato
        //selectedOptions.push(`${countryName} (${selectedNumber})`); // Aggiungi il paese selezionato con il numero alla lista di opzioni selezionate
        selectedOptions.push(`${countryName} (${selectedNumber})`);
        selectedOptionMap.set(countryName, selectedNumber);
        updateSelectedValues(); // Aggiorna la visualizzazione delle opzioni selezionate nella select
        modal.style.display = 'none'; // Chiudi la modale
    });
    

    // Chiudi la modale quando l'utente clicca fuori dall'area della modale
    window.addEventListener('click', (event) => {
        if (event.target === modal) {
            modal.style.display = 'none';
        }
    });
}

            // Funzione per aggiungere un'opzione alla lista delle opzioni selezionate
            

            // Funzione per rimuovere un'opzione dalla lista delle opzioni selezionate
            // Funzione per rimuovere un'opzione dalla lista delle opzioni selezionate
function removeSelectedOption(option) {
    selectedOptionMap.delete(option);
    updateSelectedValues();
}

// Funzione per aggiornare il contenuto visibile delle opzioni selezionate
function updateSelectedValues() {
    // Ottieni i valori della mappa (paese, numero) e crea un array di stringhe con il formato "paese (numero)"
    const selectedOptionsArray = Array.from(selectedOptionMap.entries()).map(([country, number]) => `${country} (${number})`);
    // Aggiorna la visualizzazione delle opzioni selezionate
    selectedValuesContainer.innerHTML = selectedOptionsArray.join(', ');
    // Aggiorna il valore della select nascosta
    selectElement.value = selectedOptionsArray.join(', ');
}


            // Itera attraverso le righe della lista dei paesi
            righe.forEach((countryName) => {
                // Crea un'opzione per ogni paese
                const optionElement = document.createElement('option');
                optionElement.value = countryName;
                optionElement.textContent = countryName;

                // Aggiungi l'opzione al select
                selectElement.appendChild(optionElement);

                // Aggiungi un'opzione alla lista visualizzata quando si clicca sulla select
                const optionDiv = document.createElement('div');
                optionDiv.classList.add('option');
                optionDiv.textContent = countryName;
                optionDiv.addEventListener('click', () => {
                    // Verifica se l'opzione è già stata selezionata
                    if (selectedOptionMap.has(countryName)) {
                        // Rimuovi l'opzione dalla lista delle opzioni selezionate
                        console.log("oakle")
                        removeSelectedOption(countryName);
                    } else {
                        // Aggiungi l'opzione alla lista delle opzioni selezionate
                        
                        // Apri la modale per visualizzare il paese selezionato
                        openModal(countryName);
                    }
                });
                optionsContainer.appendChild(optionDiv);
            });

            // Aggiungi un gestore di eventi al container custom-select per visualizzare o nascondere le opzioni
            const customSelectContainer = document.querySelector('.custom-select');
            customSelectContainer.addEventListener('click', () => {
                optionsContainer.classList.toggle('active');
            });
        } else {
            console.error('Lista dei paesi non disponibile');
        }
    });
});
