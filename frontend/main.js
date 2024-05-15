const { app, BrowserWindow, ipcMain } = require('electron');
const path = require('path');
const fs = require('fs');

let mainWindow;

app.on('ready', () => {
  mainWindow = new BrowserWindow({
    width: 800,
    height: 600,
    webPreferences: {
      nodeIntegration: true,
      preload: path.join(__dirname, 'preload.js')
    }
  });

  mainWindow.loadFile('index.html');
  mainWindow.webContents.openDevTools();

  mainWindow.webContents.on('did-finish-load', () => {
    fs.readFile('front_country.csv', 'utf8', (err, data) => {
      if (err) {
        console.error('Errore durante la lettura del file CSV:', err);
        return;
      }

      const righe = data.trim().split('\n');
      mainWindow.webContents.send('countries', righe);
    });
  });
});


