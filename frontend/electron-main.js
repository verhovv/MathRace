import {app, BrowserWindow, Menu} from 'electron';

function createWindow() {
    let mainWindow = new BrowserWindow({
        width: 1100,
        height: 900,
        minWidth: 1100,
        minHeight: 900,
        title: 'MathRace',
    });

    mainWindow.loadURL('http://localhost:4173/');

    mainWindow.on('closed', () => {
        mainWindow = null;
    });
}

app.on('ready', () => {
    createWindow();
    const menu = Menu.buildFromTemplate([]);
    Menu.setApplicationMenu(menu);
});
app.on('window-all-closed', () => {
    app.quit();
});
