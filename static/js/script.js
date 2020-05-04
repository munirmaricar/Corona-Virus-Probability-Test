var result = [];

$(document).ready(
    $('#resultBtn').submit(function (event) {
        event.preventDefault();
        // const result_q = $('#input').val();
        // result[0] = result_q;
        // console.log(result_q);
        $.ajax({
            type: 'GET',
            // Ganti API KEY dengan key pribadi
            url: "https://api.typeform.com/forms/jmYMsH/responses?page_size=25",
            datatype: "json",
            success: function (data) {
                console.log(data.items);
            }
        });
        // }
        // var xhttp = new XMLHttpRequest();
        // xhttp.onreadystatechange = function () {
        //     if (this.readyState == 4 && this.status == 200) {
        //         var data = JSON.parse(this.responseText);
        //         console.log(data.items);
        //     }
        // }
        // xhttp.open("GET", "https://api.typeform.com/forms/jmYMsH/responses", true)
        // xhttp.send()
    })
)