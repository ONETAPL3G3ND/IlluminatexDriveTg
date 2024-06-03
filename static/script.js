let tg = window.Telegram.WebApp;

tg.expand();

document.addEventListener('DOMContentLoaded', () => {
    const allFilesTab = document.getElementById('all-files-tab');
    const uploadFileTab = document.getElementById('upload-file-tab');
    const allFilesContent = document.getElementById('all-files-content');
    const uploadFileContent = document.getElementById('upload-file-content');
    const createFolderBtn = document.getElementById('create-folder-btn');
    const createFolderModal = document.getElementById('create-folder-modal');
    const closeModal = document.querySelector('.close');
    const createFolderSubmit = document.getElementById('create-folder-submit');
    const filesContainer = document.getElementById('files-container');
    const folderSelect = document.getElementById('folder-select');
    const uploadFileBtn = document.getElementById('upload-file-btn');

    // Tab switching
    allFilesTab.addEventListener('click', (e) => {
        e.preventDefault();
        switchTab(allFilesTab, allFilesContent);
    });

    uploadFileTab.addEventListener('click', (e) => {
        e.preventDefault();
        switchTab(uploadFileTab, uploadFileContent);
    });

    function switchTab(tab, content) {
        document.querySelectorAll('nav ul li a').forEach(a => a.classList.remove('active'));
        document.querySelectorAll('.tab-content').forEach(c => c.classList.remove('active'));
        tab.classList.add('active');
        content.classList.add('active');
    }

    // Fetch files and populate the container
    function fetchFiles() {
    fetch('https://brief-evident-ant.ngrok-free.app/files/')
        .then(response => response.json())
        .then(data => {
            filesContainer.innerHTML = '';
            data.files.forEach(file => {
                const fileCard = document.createElement('div');
                fileCard.className = 'file-card';
                fileCard.innerHTML = `
                    <h3>${file.name}</h3>
                    <p>Size: ${file.size} </p>
                    <p>Created: ${file.creation_date}</p>
                    <button onclick="downloadFile('${file.name}')">Download</button>
                    <button onclick="deleteFile('${file.name}')">Delete</button>
                `;
                filesContainer.appendChild(fileCard);
            });
        })
        .catch(error => console.error('Error fetching files:', error));
}

    fetchFiles();


    closeModal.addEventListener('click', () => {
        createFolderModal.style.display = 'none';
    });

    // Upload file
    uploadFileBtn.addEventListener('click', () => {
        const selectedFolder = folderSelect.value;
        tg.sendData(`upload ${selectedFolder}`);
    });
});

function downloadFile(url) {
    tg.sendData(`download ${url}`);
}

function deleteFile(filename) {
    tg.sendData(`delete ${filename}`);
}
