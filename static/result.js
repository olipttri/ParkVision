document.addEventListener("DOMContentLoaded", function () {
    const resultTitle = document.querySelector(".result-title");
    const resultDescription = document.getElementById("result-description");

    const params = new URLSearchParams(window.location.search);
    const result = (params.get("result") || "").trim().toLowerCase(); 

    console.log("Extracted result:", result); 

    if (result === "healthy") {
        resultTitle.textContent = "Healthy";
        resultDescription.innerHTML = `
            Great news! Based on the analysis, there are no significant indications of Parkinson's Disease. 
            Stay proactive about your health and consult a doctor if needed.
        `;
    } else if (result === "parkinson detected") {
        resultTitle.textContent = "Parkinson Detected";
        resultDescription.innerHTML = `
            Based on the analysis, there is a possibility of Parkinson's Disease. 
            This result is only an indicative assessment, not a diagnosis. 
            Please consult a healthcare professional for further evaluation.
        `;
    } else {
        resultTitle.textContent = "Processing...";
        resultDescription.textContent = "Your image is currently being processed. Please wait...";
    }
});

function saveResult() {
    alert("Result saved successfully!");
}
