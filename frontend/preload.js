const { contextBridge, ipcRenderer } = require('electron');

// Esponi solo le funzionalità necessarie
contextBridge.exposeInMainWorld(
  'electronAPI', {
    // Funzione per ricevere la lista dei paesi dal processo principale
    riceviListaPaesi: (callback) => {
      ipcRenderer.on('countries', (_, righe) => {
        callback(righe);
      });
    }
  }
);

