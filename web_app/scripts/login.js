$("form").submit((event) => {
    const username = $("input:first").val();
    const password = $("input#password").val();
    const url = 'http://web-02.feranmi.tech/api/v1/biodata/' + username;
    $.get(url , (result) => {
        console.log(result);
    });
    event.preventDefault;
});