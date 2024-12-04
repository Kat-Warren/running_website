$(document).ready(function() {
    $("#change-password-form").on("submit", function(event) {
        event.preventDefault(); // Prevent default form submission
        console.log("Change password form submitted");

        let new_password = $("#new-password").val();
        let con_password = $("#confirm-password").val();
        
        if (new_password !== con_password) {
            alert("Passwords do not match!");
            return;
        }

        console.log("New Password:", new_password);

        // Make the AJAX request
        $.ajax({
            url: "/change_password", // Match your Flask route
            type: "POST",            // Ensure POST is used
            contentType: "application/json",
            data: JSON.stringify({ new_password: new_password }),
            success: function(response) {
                console.log(response.message);
                alert("Password change successful: " + response.message);
            },
            error: function(xhr) {
                console.error(xhr.responseJSON?.message || "An error occurred.");
                alert("Password change failed: " + (xhr.responseJSON?.message || "Unknown error."));
            },
        });
    });
});


