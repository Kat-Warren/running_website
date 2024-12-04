$(document).ready(function() {

    $("#register-form").on("submit", function(event){
        event.preventDefault();
        console.log("Form submission intercepted");

        let username = $("#username").val();
        let password = $("#password").val();

        console.log("Username:", username);
        console.log("Password:", password);

        // Checks to make sure both are non empty
        if (!username || !password) {
            alert("Please enter both username and password.");
            return;
        }

        $.ajax({
            url: "/register",
            type: "POST",
            contentType: "application/json",
            data: JSON.stringify({          // Serialize data as JSON
                username: $("#username").val(),
                password: $("#password").val(),
            }),
            success: function (response) {
                alert(response.message); // Show success message
                if (response.status === 'success') {
                    window.location.href = "/login";
                }
                $("#register-form")[0].reset();

            },
            error: function (xhr) {
                let errorMessage = xhr.responseJSON?.message || "An unknown error occurred.";
                alert(errorMessage);
            },
        });
    });
});
        