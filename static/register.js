function validateAll() {
    console.log("Validating form...");
    const name = document.getElementById("name");
    const gender = document.getElementById("gender");
    const dob = document.getElementById("dob");
    const phone = document.getElementById("phone");
    const email = document.getElementById("email");
    const address = document.getElementById("address");
    const password = document.getElementById("password");
    const confirmPassword = document.getElementById("confirmPassword");
    const terms = document.getElementById("terms");

    if (
        name.value.trim() === "" ||
        gender.value.trim() === "" ||
        dob.value.trim() === "" ||
        phone.value.trim() === "" ||
        email.value.trim() === "" ||
        address.value.trim() === "" ||
        password.value.trim() === "" ||
        confirmPassword.value.trim() === ""
    ) {
        alert("All Fields Must be Filled");
        return;
    }

    if (!email.value.includes("@") || !email.value.includes(".")) {
        alert("Invalid email format");
        return;
    }

    if (password.value !== confirmPassword.value) {
        alert("Passwords do not match");
        return;
    }

    if (!/^\d{10,}$/.test(phone.value)) {
        alert("Phone number must contain at least 10 digits");
        return;
    }

    if (!terms.checked) {
        alert("You must accept the Terms & Conditions");
        return;
    }

    const today = new Date();
    const birthDate = new Date(dob.value);
    const age = today.getFullYear() - birthDate.getFullYear();
    const m = today.getMonth() - birthDate.getMonth();
    if (m < 0 || (m === 0 && today.getDate() < birthDate.getDate())) {
        age--;
    }

    if (age < 17) {
        alert("You must be at least 17 years old to register");
        return;
    }

    alert("Registration Successful!");
    document.getElementById("registerForm").submit();
}
