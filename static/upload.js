function previewImage(event) {
    const file = event.target.files[0];
    const reader = new FileReader();
    const uploadedImage = document.getElementById("uploadedImage");
    const placeholderText = document.getElementById("placeholderText");

    if (file) {
        reader.onload = function () {
            uploadedImage.src = reader.result;      
            uploadedImage.style.display = "block";
            placeholderText.style.display = "none";  
        };
        reader.readAsDataURL(file);
    } else {
        uploadedImage.src = "";
        uploadedImage.style.display = "none";
        placeholderText.style.display = "block"; 
    }
}

function processImage() {
    const fileInput = document.getElementById("file");
    if (fileInput.files.length === 0) {
        alert("Please upload an image first.");
        return;
    }

    const formData = new FormData();
    formData.append("file", fileInput.files[0]);

    fetch("/upload", {
        method: "POST",
        body: formData,
    })
        .then(response => response.json()) 
        .then(data => {
            console.log("Server result:", data.result); 
            console.log("Server image:", data.image);   
            
            if (data.error) {
                alert(`Error: ${data.error}`);
                return;
            }
            
            const query = `?result=${data.result}&image=${encodeURIComponent(data.image)}`;
            window.location.href = `/result${query}`;
        })
        .catch(error => {
            console.error("Error processing image:", error);
            alert("Error processing the image. Please try again.");
        });
}
