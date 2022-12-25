$("form").validate({
    rules: {
        username: {
            required: true,
            minlength: 2
        },
        email: {
            email: true,
            required: true
        },
        password: {
            required: true,
            minlength: 6
        },
        confirm_password: {
            required: true,
            equalTo: "#pwd"
        }
    },
    messages: {
        username: {
            required: "Please provide a username",
            minlength: "Your username must consist of at least 2 characters"
        },
        email: {
            email: "Enter a valid email address",
            required:"Please enter an email address"
        },
        password: {
            required: "Please provide a password",
            minlength: "Your password must be at least 6 characters long"
        },
        confirm_password: {
            required: "Please provide a password",
            equalTo: "Please enter the same password as above"
        }
    },
    submitHandler: function(form) {
        const username = $("input[type=username]").val();
        const email = $("input[type=email]").val();
        const password = $("input[type=password]").val();
        $.ajax({
            type: "POST",
            url: "http://web-02.feranmi.tech/api/v1/register",
            headers: {
                "Content-Type": "application/json",
                "Access-Control-Allow-Origin": "127.0.0.1:5500"
            },
            data: {"username": username, "email": email, "password": password},
            success: (result) => {
                console.log(result);
                form.submit();
            },
            dataType: "json"
          });
    }
});
