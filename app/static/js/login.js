
$(document).ready(function() {

    $("#login-form").on("submit", function(event){
        event.preventDefault();
        console.log("Form submitted");

        let username = $("#username").val();
        let password = $("#password").val();
        
        if (!username || !password) {
            alert("Username or password is missing!");
            return;
        }
        console.log("Username:", username, "Password:", password);
        jQuery.ajax({
            url: "/login",
            type: "POST",
            contentType: "application/json",
            data: JSON.stringify({ username: username, password: password }),
            success: function (response) {
                // Handle success
                console.log(response.message);
                if (response.message) {
                    alert("Login successful: " + response.message);
                } else {
                    alert("Login successful, but no message was provided.");
                }
            },
            error: function (xhr) {
                // Handle error
                console.log(xhr.responseJSON.message);
                alert("Login failed: " + xhr.responseJSON.message);
            },
        });
    });
});
        

























