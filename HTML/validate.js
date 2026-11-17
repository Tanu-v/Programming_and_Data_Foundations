function validateForm() {
    let name = document.getElementById("name").value.trim();
    let mother = document.getElementById("mother").value.trim();
    let subject = document.getElementById("subject").value;
    let fee = document.getElementById("fee").value.trim();
    let registered = document.querySelector('input[name="registered"]:checked');
    let edu = document.getElementById("edu").value.trim();

    if (name === "" || mother === "" || subject === "" || fee === "" || !registered || edu === "") {
        alert("All fields must be filled out!");
        return false; // prevents submission
    }
    return true; // form will submit
}
