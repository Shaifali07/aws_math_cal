       // callAPI function that takes the base and exponent numbers as parameters
        var callAPI = (base,exponent,operation)=>{
            // instantiate a headers object
            var myHeaders = new Headers();
            // add content type header to object
            myHeaders.append("Content-Type", "application/json");
            // using built in JSON utility package turn object to string and store in a variable
            var raw = JSON.stringify({"base":base,"exponent":exponent,"operation":operation});
            // create a JSON object with parameters for API call and store in a variable
            var requestOptions = {
                method: 'POST',
                headers: myHeaders,
                body: raw,
                redirect: 'follow'
            };
            // make API call with parameters and use promises to get response
            fetch("https://onx2acqnb9.execute-api.ap-south-1.amazonaws.com/dev", requestOptions)
            .then(response => response.text())
            .then(result => {
        // Parsing the response and updating the HTML element with ID 'result'
        var parsedResult = JSON.parse(result).body;
        document.getElementById("result").innerHTML = "Result: " + parsedResult;
    })
    .catch(error => console.log('error', error));
        }
  
