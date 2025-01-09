function showWarning() {
    const modelSelect = document.getElementById('model');
    const trainButton = document.getElementById('trainButton');
    if (modelSelect.value === 'train') {
        trainButton.style.display = 'block';
        alert('Warning: Training the model might take a lot of time.');
    } else {
        trainButton.style.display = 'none';
    }
}

function trainModel() {
    const statusBox = document.getElementById("statusBox");
    const summarizeButton = document.getElementById("summarizeButton");
    summarizeButton.disabled = true;

    // Show training in progress
    statusBox.innerHTML = `
        <div class="alert alert-info mt-4" role="alert">
            Training in process. Please look at the terminal for more details.
        </div>
    `;

    // Start the training
    fetch('/train')
        .then(response => response.json())
        .then(data => {
            if (data.status === "completed") {
                statusBox.innerHTML = `
                    <div class="alert alert-success mt-4" role="alert">
                        ${data.message}
                    </div>
                `;
            } else if (data.status === "error") {
                statusBox.innerHTML = `
                    <div class="alert alert-danger mt-4" role="alert">
                        ${data.message}
                    </div>
                `;
            }

            // Reactivate the summarize button
            summarizeButton.disabled = false;

            // Optionally remove the status box after some time
            setTimeout(() => {
                statusBox.innerHTML = "";
            }, 5000);
        })
        .catch(err => {
            statusBox.innerHTML = `
                <div class="alert alert-danger mt-4" role="alert">
                    An error occurred: ${err}
                </div>
            `;

            summarizeButton.disabled = false; // Reactivate summarize button
        });
}