$(document).ready(function () {
    let dummydata = {
        "region": {
            "name": "Africa",
            "avgAge": 19.7,
            "avgDailyIncomeInUSD": 5,
            "avgDailyIncomePopulation": 0.71
        },
        "periodType": "days",
        "timeToElapse": 58,
        "reportedCases": 674,
        "population": 66622705,
        "totalHospitalBeds": 1380614
    }
    let cleandata = {
        region: {
            name: "Africa",
            avgAge: 19.7,
            avgDailyIncomeInUSD: 5,
            avgDailyIncomePopulation: 0.71
        },
        periodType: "days",
        timeToElapse: 58,
        reportedCases: 674,
        population: 66622705,
        totalHospitalBeds: 1380614
    }
    $('#json').val(JSON.stringify(dummydata, undefined, 4))

    $("#fetch-response").click(function(e){
        e.preventDefault()
        var data = $("#json").val()
        $.post(
            '/api/v1/on-covid-19',
            data
        ).done(function(data){
            $("#response-data").html(JSON.stringify(data, undefined, 4))
        }).fail(function(jqXHR, textStatus ){
            console.error('Request Failed:'+ textStatus)
        })
    })
});
