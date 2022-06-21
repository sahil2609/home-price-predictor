function getValue(val){
    var ui = document.getElementsByName(val)
    for(i in ui){
        if(ui[i].checked){
            return parseInt(i) + 1;
        }
    }

    return - 1;
}

function predictPrice(){
    console.log("tree");
    var bhk = getValue("uiBHK");
    var bath = getValue("uiBath");
    var prediced_price = document.getElementById("uiPredictedPrice");
    var location = document.getElementById("uiLocations");
    var sqft = document.getElementById("uiSqft");

    var url = "http://127.0.0.1:5000/predict_home_price";

    $.post(url, {
        sqft: parseFloat(sqft.value),
        bhk: bhk,
        bath: bath,
        location : location.value
    },
        function(data,status){
            console.log(data.prediced_price);
            prediced_price.innerHTML = "<h2>" + data.predicted_price.toString() + " Lakh</h2>";
            console.log(status);
        }
    );
}



function onPageLoad(){
    console.log("page loaded");
    var url = "http://127.0.0.1:5000/get_location_names";
    //jquery
    $.get(url, function(data, status){
        console.log(data)
        if(data){
            var locations = data.locations;
            console.log(locations)
            var uiLocations = document.getElementById("uiLocations");
            $('#uiLocations').empty();
            for(var i in locations) {
                console.log("hello");
                var opt = new Option(locations[i]);
                $('#uiLocations').append(opt);
            }

        }
    });
}

window.onload = onPageLoad;