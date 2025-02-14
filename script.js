// // Function to handle file upload
// function handleFileUpload() {
//     const fileInput = document.getElementById('fileInput');
//     const file = fileInput.files[0];
    
//     // Check if a file is selected
//     if (!file) {
//         alert('Please select a file.');
//         return;
//     }
    
//     // Display a loading message
//     const loadingMessage = document.getElementById('loadingMessage');
//     loadingMessage.innerText = 'Uploading file...';
    
//     // Create a FormData object to send the file to the server
//     const formData = new FormData();
//     formData.append('file', file);
    
//     // Send a POST request to the server
//     fetch('/upload', {
//         method: 'POST',
//         body: formData
//     })
//     .then(response => response.json())
//     .then(data => {
//         // Hide the loading message
//         loadingMessage.innerText = '';

//         // Display the detection result
//         const resultContainer = document.getElementById('resultContainer');
//         resultContainer.innerHTML = '';
        
//         const resultText = document.createElement('p');
//         resultText.innerText = `Detection result: ${data.result}`;
//         resultContainer.appendChild(resultText);
//     })
//     .catch(error => {
//         console.error('Error:', error);
//         alert('An error occurred while uploading the file.');
//         loadingMessage.innerText = '';
//     });
// }
